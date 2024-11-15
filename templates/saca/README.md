# Secure Azure Computing Architecture(SACA) based Deployment

## Description

  This template will deploy resource as per Secure Cloud Computing Architecture. For more info refer to [Secure Cloud Computing Architecture](https://iasecontent.disa.mil/stigs/pdf/SCCA_FRD_v2-9.pdf), published by Defense Information Systems Agency (DISA).

## Deployment Steps

Deployment is split into 2 phases:

+ **Phase 1** lists steps to do automated creation of resource group setup using an ARM template.
+ **Phase 2** lists manual steps needed to complete deployment using setup.

### Phase 1 : ARM template for creating deployment

  This ARM template will do most of the steps needed for deployment. Remaining steps are manual are listed as part of phase 2.

#### Quick Launch Links

| Azure Global Region                                                                                                                                                                                                                   | Azure Government Region                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [![Azure Deploy Button](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fcitrix-adc-azure-templates%2Fmaster%2Ftemplates%2Fsaca%2FmainTemplate.json) | [![Azure Deploy Button](https://aka.ms/deploytoazurebutton)](https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcitrix%2Fcitrix-adc-azure-templates%2Fmaster%2Ftemplates%2Fsaca%2FmainTemplate.json) |

  **NOTE**: ARM Template does partial setup only. There are manual steps to be done before calling deployment successful. Manual steps are listed below as Phase 2.

### Phase 2 : Manual steps to be carried after successful deployment of ARM template

#### STEP 1: Connect to Linux Jumpbox using temporary ALB via ssh

From your local linux machine connect using:

 `ssh <linuxJumpBoxUsername>@<TEMPORARY_ALB_PUBLIC_IP_(T1)>`

where **TEMPORARY_ALB_PUBLIC_IP_(T1)** is populated as output in deployment of template.

For example

    [root@vivek-devbox:~]$ ssh defaultUser@104.46.107.242
    The authenticity of host '104.46.107.242 (104.46.107.242)' can't be established.
    RSA key fingerprint is 6d:b3:dd:2c:6d:ed:f6:c0:d8:93:69:81:6c:c5:77:30.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added '104.46.107.242' (RSA) to the list of known hosts.
    defaultUser@104.46.107.242's password:
    Welcome to Ubuntu 18.04.1 LTS (GNU/Linux 4.15.0-1035-azure x86_64)

    ...

    defaultUser@Linux-JumpBox:~$

#### STEP 2: Connect to Any ADC VPX in External ADC Pair, make it primary and configure VPX with required commands

From connected linux jumpbox, we can connect to each ADC pair and configure them.

##### STEP 2.1

Connect to any VPX in External ADC pair using ssh from linux jumpbox

 `ssh <citrixADCUsername>@<EXTERNAL_ADC_VPX0_MGMT_IP_(EA1)>`

where **EXTERNAL_ADC_VPX0_MGMT_IP_(EA1)** is populated as output in deployment of template.

For example

    defaultUser@Linux-JumpBox:~$ ssh defaultUser@10.100.1.132
    The authenticity of host '10.100.1.132 (10.100.1.132)' can't be established.
    RSA key fingerprint is SHA256:J15HD01dCzgkKhuIHbfCS7HsaRUesKe8MfYRcS+G7og.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added '10.100.1.132' (RSA) to the list of known hosts.
    ###############################################################################
    #                                                                             #
    #        WARNING: Access to this system is for authorized users only          #
    #         Disconnect IMMEDIATELY if you are not an authorized user!           #
    #                                                                             #
    ###############################################################################

    Password:

    ###############################################################################
    #                     CallHome has been enabled by default.                   #
    # This feature lets the Citrix ADC device/instance automatically upload        #
    # diagnostic and usage information to Citrix. This data will help detect      #
    # critical errors and will also be used to improve the features and the       #
    # product.                                                                    #
    #                                                                             #
    # This feature can be configured anytime using the command line interface or  #
    # the configuration utility. Please see the documentation for more details.   #
    ###############################################################################

     Done
    >

##### STEP 2.2

Ensure VPX is in primary state. If not, make it primary. Use command `show ha node 0` to get info about current VPX in HA pair. Ensure `Master State` for Node is `Primary` .

For example

    > sh ha node 0
    1)      Node ID:      0
            IP:    10.100.1.132 (Citrix-ADC-external-VPX-0)
            Node State: UP
            Master State: Primary
            Fail-Safe Mode: OFF
            INC State: ENABLED

    In case, if state is Secondary, run "force ha failover -force" and wait for 15 seconds and verify again

    > sh ha node 0
    1)      Node ID:      0
            IP:    10.100.1.132 (Citrix-ADC-external-VPX-0)
            Node State: UP
            Master State: Secondary
            Fail-Safe Mode: OFF
            INC State: ENABLED

    ...

    > force ha failover -force
    [WARNING]:Force Failover may cause configuration loss, peer health not optimum. Reason(s):

    - HA heartbeats not seen on some interfaces

     Done
     ...

                // Wait for 15 seconds
    > sh ha node 0
    1)      Node ID:      0
            IP:    10.100.1.132 (Citrix-ADC-external-VPX-0)
            Node State: UP
            Master State: Primary
            Fail-Safe Mode: OFF

##### STEP 2.3

Execute config commands on VPX. Commands to be executed are populated as output **BATCH_CMD_EXTERNAL_ADC_PRIMARY** in template deployment. Ensure you are referring to correct variable having **EXTERNAL** keyword. Copy paste the whole string into VPX cli screen and press enter.

For example

    > add route 0.0.0.0 0.0.0.0 10.100.0.1 ; rm route 0.0.0.0 0.0.0.0 10.100.1.129 ; add route 10.100.1.16 255.255.255.240 10.100.0.17 ; add lbvserver ip1http HTTP 104.46.106.141 80 ; add lbvserver ip2ssh TCP 23.101.157.174 22 ; add lbvserver ip3rdp TCP 23.101.157.174 3389 ; add service iadchttp 10.100.1.22 HTTP 80 ; add service iadcssh 10.100.1.22 TCP 22 ; add service iadcrdp 10.100.1.22 TCP 3389 ; bind lbvserver ip1http iadchttp ; bind lbvserver ip2ssh iadcssh ; bind lbvserver ip3rdp iadcrdp ; save config

    ...

     Done
    >

Now type `exit` to exit to linux-jumpbox console.

    > exit
    Bye!
    Connection to 10.100.1.132 closed.

    defaultUser@Linux-JumpBox:~$

#### STEP 3: Connect to Any ADC VPX in Internal ADC Pair, make it primary and configure VPX with required commands

##### STEP 3.1

From connected linux jumpbox, Connect to any VPX in Internal ADC pair using ssh from linux jumpbox

 `ssh <citrixADCUsername>@<INTERNAL_ADC_VPX0_MGMT_IP_(IA1)>`

where **INTERNAL_ADC_VPX0_MGMT_IP_(IA1)** is populated as output in deployment of template.

Refer STEP 2.1 for an example

##### STEP 3.2

Ensure VPX is in primary state. If not, make it primary. Use command `show ha node 0` to get info about current VPX in HA pair. Ensure `Master State` for Node is `Primary` .

Refer STEP 2.2 for an example

##### STEP 3.3

Execute config commands on VPX. Commands to be executed are populated as output **BATCH_CMD_INTERNAL_ADC_PRIMARY** in template deployment. Ensure you are referring to correct variable having **INTERNAL** keyword. Copy paste the whole string into VPX cli screen and press enter.

For example

    > add route 0.0.0.0 0.0.0.0 10.100.1.17 ; rm route 0.0.0.0 0.0.0.0 10.100.1.129 ; add lbvserver ip1http HTTP 10.100.1.22 80 ; add lbvserver ip2ssh TCP 10.100.1.22 22 ; add lbvserver ip3rdp TCP 10.100.1.22 3389 ; add service iadcssh 10.100.1.37 TCP 22 ; add service iadcrdp 10.100.1.38 TCP 3389 ; bind lbvserver ip2ssh iadcssh ; bind lbvserver ip3rdp iadcrdp ; save config

    ...

     Done
    >

Now type `exit` to exit to linux-jumpbox console.

#### STEP 4: Verify ssh/rdp to linux/windows jumpboxes using external ALB public IP2 (IP dedicated for accessing Jumpboxes)

External ALB public IP for Jumpboxes is populated in Deployment output with variable name **EXTERNAL_ALB_PUBLIC_IP_JUMPBOXES_(EL2)** . Use your local linux/windows machine to access jumboxes with this IP.

Steps are:

+ From you local linux machine, ssh to **EXTERNAL_ALB_PUBLIC_IP_JUMPBOXES_(EL2)** to access linux jumpbox. Use linux Jumpbox credentials to connect via ssh.
+ From you local windows machine, rdp to **EXTERNAL_ALB_PUBLIC_IP_JUMPBOXES_(EL2)** to access windows jumpbox's desktop. Use windows Jumpbox credentials to connect via RDP.

#### STEP 5: Delete temporary resources

From Azure portal, Delete following resources present in Resource Group. Delete them in sequence as later is being used by former.

+ Delete `Temporary-ALB-ForSetup`
+ Delete `Temporary-PublicIp-ForSetup` ------------ [ do it after `Temporary-ALB-ForSetup` is successfully deleted]

#### STEP 6: Secure **management_subnet** and **internal_subnet_server** subnets

We now secure `management_subnet` and `internal_subnet_server` subnets by adding them to `securedSubnetRouteTable` route table. This will ensure any access to these subnets are from secure subnets only.

Steps are:

+ From azure portal, go to resource named `securedSubnetRouteTable`
+ In right pane of Route table, click on `Subnets` under `Settings` heading.
+ Click on `Associate` in right pane and Choose Virtual Network `boundary-vnet` and Subnet `management_subnet`. Click `OK`.
+ Again click on `Associate` in right pane and Choose Virtual Network `boundary-vnet` and Subnet `internal_subnet_server`. Click `OK`.
+ Wait for success notifications.

## Congratulations! Your Deployment is complete and secure
