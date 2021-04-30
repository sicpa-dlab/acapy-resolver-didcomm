# acapy_client.IntroductionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**start_introduction**](IntroductionApi.md#start_introduction) | **POST** /connections/{conn_id}/start-introduction | Start an introduction between two connections


# **start_introduction**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} start_introduction(conn_id, target_connection_id)

Start an introduction between two connections

### Example

```python
import time
import acapy_client
from acapy_client.api import introduction_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = introduction_api.IntroductionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    target_connection_id = "target_connection_id_example" # str | Target connection identifier
    message = "message_example" # str | Message (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start an introduction between two connections
        api_response = api_instance.start_introduction(conn_id, target_connection_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IntroductionApi->start_introduction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start an introduction between two connections
        api_response = api_instance.start_introduction(conn_id, target_connection_id, message=message)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IntroductionApi->start_introduction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **target_connection_id** | **str**| Target connection identifier |
 **message** | **str**| Message | [optional]

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

