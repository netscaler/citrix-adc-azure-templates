## Standalone NetScaler VPX 
A single NetScaler VPX instance can be provisioned in Azure Resource Manager (ARM) portal in a standalone mode by creating the virtual machine and configuring other resources. 

For understanding architecture or manual deployment steps, refer 
- [Configuring a Standalone NetScaler Instance in ARM](https://docs.citrix.com/en-us/netscaler/12-1/deploying-vpx/deploy-vpx-on-azure/configure-vpx-standalone-arm.html)
- [Configuring Multiple IP Addresses for a Standalone NetScaler Instance](https://docs.citrix.com/en-us/netscaler/12-1/deploying-vpx/deploy-vpx-on-azure/configuring-multiple-ips-for-vpx-using-azure-resource-manager.html)

### Quick Launch Link
---
#### NetScaler VPX Express
Refer [templates/express_single_nic](../express_single_nic)

---
#### Standalone NetScaler VPX - 3 NICs 
[![Standalone NetScaler VPX - 3 NICs ](http://azuredeploy.net/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fnetscaler-azure-templates%2Fmaster%2Ftemplates%2Fstandalone%2FVPX_3nic%2FmainTemplate.json)

---
#### Standalone NetScaler VPX with autoscale - 3 NICs
[![Standalone NetScaler VPX with autoscale - 3 NICs](http://azuredeploy.net/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fnetscaler-azure-templates%2Fmaster%2Ftemplates%2Fstandalone%2FVPX_3nic_backendAutoscale%2FmainTemplate.json)

---