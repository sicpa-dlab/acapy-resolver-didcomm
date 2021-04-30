# acapy_client.CredentialsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credential_credential_id_delete**](CredentialsApi.md#credential_credential_id_delete) | **DELETE** /credential/{credential_id} | Remove credential from wallet by id
[**credential_credential_id_get**](CredentialsApi.md#credential_credential_id_get) | **GET** /credential/{credential_id} | Fetch credential from wallet by id
[**credential_mime_types_credential_id_get**](CredentialsApi.md#credential_mime_types_credential_id_get) | **GET** /credential/mime-types/{credential_id} | Get attribute MIME types from wallet
[**credential_revoked_credential_id_get**](CredentialsApi.md#credential_revoked_credential_id_get) | **GET** /credential/revoked/{credential_id} | Query credential revocation status by id
[**credential_w3c_credential_id_delete**](CredentialsApi.md#credential_w3c_credential_id_delete) | **DELETE** /credential/w3c/{credential_id} | Remove W3C credential from wallet by id
[**credential_w3c_credential_id_get**](CredentialsApi.md#credential_w3c_credential_id_get) | **GET** /credential/w3c/{credential_id} | Fetch W3C credential from wallet by id
[**credentials_get**](CredentialsApi.md#credentials_get) | **GET** /credentials | Fetch credentials from wallet
[**credentials_w3c_post**](CredentialsApi.md#credentials_w3c_post) | **POST** /credentials/w3c | Fetch W3C credentials from wallet


# **credential_credential_id_delete**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} credential_credential_id_delete(credential_id)

Remove credential from wallet by id

### Example

```python
import time
import acapy_client
from acapy_client.api import credentials_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = credentials_api.CredentialsApi(api_client)
    credential_id = "credential_id_example" # str | Credential identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove credential from wallet by id
        api_response = api_instance.credential_credential_id_delete(credential_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling CredentialsApi->credential_credential_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**| Credential identifier |

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

# **credential_credential_id_get**
> CredBrief credential_credential_id_get(credential_id)

Fetch credential from wallet by id

### Example

```python
import time
import acapy_client
from acapy_client.api import credentials_api
from acapy_client.model.cred_brief import CredBrief
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = credentials_api.CredentialsApi(api_client)
    credential_id = "credential_id_example" # str | Credential identifier

    # example passing only required values which don't have defaults set
    try:
        # Fetch credential from wallet by id
        api_response = api_instance.credential_credential_id_get(credential_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling CredentialsApi->credential_credential_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**| Credential identifier |

### Return type

[**CredBrief**](CredBrief.md)

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

# **credential_mime_types_credential_id_get**
> AttributeMimeTypesResult credential_mime_types_credential_id_get(credential_id)

Get attribute MIME types from wallet

### Example

```python
import time
import acapy_client
from acapy_client.api import credentials_api
from acapy_client.model.attribute_mime_types_result import AttributeMimeTypesResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = credentials_api.CredentialsApi(api_client)
    credential_id = "credential_id_example" # str | Credential identifier

    # example passing only required values which don't have defaults set
    try:
        # Get attribute MIME types from wallet
        api_response = api_instance.credential_mime_types_credential_id_get(credential_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling CredentialsApi->credential_mime_types_credential_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**| Credential identifier |

### Return type

[**AttributeMimeTypesResult**](AttributeMimeTypesResult.md)

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

# **credential_revoked_credential_id_get**
> CredRevokedResult credential_revoked_credential_id_get(credential_id)

Query credential revocation status by id

### Example

```python
import time
import acapy_client
from acapy_client.api import credentials_api
from acapy_client.model.cred_revoked_result import CredRevokedResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = credentials_api.CredentialsApi(api_client)
    credential_id = "credential_id_example" # str | Credential identifier
    _from = "from_example" # str | Earliest epoch of revocation status interval of interest (optional)
    to = "to_example" # str | Latest epoch of revocation status interval of interest (optional)

    # example passing only required values which don't have defaults set
    try:
        # Query credential revocation status by id
        api_response = api_instance.credential_revoked_credential_id_get(credential_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling CredentialsApi->credential_revoked_credential_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Query credential revocation status by id
        api_response = api_instance.credential_revoked_credential_id_get(credential_id, _from=_from, to=to)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling CredentialsApi->credential_revoked_credential_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**| Credential identifier |
 **_from** | **str**| Earliest epoch of revocation status interval of interest | [optional]
 **to** | **str**| Latest epoch of revocation status interval of interest | [optional]

### Return type

[**CredRevokedResult**](CredRevokedResult.md)

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

# **credential_w3c_credential_id_delete**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} credential_w3c_credential_id_delete(credential_id)

Remove W3C credential from wallet by id

### Example

```python
import time
import acapy_client
from acapy_client.api import credentials_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = credentials_api.CredentialsApi(api_client)
    credential_id = "credential_id_example" # str | Credential identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove W3C credential from wallet by id
        api_response = api_instance.credential_w3c_credential_id_delete(credential_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling CredentialsApi->credential_w3c_credential_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**| Credential identifier |

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

# **credential_w3c_credential_id_get**
> VCRecord credential_w3c_credential_id_get(credential_id)

Fetch W3C credential from wallet by id

### Example

```python
import time
import acapy_client
from acapy_client.api import credentials_api
from acapy_client.model.vc_record import VCRecord
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = credentials_api.CredentialsApi(api_client)
    credential_id = "credential_id_example" # str | Credential identifier

    # example passing only required values which don't have defaults set
    try:
        # Fetch W3C credential from wallet by id
        api_response = api_instance.credential_w3c_credential_id_get(credential_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling CredentialsApi->credential_w3c_credential_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**| Credential identifier |

### Return type

[**VCRecord**](VCRecord.md)

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

# **credentials_get**
> CredBriefList credentials_get()

Fetch credentials from wallet

### Example

```python
import time
import acapy_client
from acapy_client.api import credentials_api
from acapy_client.model.cred_brief_list import CredBriefList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = credentials_api.CredentialsApi(api_client)
    count = "count_example" # str | Maximum number to retrieve (optional)
    start = "start_example" # str | Start index (optional)
    wql = "wql_example" # str | (JSON) WQL query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch credentials from wallet
        api_response = api_instance.credentials_get(count=count, start=start, wql=wql)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling CredentialsApi->credentials_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **str**| Maximum number to retrieve | [optional]
 **start** | **str**| Start index | [optional]
 **wql** | **str**| (JSON) WQL query | [optional]

### Return type

[**CredBriefList**](CredBriefList.md)

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

# **credentials_w3c_post**
> VCRecordList credentials_w3c_post()

Fetch W3C credentials from wallet

### Example

```python
import time
import acapy_client
from acapy_client.api import credentials_api
from acapy_client.model.vc_record_list import VCRecordList
from acapy_client.model.w3_c_credentials_list_request import W3CCredentialsListRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = credentials_api.CredentialsApi(api_client)
    count = "count_example" # str | Maximum number to retrieve (optional)
    start = "start_example" # str | Start index (optional)
    wql = "wql_example" # str | (JSON) WQL query (optional)
    body = W3CCredentialsListRequest(
        contexts=[
            "contexts_example",
        ],
        given_id="given_id_example",
        issuer_id="issuer_id_example",
        max_results=1,
        proof_types=[
            "proof_types_example",
        ],
        schema_ids=[
            "schema_ids_example",
        ],
        subject_ids=[
            "subject_ids_example",
        ],
        tag_query={
            "key": "key_example",
        },
        types=[
            "types_example",
        ],
    ) # W3CCredentialsListRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch W3C credentials from wallet
        api_response = api_instance.credentials_w3c_post(count=count, start=start, wql=wql, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling CredentialsApi->credentials_w3c_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **str**| Maximum number to retrieve | [optional]
 **start** | **str**| Start index | [optional]
 **wql** | **str**| (JSON) WQL query | [optional]
 **body** | [**W3CCredentialsListRequest**](W3CCredentialsListRequest.md)|  | [optional]

### Return type

[**VCRecordList**](VCRecordList.md)

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

