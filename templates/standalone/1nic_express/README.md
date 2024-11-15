## Citrix ADC VPX Express

Citrix ADC VPX Express is a free virtual application delivery controller (normal hourly Azure Virtual Machine rates apply). This Azure custom template deployment can be used for light production loads, testing and prototyping needs.

## Azure Custom Template description

This template creates an instance of the VPX Express from the VPX Express SKU image utilising a single subnet within provided virtual network. This template also utilizes a custom script that initializes the VPX instance. Initial configuration performed by the custom script includes network interface configuration, VIP configuration and feature configuration. Further configuration can be performed by logging in to the GUI or via SSH.

## Network architecture

The Azure custom template deploys the VPX in a single-NIC mode. The standard Citrix ADC IP addresses: NSIP (management IP), VIP (where load balanced applications are accessed) and SNIP (the IP used to send traffic to back-end instances) are all provisioned on the single NIC and are drawn from the (RFC1918) address space of the provided virtual network's subnet.  The (RFC1918) NSIP is mapped to the Public IP of the VPX Instance and the RFC1918 VIP is mapped to another public IP.

## Quick Launch Link

[![Create Citrix ADC VPX Express](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fcitrix-adc-azure-templates%2Fmaster%2Ftemplates%2Fstandalone%2F1nic_express%2FmainTemplate.json)
