# acapy_client.RevocationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**revocation_active_registry_cred_def_id_get**](RevocationApi.md#revocation_active_registry_cred_def_id_get) | **GET** /revocation/active-registry/{cred_def_id} | Get current active revocation registry by credential definition id
[**revocation_clear_pending_revocations_post**](RevocationApi.md#revocation_clear_pending_revocations_post) | **POST** /revocation/clear-pending-revocations | Clear pending revocations
[**revocation_create_registry_post**](RevocationApi.md#revocation_create_registry_post) | **POST** /revocation/create-registry | Creates a new revocation registry
[**revocation_credential_record_get**](RevocationApi.md#revocation_credential_record_get) | **GET** /revocation/credential-record | Get credential revocation status
[**revocation_publish_revocations_post**](RevocationApi.md#revocation_publish_revocations_post) | **POST** /revocation/publish-revocations | Publish pending revocations to ledger
[**revocation_registries_created_get**](RevocationApi.md#revocation_registries_created_get) | **GET** /revocation/registries/created | Search for matching revocation registries that current agent created
[**revocation_registry_rev_reg_id_definition_post**](RevocationApi.md#revocation_registry_rev_reg_id_definition_post) | **POST** /revocation/registry/{rev_reg_id}/definition | Send revocation registry definition to ledger
[**revocation_registry_rev_reg_id_entry_post**](RevocationApi.md#revocation_registry_rev_reg_id_entry_post) | **POST** /revocation/registry/{rev_reg_id}/entry | Send revocation registry entry to ledger
[**revocation_registry_rev_reg_id_get**](RevocationApi.md#revocation_registry_rev_reg_id_get) | **GET** /revocation/registry/{rev_reg_id} | Get revocation registry by revocation registry id
[**revocation_registry_rev_reg_id_issued_get**](RevocationApi.md#revocation_registry_rev_reg_id_issued_get) | **GET** /revocation/registry/{rev_reg_id}/issued | Get number of credentials issued against revocation registry
[**revocation_registry_rev_reg_id_patch**](RevocationApi.md#revocation_registry_rev_reg_id_patch) | **PATCH** /revocation/registry/{rev_reg_id} | Update revocation registry with new public URI to its tails file
[**revocation_registry_rev_reg_id_set_state_patch**](RevocationApi.md#revocation_registry_rev_reg_id_set_state_patch) | **PATCH** /revocation/registry/{rev_reg_id}/set-state | Set revocation registry state manually
[**revocation_registry_rev_reg_id_tails_file_get**](RevocationApi.md#revocation_registry_rev_reg_id_tails_file_get) | **GET** /revocation/registry/{rev_reg_id}/tails-file | Download tails file
[**revocation_registry_rev_reg_id_tails_file_put**](RevocationApi.md#revocation_registry_rev_reg_id_tails_file_put) | **PUT** /revocation/registry/{rev_reg_id}/tails-file | Upload local tails file to server
[**revocation_revoke_post**](RevocationApi.md#revocation_revoke_post) | **POST** /revocation/revoke | Revoke an issued credential


# **revocation_active_registry_cred_def_id_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} revocation_active_registry_cred_def_id_get(cred_def_id)

Get current active revocation registry by credential definition id

### Example

```python
import time
import acapy_client
from acapy_client.api import revocation_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revocation_api.RevocationApi(api_client)
    cred_def_id = "cred_def_id_example" # str | Credential definition identifier

    # example passing only required values which don't have defaults set
    try:
        # Get current active revocation registry by credential definition id
        api_response = api_instance.revocation_active_registry_cred_def_id_get(cred_def_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling RevocationApi->revocation_active_registry_cred_def_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| Credential definition identifier |

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

# **revocation_clear_pending_revocations_post**
> PublishRevocations revocation_clear_pending_revocations_post()

Clear pending revocations

### Example

```python
import time
import acapy_client
from acapy_client.api import revocation_api
from acapy_client.model.clear_pending_revocations_request import ClearPendingRevocationsRequest
from acapy_client.model.publish_revocations import PublishRevocations
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revocation_api.RevocationApi(api_client)
    body = ClearPendingRevocationsRequest(
        purge={
            "key": [
                "key_example",
            ],
        },
    ) # ClearPendingRevocationsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Clear pending revocations
        api_response = api_instance.revocation_clear_pending_revocations_post(body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling RevocationApi->revocation_clear_pending_revocations_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClearPendingRevocationsRequest**](ClearPendingRevocationsRequest.md)|  | [optional]

### Return type

[**PublishRevocations**](PublishRevocations.md)

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

# **revocation_create_registry_post**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} revocation_create_registry_post()

Creates a new revocation registry

### Example

```python
import time
import acapy_client
from acapy_client.api import revocation_api
from acapy_client.model.rev_reg_create_request import RevRegCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revocation_api.RevocationApi(api_client)
    body = RevRegCreateRequest(
        credential_definition_id="credential_definition_id_example",
        max_cred_num=4,
    ) # RevRegCreateRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a new revocation registry
        api_response = api_instance.revocation_create_registry_post(body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling RevocationApi->revocation_create_registry_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RevRegCreateRequest**](RevRegCreateRequest.md)|  | [optional]

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

# **revocation_credential_record_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} revocation_credential_record_get()

Get credential revocation status

### Example

```python
import time
import acapy_client
from acapy_client.api import revocation_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revocation_api.RevocationApi(api_client)
    cred_ex_id = "cred_ex_id_example" # str | Credential exchange identifier (optional)
    cred_rev_id = "cred_rev_id_example" # str | Credential revocation identifier (optional)
    rev_reg_id = "rev_reg_id_example" # str | Revocation registry identifier (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get credential revocation status
        api_response = api_instance.revocation_credential_record_get(cred_ex_id=cred_ex_id, cred_rev_id=cred_rev_id, rev_reg_id=rev_reg_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling RevocationApi->revocation_credential_record_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier | [optional]
 **cred_rev_id** | **str**| Credential revocation identifier | [optional]
 **rev_reg_id** | **str**| Revocation registry identifier | [optional]

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

# **revocation_publish_revocations_post**
> PublishRevocations revocation_publish_revocations_post()

Publish pending revocations to ledger

### Example

```python
import time
import acapy_client
from acapy_client.api import revocation_api
from acapy_client.model.publish_revocations import PublishRevocations
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revocation_api.RevocationApi(api_client)
    body = PublishRevocations(
        rrid2crid={
            "key": [
                "key_example",
            ],
        },
    ) # PublishRevocations |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Publish pending revocations to ledger
        api_response = api_instance.revocation_publish_revocations_post(body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling RevocationApi->revocation_publish_revocations_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublishRevocations**](PublishRevocations.md)|  | [optional]

### Return type

[**PublishRevocations**](PublishRevocations.md)

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

# **revocation_registries_created_get**
> RevRegsCreated revocation_registries_created_get()

Search for matching revocation registries that current agent created

### Example

```python
import time
import acapy_client
from acapy_client.api import revocation_api
from acapy_client.model.rev_regs_created import RevRegsCreated
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revocation_api.RevocationApi(api_client)
    cred_def_id = "cred_def_id_example" # str | Credential definition identifier (optional)
    state = "init" # str | Revocation registry state (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for matching revocation registries that current agent created
        api_response = api_instance.revocation_registries_created_get(cred_def_id=cred_def_id, state=state)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling RevocationApi->revocation_registries_created_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| Credential definition identifier | [optional]
 **state** | **str**| Revocation registry state | [optional]

### Return type

[**RevRegsCreated**](RevRegsCreated.md)

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

# **revocation_registry_rev_reg_id_definition_post**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} revocation_registry_rev_reg_id_definition_post(rev_reg_id)

Send revocation registry definition to ledger

### Example

```python
import time
import acapy_client
from acapy_client.api import revocation_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revocation_api.RevocationApi(api_client)
    rev_reg_id = "rev_reg_id_example" # str | Revocation Registry identifier

    # example passing only required values which don't have defaults set
    try:
        # Send revocation registry definition to ledger
        api_response = api_instance.revocation_registry_rev_reg_id_definition_post(rev_reg_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_definition_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rev_reg_id** | **str**| Revocation Registry identifier |

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

# **revocation_registry_rev_reg_id_entry_post**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} revocation_registry_rev_reg_id_entry_post(rev_reg_id)

Send revocation registry entry to ledger

### Example

```python
import time
import acapy_client
from acapy_client.api import revocation_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revocation_api.RevocationApi(api_client)
    rev_reg_id = "rev_reg_id_example" # str | Revocation Registry identifier

    # example passing only required values which don't have defaults set
    try:
        # Send revocation registry entry to ledger
        api_response = api_instance.revocation_registry_rev_reg_id_entry_post(rev_reg_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_entry_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rev_reg_id** | **str**| Revocation Registry identifier |

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

# **revocation_registry_rev_reg_id_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} revocation_registry_rev_reg_id_get(rev_reg_id)

Get revocation registry by revocation registry id

### Example

```python
import time
import acapy_client
from acapy_client.api import revocation_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revocation_api.RevocationApi(api_client)
    rev_reg_id = "rev_reg_id_example" # str | Revocation Registry identifier

    # example passing only required values which don't have defaults set
    try:
        # Get revocation registry by revocation registry id
        api_response = api_instance.revocation_registry_rev_reg_id_get(rev_reg_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rev_reg_id** | **str**| Revocation Registry identifier |

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

# **revocation_registry_rev_reg_id_issued_get**
> RevRegIssuedResult revocation_registry_rev_reg_id_issued_get(rev_reg_id)

Get number of credentials issued against revocation registry

### Example

```python
import time
import acapy_client
from acapy_client.api import revocation_api
from acapy_client.model.rev_reg_issued_result import RevRegIssuedResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revocation_api.RevocationApi(api_client)
    rev_reg_id = "rev_reg_id_example" # str | Revocation Registry identifier

    # example passing only required values which don't have defaults set
    try:
        # Get number of credentials issued against revocation registry
        api_response = api_instance.revocation_registry_rev_reg_id_issued_get(rev_reg_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_issued_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rev_reg_id** | **str**| Revocation Registry identifier |

### Return type

[**RevRegIssuedResult**](RevRegIssuedResult.md)

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

# **revocation_registry_rev_reg_id_patch**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} revocation_registry_rev_reg_id_patch(rev_reg_id)

Update revocation registry with new public URI to its tails file

### Example

```python
import time
import acapy_client
from acapy_client.api import revocation_api
from acapy_client.model.rev_reg_update_tails_file_uri import RevRegUpdateTailsFileUri
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revocation_api.RevocationApi(api_client)
    rev_reg_id = "rev_reg_id_example" # str | Revocation Registry identifier
    body = RevRegUpdateTailsFileUri(
        tails_public_uri="tails_public_uri_example",
    ) # RevRegUpdateTailsFileUri |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update revocation registry with new public URI to its tails file
        api_response = api_instance.revocation_registry_rev_reg_id_patch(rev_reg_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update revocation registry with new public URI to its tails file
        api_response = api_instance.revocation_registry_rev_reg_id_patch(rev_reg_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rev_reg_id** | **str**| Revocation Registry identifier |
 **body** | [**RevRegUpdateTailsFileUri**](RevRegUpdateTailsFileUri.md)|  | [optional]

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

# **revocation_registry_rev_reg_id_set_state_patch**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} revocation_registry_rev_reg_id_set_state_patch(rev_reg_id, state)

Set revocation registry state manually

### Example

```python
import time
import acapy_client
from acapy_client.api import revocation_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revocation_api.RevocationApi(api_client)
    rev_reg_id = "rev_reg_id_example" # str | Revocation Registry identifier
    state = "init" # str | Revocation registry state to set

    # example passing only required values which don't have defaults set
    try:
        # Set revocation registry state manually
        api_response = api_instance.revocation_registry_rev_reg_id_set_state_patch(rev_reg_id, state)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_set_state_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rev_reg_id** | **str**| Revocation Registry identifier |
 **state** | **str**| Revocation registry state to set |

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

# **revocation_registry_rev_reg_id_tails_file_get**
> file_type revocation_registry_rev_reg_id_tails_file_get(rev_reg_id)

Download tails file

### Example

```python
import time
import acapy_client
from acapy_client.api import revocation_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revocation_api.RevocationApi(api_client)
    rev_reg_id = "rev_reg_id_example" # str | Revocation Registry identifier

    # example passing only required values which don't have defaults set
    try:
        # Download tails file
        api_response = api_instance.revocation_registry_rev_reg_id_tails_file_get(rev_reg_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_tails_file_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rev_reg_id** | **str**| Revocation Registry identifier |

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tails file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revocation_registry_rev_reg_id_tails_file_put**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} revocation_registry_rev_reg_id_tails_file_put(rev_reg_id)

Upload local tails file to server

### Example

```python
import time
import acapy_client
from acapy_client.api import revocation_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revocation_api.RevocationApi(api_client)
    rev_reg_id = "rev_reg_id_example" # str | Revocation Registry identifier

    # example passing only required values which don't have defaults set
    try:
        # Upload local tails file to server
        api_response = api_instance.revocation_registry_rev_reg_id_tails_file_put(rev_reg_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling RevocationApi->revocation_registry_rev_reg_id_tails_file_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rev_reg_id** | **str**| Revocation Registry identifier |

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

# **revocation_revoke_post**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} revocation_revoke_post()

Revoke an issued credential

### Example

```python
import time
import acapy_client
from acapy_client.api import revocation_api
from acapy_client.model.revoke_request import RevokeRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revocation_api.RevocationApi(api_client)
    body = RevokeRequest(
        cred_ex_id="cred_ex_id_example",
        cred_rev_id="cred_rev_id_example",
        publish=True,
        rev_reg_id="rev_reg_id_example",
    ) # RevokeRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Revoke an issued credential
        api_response = api_instance.revocation_revoke_post(body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling RevocationApi->revocation_revoke_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RevokeRequest**](RevokeRequest.md)|  | [optional]

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

