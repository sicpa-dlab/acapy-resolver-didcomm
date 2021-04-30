# acapy_client.MediationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mediation_default_mediator_delete**](MediationApi.md#mediation_default_mediator_delete) | **DELETE** /mediation/default-mediator | Clear default mediator
[**mediation_default_mediator_get**](MediationApi.md#mediation_default_mediator_get) | **GET** /mediation/default-mediator | Get default mediator
[**mediation_keylists_get**](MediationApi.md#mediation_keylists_get) | **GET** /mediation/keylists | Retrieve keylists by connection or role
[**mediation_keylists_mediation_id_send_keylist_query_post**](MediationApi.md#mediation_keylists_mediation_id_send_keylist_query_post) | **POST** /mediation/keylists/{mediation_id}/send-keylist-query | Send keylist query to mediator
[**mediation_keylists_mediation_id_send_keylist_update_post**](MediationApi.md#mediation_keylists_mediation_id_send_keylist_update_post) | **POST** /mediation/keylists/{mediation_id}/send-keylist-update | Send keylist update to mediator
[**mediation_mediation_id_default_mediator_put**](MediationApi.md#mediation_mediation_id_default_mediator_put) | **PUT** /mediation/{mediation_id}/default-mediator | Set default mediator
[**mediation_request_conn_id_post**](MediationApi.md#mediation_request_conn_id_post) | **POST** /mediation/request/{conn_id} | Request mediation from connection
[**mediation_requests_get**](MediationApi.md#mediation_requests_get) | **GET** /mediation/requests | Query mediation requests, returns list of all mediation records
[**mediation_requests_mediation_id_delete**](MediationApi.md#mediation_requests_mediation_id_delete) | **DELETE** /mediation/requests/{mediation_id} | Delete mediation request by ID
[**mediation_requests_mediation_id_deny_post**](MediationApi.md#mediation_requests_mediation_id_deny_post) | **POST** /mediation/requests/{mediation_id}/deny | Deny a stored mediation request
[**mediation_requests_mediation_id_get**](MediationApi.md#mediation_requests_mediation_id_get) | **GET** /mediation/requests/{mediation_id} | Retrieve mediation request record
[**mediation_requests_mediation_id_grant_post**](MediationApi.md#mediation_requests_mediation_id_grant_post) | **POST** /mediation/requests/{mediation_id}/grant | Grant received mediation


# **mediation_default_mediator_delete**
> MediationRecord mediation_default_mediator_delete()

Clear default mediator

### Example

```python
import time
import acapy_client
from acapy_client.api import mediation_api
from acapy_client.model.mediation_record import MediationRecord
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mediation_api.MediationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Clear default mediator
        api_response = api_instance.mediation_default_mediator_delete()
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling MediationApi->mediation_default_mediator_delete: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MediationRecord**](MediationRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_default_mediator_get**
> MediationRecord mediation_default_mediator_get()

Get default mediator

### Example

```python
import time
import acapy_client
from acapy_client.api import mediation_api
from acapy_client.model.mediation_record import MediationRecord
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mediation_api.MediationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get default mediator
        api_response = api_instance.mediation_default_mediator_get()
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling MediationApi->mediation_default_mediator_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MediationRecord**](MediationRecord.md)

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

# **mediation_keylists_get**
> Keylist mediation_keylists_get()

Retrieve keylists by connection or role

### Example

```python
import time
import acapy_client
from acapy_client.api import mediation_api
from acapy_client.model.keylist import Keylist
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mediation_api.MediationApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier (optional) (optional)
    role = "server" # str | Filer on role, 'client' for keys         mediated by other agents, 'server' for keys         mediated by this agent (optional) if omitted the server will use the default value of "server"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve keylists by connection or role
        api_response = api_instance.mediation_keylists_get(conn_id=conn_id, role=role)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling MediationApi->mediation_keylists_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier (optional) | [optional]
 **role** | **str**| Filer on role, &#39;client&#39; for keys         mediated by other agents, &#39;server&#39; for keys         mediated by this agent | [optional] if omitted the server will use the default value of "server"

### Return type

[**Keylist**](Keylist.md)

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

# **mediation_keylists_mediation_id_send_keylist_query_post**
> KeylistQuery mediation_keylists_mediation_id_send_keylist_query_post(mediation_id)

Send keylist query to mediator

### Example

```python
import time
import acapy_client
from acapy_client.api import mediation_api
from acapy_client.model.keylist_query_filter_request import KeylistQueryFilterRequest
from acapy_client.model.keylist_query import KeylistQuery
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mediation_api.MediationApi(api_client)
    mediation_id = "mediation_id_example" # str | Mediation record identifier
    paginate_limit = -1 # int | limit number of results (optional) if omitted the server will use the default value of -1
    paginate_offset = 0 # int | offset to use in pagination (optional) if omitted the server will use the default value of 0
    body = KeylistQueryFilterRequest(
        filter={},
    ) # KeylistQueryFilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send keylist query to mediator
        api_response = api_instance.mediation_keylists_mediation_id_send_keylist_query_post(mediation_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling MediationApi->mediation_keylists_mediation_id_send_keylist_query_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send keylist query to mediator
        api_response = api_instance.mediation_keylists_mediation_id_send_keylist_query_post(mediation_id, paginate_limit=paginate_limit, paginate_offset=paginate_offset, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling MediationApi->mediation_keylists_mediation_id_send_keylist_query_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_id** | **str**| Mediation record identifier |
 **paginate_limit** | **int**| limit number of results | [optional] if omitted the server will use the default value of -1
 **paginate_offset** | **int**| offset to use in pagination | [optional] if omitted the server will use the default value of 0
 **body** | [**KeylistQueryFilterRequest**](KeylistQueryFilterRequest.md)|  | [optional]

### Return type

[**KeylistQuery**](KeylistQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_keylists_mediation_id_send_keylist_update_post**
> KeylistUpdate mediation_keylists_mediation_id_send_keylist_update_post(mediation_id)

Send keylist update to mediator

### Example

```python
import time
import acapy_client
from acapy_client.api import mediation_api
from acapy_client.model.keylist_update import KeylistUpdate
from acapy_client.model.keylist_update_request import KeylistUpdateRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mediation_api.MediationApi(api_client)
    mediation_id = "mediation_id_example" # str | Mediation record identifier
    body = KeylistUpdateRequest(
        updates=[
            KeylistUpdateRule(
                action="add",
                recipient_key="recipient_key_example",
            ),
        ],
    ) # KeylistUpdateRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send keylist update to mediator
        api_response = api_instance.mediation_keylists_mediation_id_send_keylist_update_post(mediation_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling MediationApi->mediation_keylists_mediation_id_send_keylist_update_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send keylist update to mediator
        api_response = api_instance.mediation_keylists_mediation_id_send_keylist_update_post(mediation_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling MediationApi->mediation_keylists_mediation_id_send_keylist_update_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_id** | **str**| Mediation record identifier |
 **body** | [**KeylistUpdateRequest**](KeylistUpdateRequest.md)|  | [optional]

### Return type

[**KeylistUpdate**](KeylistUpdate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_mediation_id_default_mediator_put**
> MediationRecord mediation_mediation_id_default_mediator_put(mediation_id)

Set default mediator

### Example

```python
import time
import acapy_client
from acapy_client.api import mediation_api
from acapy_client.model.mediation_record import MediationRecord
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mediation_api.MediationApi(api_client)
    mediation_id = "mediation_id_example" # str | Mediation record identifier

    # example passing only required values which don't have defaults set
    try:
        # Set default mediator
        api_response = api_instance.mediation_mediation_id_default_mediator_put(mediation_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling MediationApi->mediation_mediation_id_default_mediator_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_id** | **str**| Mediation record identifier |

### Return type

[**MediationRecord**](MediationRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_request_conn_id_post**
> MediationRecord mediation_request_conn_id_post(conn_id)

Request mediation from connection

### Example

```python
import time
import acapy_client
from acapy_client.api import mediation_api
from acapy_client.model.mediation_record import MediationRecord
from acapy_client.model.mediation_create_request import MediationCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mediation_api.MediationApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    body = MediationCreateRequest(
        mediator_terms=[
            "mediator_terms_example",
        ],
        recipient_terms=[
            "recipient_terms_example",
        ],
    ) # MediationCreateRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Request mediation from connection
        api_response = api_instance.mediation_request_conn_id_post(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling MediationApi->mediation_request_conn_id_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Request mediation from connection
        api_response = api_instance.mediation_request_conn_id_post(conn_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling MediationApi->mediation_request_conn_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **body** | [**MediationCreateRequest**](MediationCreateRequest.md)|  | [optional]

### Return type

[**MediationRecord**](MediationRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_requests_get**
> MediationList mediation_requests_get()

Query mediation requests, returns list of all mediation records

### Example

```python
import time
import acapy_client
from acapy_client.api import mediation_api
from acapy_client.model.mediation_list import MediationList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mediation_api.MediationApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier (optional) (optional)
    mediator_terms = [
        "mediator_terms_example",
    ] # [str] | List of mediator rules for recipient (optional)
    recipient_terms = [
        "recipient_terms_example",
    ] # [str] | List of recipient rules for mediation (optional)
    state = "request" # str | Mediation state (optional) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Query mediation requests, returns list of all mediation records
        api_response = api_instance.mediation_requests_get(conn_id=conn_id, mediator_terms=mediator_terms, recipient_terms=recipient_terms, state=state)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling MediationApi->mediation_requests_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier (optional) | [optional]
 **mediator_terms** | **[str]**| List of mediator rules for recipient | [optional]
 **recipient_terms** | **[str]**| List of recipient rules for mediation | [optional]
 **state** | **str**| Mediation state (optional) | [optional]

### Return type

[**MediationList**](MediationList.md)

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

# **mediation_requests_mediation_id_delete**
> MediationRecord mediation_requests_mediation_id_delete(mediation_id)

Delete mediation request by ID

### Example

```python
import time
import acapy_client
from acapy_client.api import mediation_api
from acapy_client.model.mediation_record import MediationRecord
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mediation_api.MediationApi(api_client)
    mediation_id = "mediation_id_example" # str | Mediation record identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete mediation request by ID
        api_response = api_instance.mediation_requests_mediation_id_delete(mediation_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling MediationApi->mediation_requests_mediation_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_id** | **str**| Mediation record identifier |

### Return type

[**MediationRecord**](MediationRecord.md)

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

# **mediation_requests_mediation_id_deny_post**
> MediationDeny mediation_requests_mediation_id_deny_post(mediation_id)

Deny a stored mediation request

### Example

```python
import time
import acapy_client
from acapy_client.api import mediation_api
from acapy_client.model.mediation_deny import MediationDeny
from acapy_client.model.admin_mediation_deny import AdminMediationDeny
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mediation_api.MediationApi(api_client)
    mediation_id = "mediation_id_example" # str | Mediation record identifier
    body = AdminMediationDeny(
        mediator_terms=[
            "mediator_terms_example",
        ],
        recipient_terms=[
            "recipient_terms_example",
        ],
    ) # AdminMediationDeny |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deny a stored mediation request
        api_response = api_instance.mediation_requests_mediation_id_deny_post(mediation_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling MediationApi->mediation_requests_mediation_id_deny_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deny a stored mediation request
        api_response = api_instance.mediation_requests_mediation_id_deny_post(mediation_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling MediationApi->mediation_requests_mediation_id_deny_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_id** | **str**| Mediation record identifier |
 **body** | [**AdminMediationDeny**](AdminMediationDeny.md)|  | [optional]

### Return type

[**MediationDeny**](MediationDeny.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mediation_requests_mediation_id_get**
> MediationRecord mediation_requests_mediation_id_get(mediation_id)

Retrieve mediation request record

### Example

```python
import time
import acapy_client
from acapy_client.api import mediation_api
from acapy_client.model.mediation_record import MediationRecord
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mediation_api.MediationApi(api_client)
    mediation_id = "mediation_id_example" # str | Mediation record identifier

    # example passing only required values which don't have defaults set
    try:
        # Retrieve mediation request record
        api_response = api_instance.mediation_requests_mediation_id_get(mediation_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling MediationApi->mediation_requests_mediation_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_id** | **str**| Mediation record identifier |

### Return type

[**MediationRecord**](MediationRecord.md)

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

# **mediation_requests_mediation_id_grant_post**
> MediationGrant mediation_requests_mediation_id_grant_post(mediation_id)

Grant received mediation

### Example

```python
import time
import acapy_client
from acapy_client.api import mediation_api
from acapy_client.model.mediation_grant import MediationGrant
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mediation_api.MediationApi(api_client)
    mediation_id = "mediation_id_example" # str | Mediation record identifier

    # example passing only required values which don't have defaults set
    try:
        # Grant received mediation
        api_response = api_instance.mediation_requests_mediation_id_grant_post(mediation_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling MediationApi->mediation_requests_mediation_id_grant_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_id** | **str**| Mediation record identifier |

### Return type

[**MediationGrant**](MediationGrant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

