# Citrix ADC VPX High Availability(HA) Pair

You can deploy a pair of  Citrix ADC virtual appliances with single/multiple NIC(s) in an active-passive high availability (HA) setup on Azure. Each NIC can contain multiple IP addresses.

An active-passive deployment requires:

* An HA Independent Network Configuration (INC) configuration
* The Azure Load Balancer (ALB) in Direct Server Return (DSR) mode

All traffic goes through the primary node. The secondary node remains in standby mode until the primary node fails.
Citrix ADC VPX Express is a free virtual application delivery controller (normal hourly Azure Virtual Machine rates apply). This Azure custom template deployment can be used for light production loads, testing and prototyping needs.

## Azure Custom Template description

Citrix Citrix ADC High Availability (HA) Azure Resource Manager (ARM) templates are designed to ensure easy and consistent way of deploying Citrix ADC pair in Active-Passive mode. This template increases reliability and system availability with built in redundancy. This ARM template supports Bring Your Own License (BYOL) or Hourly based selection. Choice of selection is offered during template deployment.

## Quick Launch Link
<table>
  <thead>
    <tr>
      <th colspan="3">Use Case</th>
      <th>Template</th>
      <th>Quick Launch</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="6">Availability Set</td>
      <td rowspan="4">Public VIP</td>
      <td>1nic</td>
      <td>
        <a href="./availability_set/public_vip/1nic">template</a>
      </td>
      <td>
        <a
          href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fcitrix-adc-azure-templates%2Fmaster%2Ftemplates%2Fhigh_availability%2Favailability_set%2Fpublic_vip%2F1nic%2FmainTemplate.json"
        >
          <img src="https://aka.ms/deploytoazurebutton" />
        </a>
      </td>
    </tr>
    <tr>
      <td>2nic</td>
      <td>
        <a href="./availability_set/public_vip/2nic">template</a>
      </td>
      <td>
        <a
          href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fcitrix-adc-azure-templates%2Fmaster%2Ftemplates%2Fhigh_availability%2Favailability_set%2Fpublic_vip%2F2nic%2FmainTemplate.json" target="_blank" rel="noopener noreferrer"
        >
          <img src="https://aka.ms/deploytoazurebutton" />
        </a>
      </td>
    </tr>
    <tr>
      <td>3nic</td>
      <td>
        <a href="./availability_set/public_vip/3nic">template</a>
      </td>
      <td>
        <a
          href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fcitrix-adc-azure-templates%2Fmaster%2Ftemplates%2Fhigh_availability%2Favailability_set%2Fpublic_vip%2F3nic%2FmainTemplate.json" target="_blank" rel="noopener noreferrer"
        >
          <img src="https://aka.ms/deploytoazurebutton" />
        </a>
      </td>
    </tr>
    <tr>
      <td>3nic_backend_autoscale</td>
      <td>
        <a href="./availability_set/public_vip/3nic_backend_autoscale"
          >template</a
        >
      </td>
      <td>
        <a
          href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fcitrix-adc-azure-templates%2Fmaster%2Ftemplates%2Fhigh_availability%2Favailability_set%2Fpublic_vip%2F3nic_backend_autoscale%2FmainTemplate.json" target="_blank" rel="noopener noreferrer"
        >
          <img src="https://aka.ms/deploytoazurebutton" />
        </a>
      </td>
    </tr>
    <tr>
      <td rowspan="2">Private VIP</td>
      <td>1nic</td>
      <td>
        <a href="./availability_set/private_vip/1nic">template</a>
      </td>
      <td>
        <a
          href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fcitrix-adc-azure-templates%2Fmaster%2Ftemplates%2Fhigh_availability%2Favailability_set%2Fprivate_vip%2F1nic%2FmainTemplate.json" target="_blank" rel="noopener noreferrer"
        >
          <img src="https://aka.ms/deploytoazurebutton" />
        </a>
      </td>
    </tr>
    <tr>
      <td>3nic</td>
      <td>
        <a href="./availability_set/private_vip/3nic">template</a>
      </td>
      <td>
        <a
          href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fcitrix-adc-azure-templates%2Fmaster%2Ftemplates%2Fhigh_availability%2Favailability_set%2Fprivate_vip%2F3nic%2FmainTemplate.json" target="_blank" rel="noopener noreferrer"
        >
          <img src="https://aka.ms/deploytoazurebutton" />
        </a>
      </td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td rowspan="3">Availability Zone</td>
      <td rowspan="2">Public VIP</td>
      <td>3nic</td>
      <td>
        <a href="./availability_zone/public_vip/3nic">template</a>
      </td>
      <td>
        <a
          href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fcitrix-adc-azure-templates%2Fmaster%2Ftemplates%2Fhigh_availability%2Favailability_zone%2Fpublic_vip%2F3nic%2FmainTemplate.json" target="_blank" rel="noopener noreferrer"
        >
          <img src="https://aka.ms/deploytoazurebutton" />
        </a>
      </td>
    </tr>
    <tr>
      <td>3nic_backend_autoscale</td>
      <td>
        <a href="./availability_zone/public_vip/3nic_backend_autoscale"
          >template</a
        >
      </td>
      <td>
        <a
          href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fcitrix-adc-azure-templates%2Fmaster%2Ftemplates%2Fhigh_availability%2Favailability_zone%2Fpublic_vip%2F3nic_backend_autoscale%2FmainTemplate.json" target="_blank" rel="noopener noreferrer"
        >
          <img src="https://aka.ms/deploytoazurebutton" />
        </a>
      </td>
    </tr>
    <tr>
      <td rowspan="1">Private VIP</td>
      <td>3nic</td>
      <td>
        <a href="./availability_zone/private_vip/3nic">template</a>
      </td>
      <td>
        <a
          href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fcitrix-adc-azure-templates%2Fmaster%2Ftemplates%2Fhigh_availability%2Favailability_zone%2Fprivate_vip%2F3nic%2FmainTemplate.json" target="_blank" rel="noopener noreferrer"
        >
          <img src="https://aka.ms/deploytoazurebutton" />
        </a>
      </td>
    </tr>
  </tbody>
</table>

## Network architecture and further reading

For understanding architecture or manual deployment steps, refer

* [Deploy a Citrix ADC VPX instance on Microsoft Azure](https://docs.citrix.com/en-us/citrix-adc/current-release/deploying-vpx/deploy-vpx-on-azure.html)
* [Configure a high-availability setup with multiple IP addresses and NICs](https://docs.citrix.com/en-us/citrix-adc/current-release/deploying-vpx/deploy-vpx-on-azure/configure-vpx-pair-ha-inc.html)
* [Configure HA-INC nodes by using the Citrix high availability template with Azure ILB](https://docs.citrix.com/en-us/citrix-adc/current-release/deploying-vpx/deploy-vpx-on-azure/configure-vpx-pair-ha-inc-with-azure-ilb.html)

