# acapy_client.ResolverApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resolve**](ResolverApi.md#resolve) | **GET** /resolver/resolve/{did} | Retrieve doc for requested did


# **resolve**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} resolve(did)

Retrieve doc for requested did

### Example

```python
import time
import acapy_client
from acapy_client.api import resolver_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = resolver_api.ResolverApi(api_client)
    did = "did_example" # str | decentralize identifier(DID)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve doc for requested did
        api_response = api_instance.resolve(did)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling ResolverApi->resolve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| decentralize identifier(DID) |

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

