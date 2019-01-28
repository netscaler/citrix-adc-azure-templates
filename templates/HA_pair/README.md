## NetScaler VPX High Availability(HA) Pair
You can deploy a pair of  NetScaler virtual appliances with single/multiple NIC(s) in an active-passive high availability (HA) setup on Azure. Each NIC can contain multiple IP addresses.

An active-passive deployment requires:
- An HA Independent Network Configuration (INC) configuration
- The Azure Load Balancer (ALB) in Direct Server Return (DSR) mode

All traffic goes through the primary node. The secondary node remains in standby mode until the primary node fails. 
NetScaler VPX Express is a free virtual application delivery controller (normal hourly Azure Virtual Machine rates apply). This Azure custom template deployment can be used for light production loads, testing and prototyping needs. 

### Azure Custom Template description
Citrix NetScaler High Availability (HA) Azure Resource Manager (ARM) templates are designed to ensure easy and consistent way of deploying NetScaler pair in Active-Passive mode. This template increases reliability and system availability with built in redundancy. This ARM template supports Bring Your Own License (BYOL) or Hourly based selection. Choice of selection is offered during template deployment. 

### Network architecture
For understanding architecture or manual deployment steps, refer
- [Configuring an HA Setup with Multiple IP Addresses and NICs](https://docs.citrix.com/en-us/netscaler/12-1/deploying-vpx/deploy-vpx-on-azure/configure-vpx-pair-ha-inc.html)
- [Configuring an HA Setup with a Single IP Address and a Single NIC](https://docs.citrix.com/en-us/netscaler/12-1/deploying-vpx/deploy-vpx-on-azure/configure-vpx-ha-mode-arm.html)
- [Add Azure autoscale settings](https://docs.citrix.com/en-us/netscaler/12-1/deploying-vpx/deploy-vpx-on-azure/Autoscale.html)

### Quick Launch Link
---
#### NetScaler High Availability(HA) Pair - 3 NICs 
##### &nbsp;&nbsp;&nbsp;&nbsp; using Availability Set:
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [![Create NetScaler High Availability(HA) Pair - 3 NICs (using Availability Set)](http://azuredeploy.net/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fnetscaler-azure-templates%2Fmaster%2Ftemplates%2FHA_pair%2FHA_3nic%2FmainTemplate.json) 

##### &nbsp;&nbsp;&nbsp;&nbsp; using Availability Zones:
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [![Create NetScaler High Availability(HA) Pair - 3 NICs (using Availability Zones)](http://azuredeploy.net/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fnetscaler-azure-templates%2Fmaster%2Ftemplates%2FHA_pair%2FHA_3nic_zones%2FmainTemplate.json)
&nbsp;

---
#### NetScaler High Availability(HA) Pair with autoscale - 3 NICs
##### &nbsp;&nbsp;&nbsp;&nbsp; using Availability Set:
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [![Create NetScaler High Availability(HA) Pair with autoscale - 3 NICs (using Availability Set)](http://azuredeploy.net/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fnetscaler-azure-templates%2Fmaster%2Ftemplates%2FHA_pair%2FHA_3nic_backendAutoscale%2FmainTemplate.json)

##### &nbsp;&nbsp;&nbsp;&nbsp; using Availability Zones:
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [![Create NetScaler High Availability(HA) Pair with autoscale - 3 NICs (using Availability Zones)](http://azuredeploy.net/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fnetscaler-azure-templates%2Fmaster%2Ftemplates%2FHA_pair%2FHA_3nic_backendAutoscale_zones%2FmainTemplate.json)

---
#### NetScaler High Availability(HA) Pair - 2 NICs
##### &nbsp;&nbsp;&nbsp;&nbsp; using Availability Set:
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [![Create NetScaler High Availability(HA) Pair - 2 NICs (using Availability Set)](http://azuredeploy.net/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fnetscaler-azure-templates%2Fmaster%2Ftemplates%2FHA_pair%2FHA_2nic%2FmainTemplate.json)


---
#### NetScaler High Availability(HA) Pair - 1 NIC
##### &nbsp;&nbsp;&nbsp;&nbsp; using Availability Set:
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [![Create NetScaler High Availability(HA) Pair - 1 NIC (using Availability Set)](http://azuredeploy.net/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fnetscaler-azure-templates%2Fmaster%2Ftemplates%2FHA_pair%2FHA_1nic%2FmainTemplate.json)


---
