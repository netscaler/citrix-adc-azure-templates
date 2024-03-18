# How to convert existing ARM templates to provision FIPS enabled VPX builds

## Steps

> Users can directly edit the ARM template in the portal using edit template and edit parameter option.

### 1. Using edit template change the below param by adding  `netscalerfipsbyol`

``` json
"vmSku": {
    "defaultValue": "netscalerfipsbyol",
    "type": "String",
    "allowedValues": [
        "netscalerfipsbyol"
    ]
}
```

### 2. Now search for `netscalervpx-130` and replace it with `adcvpxfips-13-1` in two places

``` json
"plan": {
    "name": "[parameters('vmSku')]",
    "publisher": "citrix",
    "product": "adcvpxfips-13-1"
}
 ```

``` json
"imageReference": {
    "publisher": "citrix",
    "offer": "adcvpxfips-13-1",
    "sku": "[parameters('vmSku')]",
    "version": "latest"
}
```

### 3. save the template and click Review+create button

## Validation

``` bash
[user@citrix] ➤ ssh demouser@x.x.x.x
Warning: Permanently added 'x.x.x.x' (RSA) to the list of known hosts.
###############################################################################
# #
# WARNING: Access to this system is for authorized users only #
# Disconnect IMMEDIATELY if you are not an authorized user! #
# #
###############################################################################

demouser@x.x.x.x's password:
> shell
Copyright (c) 1992-2013 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
The Regents of the University of California. All rights reserved.

root@Citrix-ADC-VPX# sysctl netscaler.azure_descr
netscaler.azure_descr: Citrix ADC VPX FIPS BYOL
```
