## NetScaler VPX Express 
NetScaler VPX Express is a free virtual application delivery controller (normal hourly Azure Virtual Machine rates apply). This Azure custom template deployment can be used for light production loads, testing and prototyping needs. 


## Azure Custom Template description
This template creates an instance of the VPX Express from the VPX Express SKU image utilising a single subnet within provided virtual network. This template also utilizes a custom script that initializes the VPX instance. Initial configuration performed by the custom script includes network interface configuration, VIP configuration and feature configuration. Further configuration can be performed by logging in to the GUI or via SSH.

## Network architecture
The Azure custom template deploys the VPX in a single-NIC mode. The standard NetScaler IP addresses: NSIP (management IP), VIP (where load balanced applications are accessed) and SNIP (the IP used to send traffic to backend instances) are all provisioned on the single NIC and are drawn from the (RFC1918) address space of the provided virtual network's subnet.  The (RFC1918) NSIP is mapped to the Public IP of the VPX Instance and the RFC1918 VIP is mapped to another public IP.

## Quick Launch Link

[![Create NetScaler VPX Express](http://azuredeploy.net/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fnetscaler-azure-templates%2Fmaster%2Ftemplates%2Fexpress_single_nic%2FmainTemplate.json)


## Additional Links:

- VPX installation in Azure : https://docs.citrix.com/en-us/netscaler/12/deploying-vpx/deploy-vpx-on-azure.html
- NetScaler 12.0 Documentation : https://docs.citrix.com/en-us/netscaler/12.html 
- NetScaler Overview : https://www.citrix.com/products/netscaler-adc/resources/netscaler-vpx.html