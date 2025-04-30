## About the connector
The NetScaler appliance is an application switch which performs application-specific traffic analysis to intelligently distribute, optimize, and secure Layer 4-Layer 7 (L4–L7) network traffic for web applications.
<p>This document provides information about the NetScaler ADC Connector, which facilitates automated interactions, with a NetScaler ADC server using FortiSOAR&trade; playbooks. Add the NetScaler ADC Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with NetScaler ADC.</p>

### Version information

Connector Version: 1.0.1

Authored By: Fortinet

Certified: No
## Release Notes for version 1.0.1
Following enhancements have been made to the NetScaler ADC Connector in version 1.0.1:
<ul>
<li><p>Added parameter "ACL Type" for all action.</p></li>
<li><p>Added support to save configuration after creation of access list.</p></li>

<li><p>Fixed check health which was causing error "Required argument missing [Both 'pagesno' %26 'pagesize' should be given".</p></li>
</ul>

## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-netscaler-adc`

## Prerequisites to configuring the connector
- You must have the URL of NetScaler ADC server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the NetScaler ADC server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>NetScaler ADC</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>IP address or hostname of the NetScaler server to which you will connect and perform automated operations.<br>
<tr><td>API Token<br></td><td>Specify the API Token that is generated through the NetScaler server<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Create NetScaler ACL Resource<br></td><td>Creates a new NetScaler ACL(Access Control List) entry resource in your NetScaler server based on the parameters provided<br></td><td>create_acl_resource <br/>Investigation<br></td></tr>
<tr><td>Get NetScaler ACL Resource<br></td><td>Retrieves NetScaler ACL(Access Control List) entry resource in your NetScaler server based on the parameters provided<br></td><td>get_acl_resource <br/>Investigation<br></td></tr>
<tr><td>Change NetScaler ACL Resource State<br></td><td>Changes NetScaler ACL(Access Control List) entry resource state(Enable/Disable) in your NetScaler server based on the parameters provided<br></td><td>change_acl_resource_state <br/>Investigation<br></td></tr>
<tr><td>Delete NetScaler ACL Resource<br></td><td>Deletes NetScaler ACL(Access Control List) entry resource in your NetScaler server based on the parameters provided<br></td><td>delete_acl_resource <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Create NetScaler ACL Resource
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>ACL Type<br></td><td>Specify the ACL type as Extended ACL or Simple ACL.<br>
</td></tr><tr><td>ACL Name<br></td><td>Specify the Name for the extended ACL rule<br>
</td></tr><tr><td>Source IP<br></td><td>Specify the IP address or range of IP addresses to match against the source IP address of an incoming IPv4 packet<br>
</td></tr><tr><td>Destination IP<br></td><td>Specify the IP address or range of IP addresses to match against the destination IP address of an incoming IPv4 packet<br>
</td></tr><tr><td>ACL Action<br></td><td>Specify the action to perform on incoming IPv4 packets that match the extended ACL rule<br>
</td></tr><tr><td>Other Fields<br></td><td>Specify fields in the JSON format to be sent as json_data according to NetScaler REST API Documentation. https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release/configuration/ns/nsacl.html<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get NetScaler ACL Resource
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>ACL Type<br></td><td>Specify the ACL type as Extended ACL or Simple ACL.<br>
</td></tr><tr><td>ACL Name<br></td><td>Specify the Name for the extended ACL rule that you want to retrieve. By default all ACL will be fetched<br>
</td></tr><tr><td>Page Size<br></td><td>Specify the Number of results to return per page.<br>
</td></tr><tr><td>Page Number<br></td><td>Specify the page number of results to be fetched<br>
</td></tr><tr><td>Other Fields<br></td><td>Specify fields in the JSON format to be sent as json_data according to NetScaler REST API Documentation. https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release/configuration/ns/nsacl.html<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Change NetScaler ACL Resource State
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>ACL Type<br></td><td>Specify the ACL type as Extended ACL or Simple ACL.<br>
</td></tr><tr><td>ACL Name<br></td><td>Specify the Name for the extended ACL rule that you want to delete<br>
</td></tr><tr><td>Action<br></td><td>Specify the Action for the extended ACL rule to apply<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Delete NetScaler ACL Resource
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>ACL Type<br></td><td>Specify the ACL type as Extended ACL or Simple ACL.<br>
</td></tr><tr><td>ACL Name<br></td><td>Specify the Name for the extended ACL rule that you want to delete<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - NetScaler ADC - 1.0.1` playbook collection comes bundled with the NetScaler ADC connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the NetScaler ADC connector.

- Change NetScaler ACL Resource State
- Create NetScaler ACL Resource
- Delete NetScaler ACL Resource
- Get NetScaler ACL Resource

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
