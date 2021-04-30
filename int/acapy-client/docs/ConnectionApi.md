# acapy_client.ConnectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_invitation**](ConnectionApi.md#accept_invitation) | **POST** /connections/{conn_id}/accept-invitation | Accept a stored connection invitation
[**accept_request**](ConnectionApi.md#accept_request) | **POST** /connections/{conn_id}/accept-request | Accept a stored connection request
[**connections**](ConnectionApi.md#connections) | **GET** /connections | Query agent-to-agent connections
[**create_invitation**](ConnectionApi.md#create_invitation) | **POST** /connections/create-invitation | Create a new connection invitation
[**create_static**](ConnectionApi.md#create_static) | **POST** /connections/create-static | Create a new static connection
[**delete_connection**](ConnectionApi.md#delete_connection) | **DELETE** /connections/{conn_id} | Remove an existing connection record
[**establish_inbound**](ConnectionApi.md#establish_inbound) | **POST** /connections/{conn_id}/establish-inbound/{ref_id} | Assign another connection as the inbound connection
[**get_connection**](ConnectionApi.md#get_connection) | **GET** /connections/{conn_id} | Fetch a single connection record
[**get_endpoints**](ConnectionApi.md#get_endpoints) | **GET** /connections/{conn_id}/endpoints | Fetch connection remote endpoint
[**get_metadata**](ConnectionApi.md#get_metadata) | **GET** /connections/{conn_id}/metadata | Fetch connection metadata
[**receive_invitation**](ConnectionApi.md#receive_invitation) | **POST** /connections/receive-invitation | Receive a new connection invitation
[**set_metadata**](ConnectionApi.md#set_metadata) | **POST** /connections/{conn_id}/metadata | Set connection metadata


# **accept_invitation**
> ConnRecord accept_invitation(conn_id)

Accept a stored connection invitation

### Example

```python
import time
import acapy_client
from acapy_client.api import connection_api
from acapy_client.model.conn_record import ConnRecord
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    mediation_id = "mediation_id_example" # str | Identifier for active mediation record to be used (optional)
    my_endpoint = "my_endpoint_example" # str | My URL endpoint (optional)
    my_label = "my_label_example" # str | Label for connection (optional)

    # example passing only required values which don't have defaults set
    try:
        # Accept a stored connection invitation
        api_response = api_instance.accept_invitation(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ConnectionApi->accept_invitation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Accept a stored connection invitation
        api_response = api_instance.accept_invitation(conn_id, mediation_id=mediation_id, my_endpoint=my_endpoint, my_label=my_label)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ConnectionApi->accept_invitation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional]
 **my_endpoint** | **str**| My URL endpoint | [optional]
 **my_label** | **str**| Label for connection | [optional]

### Return type

[**ConnRecord**](ConnRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accept_request**
> ConnRecord accept_request(conn_id)

Accept a stored connection request

### Example

```python
import time
import acapy_client
from acapy_client.api import connection_api
from acapy_client.model.conn_record import ConnRecord
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    my_endpoint = "my_endpoint_example" # str | My URL endpoint (optional)

    # example passing only required values which don't have defaults set
    try:
        # Accept a stored connection request
        api_response = api_instance.accept_request(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ConnectionApi->accept_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Accept a stored connection request
        api_response = api_instance.accept_request(conn_id, my_endpoint=my_endpoint)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ConnectionApi->accept_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **my_endpoint** | **str**| My URL endpoint | [optional]

### Return type

[**ConnRecord**](ConnRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections**
> ConnectionList connections()

Query agent-to-agent connections

### Example

```python
import time
import acapy_client
from acapy_client.api import connection_api
from acapy_client.model.connection_list import ConnectionList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    alias = "alias_example" # str | Alias (optional)
    invitation_key = "invitation_key_example" # str | invitation key (optional)
    my_did = "my_did_example" # str | My DID (optional)
    state = "init" # str | Connection state (optional)
    their_did = "their_did_example" # str | Their DID (optional)
    their_role = "invitee" # str | Their role in the connection protocol (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Query agent-to-agent connections
        api_response = api_instance.connections(alias=alias, invitation_key=invitation_key, my_did=my_did, state=state, their_did=their_did, their_role=their_role)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias | [optional]
 **invitation_key** | **str**| invitation key | [optional]
 **my_did** | **str**| My DID | [optional]
 **state** | **str**| Connection state | [optional]
 **their_did** | **str**| Their DID | [optional]
 **their_role** | **str**| Their role in the connection protocol | [optional]

### Return type

[**ConnectionList**](ConnectionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invitation**
> InvitationResult create_invitation()

Create a new connection invitation

### Example

```python
import time
import acapy_client
from acapy_client.api import connection_api
from acapy_client.model.invitation_result import InvitationResult
from acapy_client.model.create_invitation_request import CreateInvitationRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    alias = "alias_example" # str | Alias (optional)
    auto_accept = "auto_accept_example" # str | Auto-accept connection (defaults to configuration) (optional)
    multi_use = True # bool | Create invitation for multiple use (default false) (optional)
    public = True # bool | Create invitation from public DID (default false) (optional)
    body = CreateInvitationRequest(
        mediation_id="mediation_id_example",
        metadata={},
        my_label="my_label_example",
        recipient_keys=[
            "recipient_keys_example",
        ],
        routing_keys=[
            "routing_keys_example",
        ],
        service_endpoint="service_endpoint_example",
    ) # CreateInvitationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new connection invitation
        api_response = api_instance.create_invitation(alias=alias, auto_accept=auto_accept, multi_use=multi_use, public=public, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ConnectionApi->create_invitation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias | [optional]
 **auto_accept** | **str**| Auto-accept connection (defaults to configuration) | [optional]
 **multi_use** | **bool**| Create invitation for multiple use (default false) | [optional]
 **public** | **bool**| Create invitation from public DID (default false) | [optional]
 **body** | [**CreateInvitationRequest**](CreateInvitationRequest.md)|  | [optional]

### Return type

[**InvitationResult**](InvitationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_static**
> ConnectionStaticResult create_static()

Create a new static connection

### Example

```python
import time
import acapy_client
from acapy_client.api import connection_api
from acapy_client.model.connection_static_result import ConnectionStaticResult
from acapy_client.model.connection_static_request import ConnectionStaticRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    body = ConnectionStaticRequest(
        alias="alias_example",
        my_did="my_did_example",
        my_seed="my_seed_example",
        their_did="their_did_example",
        their_endpoint="their_endpoint_example",
        their_label="their_label_example",
        their_seed="their_seed_example",
        their_verkey="their_verkey_example",
    ) # ConnectionStaticRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new static connection
        api_response = api_instance.create_static(body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ConnectionApi->create_static: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionStaticRequest**](ConnectionStaticRequest.md)|  | [optional]

### Return type

[**ConnectionStaticResult**](ConnectionStaticResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_connection(conn_id)

Remove an existing connection record

### Example

```python
import time
import acapy_client
from acapy_client.api import connection_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove an existing connection record
        api_response = api_instance.delete_connection(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ConnectionApi->delete_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **establish_inbound**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} establish_inbound(conn_id, ref_id)

Assign another connection as the inbound connection

### Example

```python
import time
import acapy_client
from acapy_client.api import connection_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    ref_id = "ref_id_example" # str | Inbound connection identifier

    # example passing only required values which don't have defaults set
    try:
        # Assign another connection as the inbound connection
        api_response = api_instance.establish_inbound(conn_id, ref_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ConnectionApi->establish_inbound: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **ref_id** | **str**| Inbound connection identifier |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection**
> ConnRecord get_connection(conn_id)

Fetch a single connection record

### Example

```python
import time
import acapy_client
from acapy_client.api import connection_api
from acapy_client.model.conn_record import ConnRecord
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier

    # example passing only required values which don't have defaults set
    try:
        # Fetch a single connection record
        api_response = api_instance.get_connection(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ConnectionApi->get_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |

### Return type

[**ConnRecord**](ConnRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoints**
> EndpointsResult get_endpoints(conn_id)

Fetch connection remote endpoint

### Example

```python
import time
import acapy_client
from acapy_client.api import connection_api
from acapy_client.model.endpoints_result import EndpointsResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier

    # example passing only required values which don't have defaults set
    try:
        # Fetch connection remote endpoint
        api_response = api_instance.get_endpoints(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ConnectionApi->get_endpoints: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |

### Return type

[**EndpointsResult**](EndpointsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**
> ConnectionMetadata get_metadata(conn_id)

Fetch connection metadata

### Example

```python
import time
import acapy_client
from acapy_client.api import connection_api
from acapy_client.model.connection_metadata import ConnectionMetadata
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    key = "key_example" # str | Key to retrieve. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch connection metadata
        api_response = api_instance.get_metadata(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ConnectionApi->get_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch connection metadata
        api_response = api_instance.get_metadata(conn_id, key=key)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ConnectionApi->get_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **key** | **str**| Key to retrieve. | [optional]

### Return type

[**ConnectionMetadata**](ConnectionMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receive_invitation**
> ConnRecord receive_invitation()

Receive a new connection invitation

### Example

```python
import time
import acapy_client
from acapy_client.api import connection_api
from acapy_client.model.conn_record import ConnRecord
from acapy_client.model.receive_invitation_request import ReceiveInvitationRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    alias = "alias_example" # str | Alias (optional)
    auto_accept = "auto_accept_example" # str | Auto-accept connection (defaults to configuration) (optional)
    mediation_id = "mediation_id_example" # str | Identifier for active mediation record to be used (optional)
    body = ReceiveInvitationRequest(
        id="id_example",
        did="did_example",
        image_url="image_url_example",
        label="label_example",
        recipient_keys=[
            "recipient_keys_example",
        ],
        routing_keys=[
            "routing_keys_example",
        ],
        service_endpoint="service_endpoint_example",
    ) # ReceiveInvitationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Receive a new connection invitation
        api_response = api_instance.receive_invitation(alias=alias, auto_accept=auto_accept, mediation_id=mediation_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ConnectionApi->receive_invitation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias | [optional]
 **auto_accept** | **str**| Auto-accept connection (defaults to configuration) | [optional]
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional]
 **body** | [**ReceiveInvitationRequest**](ReceiveInvitationRequest.md)|  | [optional]

### Return type

[**ConnRecord**](ConnRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_metadata**
> ConnectionMetadata set_metadata(conn_id)

Set connection metadata

### Example

```python
import time
import acapy_client
from acapy_client.api import connection_api
from acapy_client.model.connection_metadata import ConnectionMetadata
from acapy_client.model.connection_metadata_set_request import ConnectionMetadataSetRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    body = ConnectionMetadataSetRequest(
        metadata={},
    ) # ConnectionMetadataSetRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set connection metadata
        api_response = api_instance.set_metadata(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ConnectionApi->set_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set connection metadata
        api_response = api_instance.set_metadata(conn_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ConnectionApi->set_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **body** | [**ConnectionMetadataSetRequest**](ConnectionMetadataSetRequest.md)|  | [optional]

### Return type

[**ConnectionMetadata**](ConnectionMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

