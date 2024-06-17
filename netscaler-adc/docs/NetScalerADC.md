## About the connector
The NetScaler appliance is an application switch which performs application-specific traffic analysis to intelligently distribute, optimize, and secure Layer 4-Layer 7 (L4–L7) network traffic for web applications.
<p>This document provides information about the NetScaler ADC Connector, which facilitates automated interactions, with a NetScaler ADC server using FortiSOAR&trade; playbooks. Add the NetScaler ADC Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with NetScaler ADC.</p>
### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-netscaler-adc</pre>

## Prerequisites to configuring the connector
- You must have the credentials of NetScaler ADC server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the NetScaler ADC server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>NetScaler ADC</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>IP address or hostname of the NetScaler server to which you will connect and perform automated operations.
</td>
</tr><tr><td>API Token</td><td>Specify the API Token that is generated through the NetScaler server
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>
## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Create NetScaler ACL Resource</td><td>Creates a new NetScaler ACL(Access Control List) entry resource in your NetScaler server based on the parameters provided</td><td>create_acl_resource <br/>Investigation</td></tr>
<tr><td>Get NetScaler ACL Resource</td><td>Retrieves NetScaler ACL(Access Control List) entry resource in your NetScaler server based on the parameters provided</td><td>get_acl_resource <br/>Investigation</td></tr>
<tr><td>Delete NetScaler ACL Resource</td><td>Deletes NetScaler ACL(Access Control List) entry resource in your NetScaler server based on the parameters provided</td><td>delete_acl_resource <br/>Investigation</td></tr>
<tr><td>Delete NetScaler ACL Resource</td><td>Deletes NetScaler ACL(Access Control List) entry resource in your NetScaler server based on the parameters provided</td><td>delete_acl_resource <br/>Investigation</td></tr>
<tr><td>Change NetScaler ACL Resource State</td><td>Changes NetScaler ACL(Access Control List) entry resource state(Enable/Disable) in your NetScaler server based on the parameters provided</td><td>change_acl_resource_state <br/>Investigation</td></tr>
</tbody></table>
### operation: Create NetScaler ACL Resource
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>ACL Name</td><td>Specify the Name for the extended ACL rule
</td></tr><tr><td>ACL Action</td><td>Specify the action to perform on incoming IPv4 packets that match the extended ACL rule
</td></tr><tr><td>Source IP</td><td>Specify the IP address or range of IP addresses to match against the source IP address of an incoming IPv4 packet
</td></tr><tr><td>Destination IP</td><td>Specify the IP address or range of IP addresses to match against the destination IP address of an incoming IPv4 packet
</td></tr><tr><td>Other Fields</td><td>Specify fields in the JSON format to be sent as json_data according to NetScaler REST API Documentation. https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release/configuration/ns/nsacl.html
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Get NetScaler ACL Resource
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>ACL Name</td><td>Specify the Name for the extended ACL rule that you want to retrieve. By default all ACL will be fetched
</td></tr><tr><td>Page Size</td><td>Specify the Number of results to return per page.
</td></tr><tr><td>Page Number</td><td>Specify the page number of results to be fetched
</td></tr><tr><td>Other Fields</td><td>Specify fields in the JSON format to be sent as json_data according to NetScaler REST API Documentation. https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release/configuration/ns/nsacl.html
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Delete NetScaler ACL Resource
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>ACL Name</td><td>Specify the Name for the extended ACL rule that you want to delete
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Delete NetScaler ACL Resource
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>ACL Name</td><td>Specify the Name for the extended ACL rule that you want to delete
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Change NetScaler ACL Resource State
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>ACL Name</td><td>Specify the Name for the extended ACL rule that you want to delete
</td></tr><tr><td>Action</td><td>Specify the Action for the extended ACL rule to apply
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - netscaler-adc - 1.0.0` playbook collection comes bundled with the NetScaler ADC connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the NetScaler ADC connector.

- Change NetScaler ACL Resource State
- Create NetScaler ACL Resource
- Delete NetScaler ACL Resource
- Delete NetScaler ACL Resource
- Get NetScaler ACL Resource

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
