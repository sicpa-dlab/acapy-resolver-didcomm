# acapy_client.JsonldApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jsonld_sign_post**](JsonldApi.md#jsonld_sign_post) | **POST** /jsonld/sign | Sign a JSON-LD structure and return it
[**jsonld_verify_post**](JsonldApi.md#jsonld_verify_post) | **POST** /jsonld/verify | Verify a JSON-LD structure.


# **jsonld_sign_post**
> SignResponse jsonld_sign_post()

Sign a JSON-LD structure and return it

### Example

```python
import time
import acapy_client
from acapy_client.api import jsonld_api
from acapy_client.model.sign_response import SignResponse
from acapy_client.model.sign_request import SignRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = jsonld_api.JsonldApi(api_client)
    body = SignRequest(
        doc=Generated(
            credential={},
            options=Generated(),
        ),
        verkey="verkey_example",
    ) # SignRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sign a JSON-LD structure and return it
        api_response = api_instance.jsonld_sign_post(body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling JsonldApi->jsonld_sign_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SignRequest**](SignRequest.md)|  | [optional]

### Return type

[**SignResponse**](SignResponse.md)

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

# **jsonld_verify_post**
> VerifyResponse jsonld_verify_post()

Verify a JSON-LD structure.

### Example

```python
import time
import acapy_client
from acapy_client.api import jsonld_api
from acapy_client.model.verify_request import VerifyRequest
from acapy_client.model.verify_response import VerifyResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = jsonld_api.JsonldApi(api_client)
    body = VerifyRequest(
        doc={},
        verkey="verkey_example",
    ) # VerifyRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Verify a JSON-LD structure.
        api_response = api_instance.jsonld_verify_post(body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling JsonldApi->jsonld_verify_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyRequest**](VerifyRequest.md)|  | [optional]

### Return type

[**VerifyResponse**](VerifyResponse.md)

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

