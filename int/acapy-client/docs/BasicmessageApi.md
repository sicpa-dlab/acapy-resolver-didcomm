# acapy_client.BasicmessageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_basic_message**](BasicmessageApi.md#send_basic_message) | **POST** /connections/{conn_id}/send-message | Send a basic message to a connection


# **send_basic_message**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} send_basic_message(conn_id)

Send a basic message to a connection

### Example

```python
import time
import acapy_client
from acapy_client.api import basicmessage_api
from acapy_client.model.send_message import SendMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = basicmessage_api.BasicmessageApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    body = SendMessage(
        content="content_example",
    ) # SendMessage |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a basic message to a connection
        api_response = api_instance.send_basic_message(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling BasicmessageApi->send_basic_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a basic message to a connection
        api_response = api_instance.send_basic_message(conn_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling BasicmessageApi->send_basic_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **body** | [**SendMessage**](SendMessage.md)|  | [optional]

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

