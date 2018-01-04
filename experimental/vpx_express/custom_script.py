#!/usr/bin/env python
import logging
import os
import urllib2
import time
import json
import socket
import struct
import base64
import requests
import sys


# Globals
AZURE_CUST_DATA_FILE = "/nsconfig/.AZURE/customdata"

# Set logging
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Generic methods


def get_key_value_pair(text):
    if "=" in text:
        return text.split("=", 1)
    return [text, ""]

# Azure specific methods


def get_azure_custom_data():
    try:
        with open(AZURE_CUST_DATA_FILE, "r") as f:
            return base64.b64decode(f.read()).split(";")
    except Exception as e:
        raise Exception(
            'Failed to fetch and decode azure custom data: %s' % str(e))


def get_azure_imds_metadata(url):
    r = requests.get(url, headers={"Metadata": "true"})
    logger.info('IMDS Metadata Request: %s' % url)
    logger.info('IMDS Metadata Response: %s' % r.text)
    return r.json() if r.status_code == 200 else {}


def get_azure_network_imds():
    url = "http://169.254.169.254/metadata/instance/network?api-version=2017-08-01"
    return get_azure_imds_metadata(url)


def _parse_private_ip(networkDict, index):
    return networkDict["interface"][0]["ipv4"]["ipAddress"][index]["privateIpAddress"]


def _parse_public_ip(networkDict, index):
    return networkDict["interface"][0]["ipv4"]["ipAddress"][index]["publicIpAddress"]


def parse_nsip(networkDict):
    return _parse_private_ip(networkDict, 0)


def parse_vip(networkDict):
    return _parse_public_ip(networkDict, 1)


def parse_snip(networkDict):
    return _parse_private_ip(networkDict, 2)


def parse_subnet_mask(networkDict):
    prefix = networkDict["interface"][0]["ipv4"]["subnet"][0]["prefix"]
    mask = (1 << 32) - (1 << 32 >> int(prefix))
    return socket.inet_ntoa(struct.pack('>L', mask))

# NS specific methods


def save_config(usr, pwd, ns_url):
    url = ns_url + 'nitro/v1/config/nsconfig?action=save'

    jsons = '{"nsconfig":{}}'
    logger.info('Initiating NITRO call to save config')
    result = do_nitro_call_with_retry(
        usr, pwd, url, jsons, timeout=10, max_retries=3)
    if not result[0]:
        raise Exception('Failed to save config reason=' + result[1])


def configure_features(usr, pwd, ns_url, features):
    url = ns_url + 'nitro/v1/config/nsfeature?action=enable'

    feat = {'nsfeature': {'feature': features}}
    jsons = json.dumps(feat)
    logger.info('Initiating NITRO call to configure features')
    result = do_nitro_call_with_retry(
        usr, pwd, url, jsons, timeout=10, max_retries=3)
    if not result[0]:
        raise Exception('Failed to configure features reason=' + result[1])


