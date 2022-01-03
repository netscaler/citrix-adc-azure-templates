# Citrix ADC (formerly known as Netscaler) Azure Templates

## Latest updates ⚡

> 13.1 version is now available to deploy.

> **Accelerated Networking** capability is enabled to every Citrix ADC interface using ARM templates, by default. [Learn More](https://docs.citrix.com/en-us/citrix-adc/current-release/deploying-vpx/deploy-vpx-on-azure/configure-vpx-to-use-azure-accelerated-networking.html)

## Introduction

Welcome to the GitHub repository for Citrix ADC (formerly known as NetScaler) ARM(Azure Resource Manager) templates. This repository hosts [Citrix ADC](https://www.citrix.com/en-in/products/citrix-adc/) custom templates for deploying Citrix ADC in Microsoft Azure Cloud Services. All of the templates in this repository have been developed and maintained by the Citrix ADC engineering team.

## Citrix ADC: Load Balancer, SSL VPN, WAF& SSO

### Citrix ADC VPX Application Delivery Controller version 13.0

Citrix ADC is an all-in-one web Application Delivery Controller (ADC) that makes applications run faster, reduces web application ownership costs, optimizes the user experience, and makes sure that applications are always available.

Citrix ADC offers many tools for application deployment. Some of the primary tools are:

* Application Acceleration and Application Security
* HTTP Compression and HTTP Caching
* Web Application Firewall (WAF)
* L4-7 Load Balancer
* Global Server Load Balancing (GSLB)
* SSL Acceleration
* Server Offloading
* Server Consolidation
* Content Switching and Content Caching
* High Availability
* Remote Access and Remote Monitoring
* Policy Engine with Multi-Tenancy
* Data Loss Prevention
* Session Persistence
* SSL VPN
* Single Sign-On

As an undisputed leader of service and application delivery, Citrix ADC solutions are deployed in thousands of networks around the globe to optimize, secure and control the delivery of all enterprise and cloud services. Deployed directly in front of web and database servers, Citrix ADC provides an integrated, and easy-to-use platform.

### Citrix ADC version 13.0 High Availability (HA) Pair

Citrix ADC High Availability (HA) Azure Resource Manager (ARM) template is designed to ensure easy and consistent way of deploying Citrix ADC pair in Active-Passive mode. In addition to benefits of standalone Citrix ADC, HA Pair increases reliability and system availability with built in redundancy. This ARM template supports Bring Your Own License (BYOL) or Hourly based selection. Choice of selection is offered during template deployment.

## Citrix ADC VPX in Azure

Standard Citrix ADC VPX offers are available as resources in the Azure portal. This repository is an extension to provide additional deployments supported by Citrix.

## About these templates

Each template in this repository has co-located documentation describing the usage and architecture of the template. The templates attempt to codify recommended deployment architecture of the Citrix ADC VPX, or to introduce the user to the Citrix ADC or to demonstrate a particular feature / edition / option. Users can re-use / modify or enhance the templates to suit their particular production and testing needs. Most templates require sufficient subscriptions to portal.azure.com to create resource and deploy templates.

Citrix ADC VPX Azure Resource Manager (ARM) templates are designed to ensure easy and consistent way of deploying standalone Citrix ADC VPX. These template increases reliability and system availability with built in redundancy. These ARM template supports Bring Your Own License (BYOL) or Hourly based selection. Choice of selection is either mentioned in template desciption or offered during template deployment.

## Versioning

The master branch of the repository generally has the latest version of the template. Older released versions are tagged appropriately as release with Citrix ADC release version. We additionally maintain dedicated branches hosting templates for supported Citrix ADC releases. These branches are named as `CitrixADC<ReleaseVersion>` .

## Support

For production issues with the templates, please contact Citrix Support through your normal support channels. If you have fixes / suggestions for improvements or requests specific to ARM Templates, please raise an issue in this repository.

## Further reading

* [Deploy a Citrix ADC VPX instance on Microsoft Azure](https://docs.citrix.com/en-us/citrix-adc/current-release/deploying-vpx/deploy-vpx-on-azure.html)
* [Citrix ADC 13.0 Product Documentation](https://docs.citrix.com/en-us/citrix-adc/current-release)

## Legal

* [Citrix Privacy Policy](http://www.citrix.com/about/legal/privacy.html)
* [Citrix License](LICENSE.md)
