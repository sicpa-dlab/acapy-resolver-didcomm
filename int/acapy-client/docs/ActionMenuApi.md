# acapy_client.ActionMenuApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_menu_conn_id_close_post**](ActionMenuApi.md#action_menu_conn_id_close_post) | **POST** /action-menu/{conn_id}/close | Close the active menu associated with a connection
[**action_menu_conn_id_fetch_post**](ActionMenuApi.md#action_menu_conn_id_fetch_post) | **POST** /action-menu/{conn_id}/fetch | Fetch the active menu
[**action_menu_conn_id_perform_post**](ActionMenuApi.md#action_menu_conn_id_perform_post) | **POST** /action-menu/{conn_id}/perform | Perform an action associated with the active menu
[**action_menu_conn_id_request_post**](ActionMenuApi.md#action_menu_conn_id_request_post) | **POST** /action-menu/{conn_id}/request | Request the active menu
[**action_menu_conn_id_send_menu_post**](ActionMenuApi.md#action_menu_conn_id_send_menu_post) | **POST** /action-menu/{conn_id}/send-menu | Send an action menu to a connection


# **action_menu_conn_id_close_post**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} action_menu_conn_id_close_post(conn_id)

Close the active menu associated with a connection

### Example

```python
import time
import acapy_client
from acapy_client.api import action_menu_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = action_menu_api.ActionMenuApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier

    # example passing only required values which don't have defaults set
    try:
        # Close the active menu associated with a connection
        api_response = api_instance.action_menu_conn_id_close_post(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ActionMenuApi->action_menu_conn_id_close_post: %s\n" % e)
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

# **action_menu_conn_id_fetch_post**
> ActionMenuFetchResult action_menu_conn_id_fetch_post(conn_id)

Fetch the active menu

### Example

```python
import time
import acapy_client
from acapy_client.api import action_menu_api
from acapy_client.model.action_menu_fetch_result import ActionMenuFetchResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = action_menu_api.ActionMenuApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier

    # example passing only required values which don't have defaults set
    try:
        # Fetch the active menu
        api_response = api_instance.action_menu_conn_id_fetch_post(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ActionMenuApi->action_menu_conn_id_fetch_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |

### Return type

[**ActionMenuFetchResult**](ActionMenuFetchResult.md)

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

# **action_menu_conn_id_perform_post**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} action_menu_conn_id_perform_post(conn_id)

Perform an action associated with the active menu

### Example

```python
import time
import acapy_client
from acapy_client.api import action_menu_api
from acapy_client.model.perform_request import PerformRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = action_menu_api.ActionMenuApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    body = PerformRequest(
        name="name_example",
        params={
            "key": "key_example",
        },
    ) # PerformRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Perform an action associated with the active menu
        api_response = api_instance.action_menu_conn_id_perform_post(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ActionMenuApi->action_menu_conn_id_perform_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Perform an action associated with the active menu
        api_response = api_instance.action_menu_conn_id_perform_post(conn_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ActionMenuApi->action_menu_conn_id_perform_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **body** | [**PerformRequest**](PerformRequest.md)|  | [optional]

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

# **action_menu_conn_id_request_post**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} action_menu_conn_id_request_post(conn_id)

Request the active menu

### Example

```python
import time
import acapy_client
from acapy_client.api import action_menu_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = action_menu_api.ActionMenuApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier

    # example passing only required values which don't have defaults set
    try:
        # Request the active menu
        api_response = api_instance.action_menu_conn_id_request_post(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ActionMenuApi->action_menu_conn_id_request_post: %s\n" % e)
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

# **action_menu_conn_id_send_menu_post**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} action_menu_conn_id_send_menu_post(conn_id)

Send an action menu to a connection

### Example

```python
import time
import acapy_client
from acapy_client.api import action_menu_api
from acapy_client.model.send_menu import SendMenu
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = action_menu_api.ActionMenuApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    body = SendMenu(
        menu={},
    ) # SendMenu |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an action menu to a connection
        api_response = api_instance.action_menu_conn_id_send_menu_post(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ActionMenuApi->action_menu_conn_id_send_menu_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an action menu to a connection
        api_response = api_instance.action_menu_conn_id_send_menu_post(conn_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ActionMenuApi->action_menu_conn_id_send_menu_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **body** | [**SendMenu**](SendMenu.md)|  | [optional]

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