def do_nitro_call_with_retry(
        usr, pwd, url, json_data, timeout, max_retries=9):
    retry_count = 0
    retry = True
    success = False
    failure_reason = ''

    headers = {'Content-Type': 'application/json',
               'X-NITRO-USER': usr, 'X-NITRO-PASS': pwd}
    r = urllib2.Request(url, data=json_data, headers=headers)
    while retry:
        try:
            logger.info('Initiating NITRO call to ' +
                        url + ', data=' + json_data)
            urllib2.urlopen(r, timeout=timeout)
            logger.info('NITRO call to ' + url + ', data=' +
                        json_data + ' succeeded!')
            retry = False
            success = True
        except urllib2.HTTPError as hte:
            if hte.code != 409:
                logger.warning('HTTP Error making NITRO call: Error: ' +
                               str(hte))
                retry = False
                failure_reason = 'NITRO error :' + str(hte)
                if hte.code == 503 or hte.code == 599 or hte.code == 401:
                    # service unavailable or internal error, just sleep and try
                    # again
                    logger.info(
                        'NS VPX is not ready to be configured, service unavailable condition, may retry...')
                    retry = True
                    retry_count += 1
                    if retry_count > max_retries:
                        logger.info(
                            'Too many retries, giving up, retries=' +
                            str(retry_count))
                        retry = False
                        success = False
                        failure_reason = 'Too many retries due to NITRO error ' +\
                                         str(hte)
                        break
                    logger.info(
                        'NS VPX is not ready to be configured, retrying in 10 seconds')
                    time.sleep(10)
            else:
                logger.info('409 conflict: NS VPX already configured, no-op')
                success = True
                retry = False
        except urllib2.URLError as ure:
            logger.warning('URLError during NITRO call: reason=' +
                           str(ure.reason))
            if type(ure.reason).__name__ == 'timeout':
                logger.info('Socket timeout configuring NS VPX')
                retry_count += 1
                if retry_count > 9:
                    logger.info(
                        'Too many timeouts: giving up on configuring NS VPX')
                    retry = False
                    failure_reason = 'Too many retries due to socket timeouts'
                    success = False
                    break
                logger.info(
                    'NS VPX is not ready to be configured, retrying in 10 seconds')
                time.sleep(10)
            else:
                logger.info('Error configuring NS VPX: Irrecoverable error')
                retry = False
                failure_reason = 'Irrecoverable URL error'
                success = False
    return (success, failure_reason)


def configure_ip(usr, pwd, ns_url, ip, subnet_mask, ip_type):
    url = ns_url + 'nitro/v1/config/nsip'
    logger.info('Configuring NSIP: ip= ' + ip + ', mask=' +
                subnet_mask + ', type=' + ip_type)

    jsons = '{"nsip":{"ipaddress":"%s", "netmask":"%s", "type":"%s"}}' % (
        ip, subnet_mask, ip_type)
    result = do_nitro_call_with_retry(
        usr, pwd, url, jsons, timeout=10, max_retries=9)
    if not result[0]:
        raise Exception('Failed to configure NSIP, type=' +
                        ip_type + ', reason=' + result[1])


# main method
if __name__ == "__main__":
    logger.info("azure custom script started")

    logger.info("read custom data into dict")
    cdata = {}
    if os.path.isfile(AZURE_CUST_DATA_FILE):
        for pair in get_azure_custom_data():
            k, v = get_key_value_pair(pair)
            cdata[k] = v
    else:
        logger.error("failed to fetch Azure custom data")
        exit(1)
    logger.info("azure custom data: %s" % cdata)

    logger.info("fetch networking info from metadata service")
    attempts = 0
    networkDict = {}
    while True:
        networkDict = get_azure_network_imds()
        if networkDict:
            break
        elif attempts >= 6:
            logger.error("failed to fetch network info from IMDS")
            exit(1)
        attempts += 1
        time.sleep(30)

    logger.info("read command line parameters")
    if len(sys.argv) < 2:
        logger.error("password is required for nitro calls")
        exit(1)

    try:
        logger.info("intialize variables")
        usr = cdata['username']
        pwd = sys.argv[1]
        nsip = parse_nsip(networkDict)
        vip = parse_vip(networkDict)
        snip = parse_snip(networkDict)
        subnet_mask = parse_subnet_mask(networkDict)
        ns_url = 'https://%s/' % (nsip)

        logger.info('ns_url=' + ns_url)
        logger.info('Going to add a SNIP to the NSIP ENI')
        configure_ip(usr, pwd, ns_url, snip, subnet_mask, 'snip')
        logger.info('Going to add a VIP to the NSIP ENI')
        configure_ip(usr, pwd, ns_url, vip, subnet_mask, 'vip')
        logger.info('Going to configure features')
        configure_features(usr, pwd, ns_url, ['LB', 'CS', 'SSL', 'WL'])
        save_config(usr, pwd, ns_url)
    except Exception as e:
        logger.error("failed to configure. exception: %s" % str(e))

    logger.info("azure custom script finished")
    exit(0)
