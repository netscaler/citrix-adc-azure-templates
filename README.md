# NetScaler Azure Templates

## Introduction
Welcome to the GitHub repository for NetScaler ARM(Azure Resource Manager) templates. This repository hosts [Citrix NetScaler ADC](https://www.citrix.com/products/netscaler-adc/) custom templates for deploying NetScaler ADC in Microsoft Azure Cloud Services. All of the templates in this repository have been developed and maintained by the Citrix NetScaler engineering team. 

## NetScaler ADC: Load Balancer, SSL VPN, WAF& SSO

### NetScaler VPX Application Delivery Controller version 12.1

Citrix NetScaler is an all-in-one web Application Delivery Controller (ADC) that makes applications run faster, reduces web application ownership costs, optimizes the user experience, and makes sure that applications are always available.

Citrix NetScaler offers many tools for application deployment. Some of the primary tools are:
*	Application Acceleration and Application Security
*	HTTP Compression and HTTP Caching
*	Web Application Firewall (WAF)
*	L4-7 Load Balancer
*	Global Server Load Balancing (GSLB)
*	SSL Acceleration
*	Server Offloading
*	Server Consolidation
*	Content Switching and Content Caching
*	High Availability
*	Remote Access and Remote Monitoring
*	Policy Engine with Multi-Tenancy
*	Data Loss Prevention
*	Session Persistence
*	SSL VPN
*	Single Sign-On

As an undisputed leader of service and application delivery, Citrix NetScaler solutions are deployed in thousands of networks around the globe to optimize, secure and control the delivery of all enterprise and cloud services. Deployed directly in front of web and database servers, NetScaler provides an integrated, and easy-to-use platform.

### NetScaler ADC version 12.1 High Availability (HA) Pair

Citrix NetScaler High Availability (HA) Azure Resource Manager (ARM) template is designed to ensure easy and consistent way of deploying NetScaler pair in Active-Passive mode. In addition to benefits of standalone NetScaler ADC, HA Pair increases reliability and system availability with built in redundancy. This ARM template supports Bring Your Own License (BYOL) or Hourly based selection. Choice of selection is offered during template deployment.

## NetScaler VPX in Azure
Standard Citrix NetScaler VPX offers are available as resources in the Azure portal. This repository is an extension to provide additional deployments supported by Citrix.

## About these templates
Each template in this repository has co-located documentation describing the usage and architecture of the template. The templates attempt to codify recommended deployment architecture of the Citrix NetScaler VPX, or to introduce the user to the Citrix NetScaler or to demonstrate a particular feature / edition / option. Users can re-use / modify or enhance the templates to suit their particular production and testing needs. Most templates require sufficient subscriptions to portal.azure.com to create resource and deploy templates.

Citrix NetScaler VPX Azure Resource Manager (ARM) templates are designed to ensure easy and consistent way of deploying standalone NetScaler VPX. These template increases reliability and system availability with built in redundancy. These ARM template supports Bring Your Own License (BYOL) or Hourly based selection. Choice of selection is either mentioned in template desciption or offered during template deployment.

## Template Links
#### [NetScaler VPX Express](templates/express_single_nic/)
#### [Standalone NetScaler VPX Templates](templates/standalone/)
#### [NetScaler High Availability(HA) Pair Templates](templates/HA_pair/)

## Versioning
The master branch of the repository generally has the latest version of the template. Older released versions are tagged appropriately as release with NetScaler release version. We additionally maintain dedicated branches hosting templates for supoprted NetScaler releases. These branches are named as `NetScaler<ReleaseVersion>` 

## Support
For production issues with the templates, please contact Citrix Support through your normal support channels. If you have fixes / suggestions for improvements or requests specific to ARM Templates, please raise an issue in this repository. 

## Further reading
- [Deploy a NetScaler VPX instance on Microsoft Azure](https://docs.citrix.com/en-us/netscaler/12-1/deploying-vpx/deploy-vpx-on-azure.html)
- [Citrix NetScaler 12.1 Product Documentation](https://docs.citrix.com/en-us/netscaler/12-1.html)
- [Citrix NetScaler Overview](https://www.citrix.com/products/netscaler-adc/resources/netscaler-vpx.html)

## Legal
- [Citrix Privacy Policy](http://www.citrix.com/about/legal/privacy.html)
- [Citrix License](LICENSE.md)