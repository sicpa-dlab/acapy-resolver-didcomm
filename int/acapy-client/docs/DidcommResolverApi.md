# acapy_client.DidcommResolverApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_resolver_connection**](DidcommResolverApi.md#register_resolver_connection) | **POST** /resolver/register/{conn_id} | Register DIDcomm resolver.
[**resolver_connection**](DidcommResolverApi.md#resolver_connection) | **GET** /resolver/connections/{conn_id} | Fetch DIDComm Resolver details.
[**resolver_connections**](DidcommResolverApi.md#resolver_connections) | **GET** /resolver/connections | List DIDcomm resolvers.
[**resolver_update_conn_id_post**](DidcommResolverApi.md#resolver_update_conn_id_post) | **POST** /resolver/update/{conn_id} | Update DIDcomm resolvable methods.
[**unset_resolver_connection**](DidcommResolverApi.md#unset_resolver_connection) | **DELETE** /resolver/connections/{conn_id} | Remove an existing connection record.


# **register_resolver_connection**
> ResolverConnection register_resolver_connection(conn_id)

Register DIDcomm resolver.

### Example

```python
import time
import acapy_client
from acapy_client.api import didcomm_resolver_api
from acapy_client.model.resolver_connection import ResolverConnection
from acapy_client.model.connection_register_request import ConnectionRegisterRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = didcomm_resolver_api.DidcommResolverApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    body = ConnectionRegisterRequest(
        methods=[
            "methods_example",
        ],
    ) # ConnectionRegisterRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Register DIDcomm resolver.
        api_response = api_instance.register_resolver_connection(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling DidcommResolverApi->register_resolver_connection: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register DIDcomm resolver.
        api_response = api_instance.register_resolver_connection(conn_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling DidcommResolverApi->register_resolver_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **body** | [**ConnectionRegisterRequest**](ConnectionRegisterRequest.md)|  | [optional]

### Return type

[**ResolverConnection**](ResolverConnection.md)

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

# **resolver_connection**
> ResolverConnection resolver_connection(conn_id)

Fetch DIDComm Resolver details.

### Example

```python
import time
import acapy_client
from acapy_client.api import didcomm_resolver_api
from acapy_client.model.resolver_connection import ResolverConnection
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = didcomm_resolver_api.DidcommResolverApi(api_client)
    conn_id = "conn_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch DIDComm Resolver details.
        api_response = api_instance.resolver_connection(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling DidcommResolverApi->resolver_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**|  |

### Return type

[**ResolverConnection**](ResolverConnection.md)

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

# **resolver_connections**
> ResolverConnectionList resolver_connections()

List DIDcomm resolvers.

### Example

```python
import time
import acapy_client
from acapy_client.api import didcomm_resolver_api
from acapy_client.model.resolver_connection_list import ResolverConnectionList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = didcomm_resolver_api.DidcommResolverApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List DIDcomm resolvers.
        api_response = api_instance.resolver_connections()
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling DidcommResolverApi->resolver_connections: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ResolverConnectionList**](ResolverConnectionList.md)

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

# **resolver_update_conn_id_post**
> ResolverConnection resolver_update_conn_id_post(conn_id)

Update DIDcomm resolvable methods.

### Example

```python
import time
import acapy_client
from acapy_client.api import didcomm_resolver_api
from acapy_client.model.resolver_connection import ResolverConnection
from acapy_client.model.connection_register_request import ConnectionRegisterRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = didcomm_resolver_api.DidcommResolverApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    body = ConnectionRegisterRequest(
        methods=[
            "methods_example",
        ],
    ) # ConnectionRegisterRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update DIDcomm resolvable methods.
        api_response = api_instance.resolver_update_conn_id_post(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling DidcommResolverApi->resolver_update_conn_id_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update DIDcomm resolvable methods.
        api_response = api_instance.resolver_update_conn_id_post(conn_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling DidcommResolverApi->resolver_update_conn_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **body** | [**ConnectionRegisterRequest**](ConnectionRegisterRequest.md)|  | [optional]

### Return type

[**ResolverConnection**](ResolverConnection.md)

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

# **unset_resolver_connection**
> ConnectionRemoveResponse unset_resolver_connection(conn_id)

Remove an existing connection record.

### Example

```python
import time
import acapy_client
from acapy_client.api import didcomm_resolver_api
from acapy_client.model.connection_remove_response import ConnectionRemoveResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = didcomm_resolver_api.DidcommResolverApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove an existing connection record.
        api_response = api_instance.unset_resolver_connection(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling DidcommResolverApi->unset_resolver_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |

### Return type

[**ConnectionRemoveResponse**](ConnectionRemoveResponse.md)

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

