# acapy_client.LedgerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ledger_did_endpoint_get**](LedgerApi.md#ledger_did_endpoint_get) | **GET** /ledger/did-endpoint | Get the endpoint for a DID from the ledger.
[**ledger_did_verkey_get**](LedgerApi.md#ledger_did_verkey_get) | **GET** /ledger/did-verkey | Get the verkey for a DID from the ledger.
[**ledger_get_nym_role_get**](LedgerApi.md#ledger_get_nym_role_get) | **GET** /ledger/get-nym-role | Get the role from the NYM registration of a public DID.
[**ledger_register_nym_post**](LedgerApi.md#ledger_register_nym_post) | **POST** /ledger/register-nym | Send a NYM registration to the ledger.
[**ledger_rotate_public_did_keypair_patch**](LedgerApi.md#ledger_rotate_public_did_keypair_patch) | **PATCH** /ledger/rotate-public-did-keypair | Rotate key pair for public DID.
[**ledger_taa_accept_post**](LedgerApi.md#ledger_taa_accept_post) | **POST** /ledger/taa/accept | Accept the transaction author agreement
[**ledger_taa_get**](LedgerApi.md#ledger_taa_get) | **GET** /ledger/taa | Fetch the current transaction author agreement, if any


# **ledger_did_endpoint_get**
> GetDIDEndpointResponse ledger_did_endpoint_get(did)

Get the endpoint for a DID from the ledger.

### Example

```python
import time
import acapy_client
from acapy_client.api import ledger_api
from acapy_client.model.get_did_endpoint_response import GetDIDEndpointResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)
    did = "did_example" # str | DID of interest
    endpoint_type = "Endpoint" # str | Endpoint type of interest (default 'Endpoint') (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the endpoint for a DID from the ledger.
        api_response = api_instance.ledger_did_endpoint_get(did)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling LedgerApi->ledger_did_endpoint_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the endpoint for a DID from the ledger.
        api_response = api_instance.ledger_did_endpoint_get(did, endpoint_type=endpoint_type)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling LedgerApi->ledger_did_endpoint_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID of interest |
 **endpoint_type** | **str**| Endpoint type of interest (default &#39;Endpoint&#39;) | [optional]

### Return type

[**GetDIDEndpointResponse**](GetDIDEndpointResponse.md)

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

# **ledger_did_verkey_get**
> GetDIDVerkeyResponse ledger_did_verkey_get(did)

Get the verkey for a DID from the ledger.

### Example

```python
import time
import acapy_client
from acapy_client.api import ledger_api
from acapy_client.model.get_did_verkey_response import GetDIDVerkeyResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)
    did = "did_example" # str | DID of interest

    # example passing only required values which don't have defaults set
    try:
        # Get the verkey for a DID from the ledger.
        api_response = api_instance.ledger_did_verkey_get(did)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling LedgerApi->ledger_did_verkey_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID of interest |

### Return type

[**GetDIDVerkeyResponse**](GetDIDVerkeyResponse.md)

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

# **ledger_get_nym_role_get**
> GetNymRoleResponse ledger_get_nym_role_get(did)

Get the role from the NYM registration of a public DID.

### Example

```python
import time
import acapy_client
from acapy_client.api import ledger_api
from acapy_client.model.get_nym_role_response import GetNymRoleResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)
    did = "did_example" # str | DID of interest

    # example passing only required values which don't have defaults set
    try:
        # Get the role from the NYM registration of a public DID.
        api_response = api_instance.ledger_get_nym_role_get(did)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling LedgerApi->ledger_get_nym_role_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID of interest |

### Return type

[**GetNymRoleResponse**](GetNymRoleResponse.md)

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

# **ledger_register_nym_post**
> RegisterLedgerNymResponse ledger_register_nym_post(did, verkey)

Send a NYM registration to the ledger.

### Example

```python
import time
import acapy_client
from acapy_client.api import ledger_api
from acapy_client.model.register_ledger_nym_response import RegisterLedgerNymResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)
    did = "did_example" # str | DID to register
    verkey = "verkey_example" # str | Verification key
    alias = "alias_example" # str | Alias (optional)
    role = "STEWARD" # str | Role (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a NYM registration to the ledger.
        api_response = api_instance.ledger_register_nym_post(did, verkey)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling LedgerApi->ledger_register_nym_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a NYM registration to the ledger.
        api_response = api_instance.ledger_register_nym_post(did, verkey, alias=alias, role=role)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling LedgerApi->ledger_register_nym_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID to register |
 **verkey** | **str**| Verification key |
 **alias** | **str**| Alias | [optional]
 **role** | **str**| Role | [optional]

### Return type

[**RegisterLedgerNymResponse**](RegisterLedgerNymResponse.md)

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

# **ledger_rotate_public_did_keypair_patch**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} ledger_rotate_public_did_keypair_patch()

Rotate key pair for public DID.

### Example

```python
import time
import acapy_client
from acapy_client.api import ledger_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Rotate key pair for public DID.
        api_response = api_instance.ledger_rotate_public_did_keypair_patch()
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling LedgerApi->ledger_rotate_public_did_keypair_patch: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **ledger_taa_accept_post**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} ledger_taa_accept_post()

Accept the transaction author agreement

### Example

```python
import time
import acapy_client
from acapy_client.api import ledger_api
from acapy_client.model.taa_accept import TAAAccept
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)
    body = TAAAccept(
        mechanism="mechanism_example",
        text="text_example",
        version="version_example",
    ) # TAAAccept |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Accept the transaction author agreement
        api_response = api_instance.ledger_taa_accept_post(body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling LedgerApi->ledger_taa_accept_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TAAAccept**](TAAAccept.md)|  | [optional]

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

# **ledger_taa_get**
> TAAResult ledger_taa_get()

Fetch the current transaction author agreement, if any

### Example

```python
import time
import acapy_client
from acapy_client.api import ledger_api
from acapy_client.model.taa_result import TAAResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch the current transaction author agreement, if any
        api_response = api_instance.ledger_taa_get()
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling LedgerApi->ledger_taa_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TAAResult**](TAAResult.md)

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

