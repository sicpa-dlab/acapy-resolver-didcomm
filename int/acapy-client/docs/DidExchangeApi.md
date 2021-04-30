# acapy_client.DidExchangeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**didexchange_conn_id_accept_invitation_post**](DidExchangeApi.md#didexchange_conn_id_accept_invitation_post) | **POST** /didexchange/{conn_id}/accept-invitation | Accept a stored connection invitation
[**didexchange_conn_id_accept_request_post**](DidExchangeApi.md#didexchange_conn_id_accept_request_post) | **POST** /didexchange/{conn_id}/accept-request | Accept a stored connection request
[**didexchange_create_request_post**](DidExchangeApi.md#didexchange_create_request_post) | **POST** /didexchange/create-request | Create request against public DID&#39;s implicit invitation
[**didexchange_receive_request_post**](DidExchangeApi.md#didexchange_receive_request_post) | **POST** /didexchange/receive-request | Receive request against public DID&#39;s implicit invitation


# **didexchange_conn_id_accept_invitation_post**
> ConnRecord didexchange_conn_id_accept_invitation_post(conn_id)

Accept a stored connection invitation

### Example

```python
import time
import acapy_client
from acapy_client.api import did_exchange_api
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
    api_instance = did_exchange_api.DidExchangeApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    my_endpoint = "my_endpoint_example" # str | My URL endpoint (optional)
    my_label = "my_label_example" # str | Label for connection request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Accept a stored connection invitation
        api_response = api_instance.didexchange_conn_id_accept_invitation_post(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling DidExchangeApi->didexchange_conn_id_accept_invitation_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Accept a stored connection invitation
        api_response = api_instance.didexchange_conn_id_accept_invitation_post(conn_id, my_endpoint=my_endpoint, my_label=my_label)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling DidExchangeApi->didexchange_conn_id_accept_invitation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **my_endpoint** | **str**| My URL endpoint | [optional]
 **my_label** | **str**| Label for connection request | [optional]

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

# **didexchange_conn_id_accept_request_post**
> ConnRecord didexchange_conn_id_accept_request_post(conn_id)

Accept a stored connection request

### Example

```python
import time
import acapy_client
from acapy_client.api import did_exchange_api
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
    api_instance = did_exchange_api.DidExchangeApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    mediation_id = "mediation_id_example" # str | Identifier for active mediation record to be used (optional)
    my_endpoint = "my_endpoint_example" # str | My URL endpoint (optional)

    # example passing only required values which don't have defaults set
    try:
        # Accept a stored connection request
        api_response = api_instance.didexchange_conn_id_accept_request_post(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling DidExchangeApi->didexchange_conn_id_accept_request_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Accept a stored connection request
        api_response = api_instance.didexchange_conn_id_accept_request_post(conn_id, mediation_id=mediation_id, my_endpoint=my_endpoint)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling DidExchangeApi->didexchange_conn_id_accept_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional]
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

# **didexchange_create_request_post**
> DIDXRequest didexchange_create_request_post(their_public_did)

Create request against public DID's implicit invitation

### Example

```python
import time
import acapy_client
from acapy_client.api import did_exchange_api
from acapy_client.model.didx_request import DIDXRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = did_exchange_api.DidExchangeApi(api_client)
    their_public_did = "their_public_did_example" # str | Public DID to which to request connection
    mediation_id = "mediation_id_example" # str | Identifier for active mediation record to be used (optional)
    my_endpoint = "my_endpoint_example" # str | My URL endpoint (optional)
    my_label = "my_label_example" # str | Label for connection request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create request against public DID's implicit invitation
        api_response = api_instance.didexchange_create_request_post(their_public_did)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling DidExchangeApi->didexchange_create_request_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create request against public DID's implicit invitation
        api_response = api_instance.didexchange_create_request_post(their_public_did, mediation_id=mediation_id, my_endpoint=my_endpoint, my_label=my_label)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling DidExchangeApi->didexchange_create_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **their_public_did** | **str**| Public DID to which to request connection |
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional]
 **my_endpoint** | **str**| My URL endpoint | [optional]
 **my_label** | **str**| Label for connection request | [optional]

### Return type

[**DIDXRequest**](DIDXRequest.md)

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

# **didexchange_receive_request_post**
> ConnRecord didexchange_receive_request_post()

Receive request against public DID's implicit invitation

### Example

```python
import time
import acapy_client
from acapy_client.api import did_exchange_api
from acapy_client.model.conn_record import ConnRecord
from acapy_client.model.didx_request import DIDXRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = did_exchange_api.DidExchangeApi(api_client)
    alias = "alias_example" # str | Alias for connection (optional)
    auto_accept = "auto_accept_example" # str | Auto-accept connection (defaults to configuration) (optional)
    mediation_id = "mediation_id_example" # str | Identifier for active mediation record to be used (optional)
    my_endpoint = "my_endpoint_example" # str | My URL endpoint (optional)
    body = DIDXRequest(
        id="id_example",
        did="did_example",
        did_docattach={},
        label="label_example",
    ) # DIDXRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Receive request against public DID's implicit invitation
        api_response = api_instance.didexchange_receive_request_post(alias=alias, auto_accept=auto_accept, mediation_id=mediation_id, my_endpoint=my_endpoint, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling DidExchangeApi->didexchange_receive_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias for connection | [optional]
 **auto_accept** | **str**| Auto-accept connection (defaults to configuration) | [optional]
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional]
 **my_endpoint** | **str**| My URL endpoint | [optional]
 **body** | [**DIDXRequest**](DIDXRequest.md)|  | [optional]

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

