# acapy_client.TrustpingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_trust_ping**](TrustpingApi.md#send_trust_ping) | **POST** /connections/{conn_id}/send-ping | Send a trust ping to a connection


# **send_trust_ping**
> PingRequestResponse send_trust_ping(conn_id)

Send a trust ping to a connection

### Example

```python
import time
import acapy_client
from acapy_client.api import trustping_api
from acapy_client.model.ping_request import PingRequest
from acapy_client.model.ping_request_response import PingRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = trustping_api.TrustpingApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    body = PingRequest(
        comment="comment_example",
    ) # PingRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a trust ping to a connection
        api_response = api_instance.send_trust_ping(conn_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling TrustpingApi->send_trust_ping: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a trust ping to a connection
        api_response = api_instance.send_trust_ping(conn_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling TrustpingApi->send_trust_ping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **body** | [**PingRequest**](PingRequest.md)|  | [optional]

### Return type

[**PingRequestResponse**](PingRequestResponse.md)

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

