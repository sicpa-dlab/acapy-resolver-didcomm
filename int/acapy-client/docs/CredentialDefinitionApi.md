# acapy_client.CredentialDefinitionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credential_definitions_created_get**](CredentialDefinitionApi.md#credential_definitions_created_get) | **GET** /credential-definitions/created | Search for matching credential definitions that agent originated
[**credential_definitions_cred_def_id_get**](CredentialDefinitionApi.md#credential_definitions_cred_def_id_get) | **GET** /credential-definitions/{cred_def_id} | Gets a credential definition from the ledger
[**credential_definitions_post**](CredentialDefinitionApi.md#credential_definitions_post) | **POST** /credential-definitions | Sends a credential definition to the ledger


# **credential_definitions_created_get**
> CredentialDefinitionsCreatedResult credential_definitions_created_get()

Search for matching credential definitions that agent originated

### Example

```python
import time
import acapy_client
from acapy_client.api import credential_definition_api
from acapy_client.model.credential_definitions_created_result import CredentialDefinitionsCreatedResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = credential_definition_api.CredentialDefinitionApi(api_client)
    cred_def_id = "cred_def_id_example" # str | Credential definition id (optional)
    issuer_did = "issuer_did_example" # str | Issuer DID (optional)
    schema_id = "schema_id_example" # str | Schema identifier (optional)
    schema_issuer_did = "schema_issuer_did_example" # str | Schema issuer DID (optional)
    schema_name = "schema_name_example" # str | Schema name (optional)
    schema_version = "schema_version_example" # str | Schema version (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for matching credential definitions that agent originated
        api_response = api_instance.credential_definitions_created_get(cred_def_id=cred_def_id, issuer_did=issuer_did, schema_id=schema_id, schema_issuer_did=schema_issuer_did, schema_name=schema_name, schema_version=schema_version)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling CredentialDefinitionApi->credential_definitions_created_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| Credential definition id | [optional]
 **issuer_did** | **str**| Issuer DID | [optional]
 **schema_id** | **str**| Schema identifier | [optional]
 **schema_issuer_did** | **str**| Schema issuer DID | [optional]
 **schema_name** | **str**| Schema name | [optional]
 **schema_version** | **str**| Schema version | [optional]

### Return type

[**CredentialDefinitionsCreatedResult**](CredentialDefinitionsCreatedResult.md)

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

# **credential_definitions_cred_def_id_get**
> CredentialDefinitionGetResult credential_definitions_cred_def_id_get(cred_def_id)

Gets a credential definition from the ledger

### Example

```python
import time
import acapy_client
from acapy_client.api import credential_definition_api
from acapy_client.model.credential_definition_get_result import CredentialDefinitionGetResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = credential_definition_api.CredentialDefinitionApi(api_client)
    cred_def_id = "cred_def_id_example" # str | Credential definition identifier

    # example passing only required values which don't have defaults set
    try:
        # Gets a credential definition from the ledger
        api_response = api_instance.credential_definitions_cred_def_id_get(cred_def_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling CredentialDefinitionApi->credential_definitions_cred_def_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| Credential definition identifier |

### Return type

[**CredentialDefinitionGetResult**](CredentialDefinitionGetResult.md)

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

# **credential_definitions_post**
> TxnOrCredentialDefinitionSendResult credential_definitions_post()

Sends a credential definition to the ledger

### Example

```python
import time
import acapy_client
from acapy_client.api import credential_definition_api
from acapy_client.model.txn_or_credential_definition_send_result import TxnOrCredentialDefinitionSendResult
from acapy_client.model.credential_definition_send_request import CredentialDefinitionSendRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = credential_definition_api.CredentialDefinitionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier (optional)
    create_transaction_for_endorser = True # bool | Create Transaction For Endorser's signature (optional)
    body = CredentialDefinitionSendRequest(
        revocation_registry_size=4,
        schema_id="schema_id_example",
        support_revocation=True,
        tag="tag_example",
    ) # CredentialDefinitionSendRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sends a credential definition to the ledger
        api_response = api_instance.credential_definitions_post(conn_id=conn_id, create_transaction_for_endorser=create_transaction_for_endorser, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling CredentialDefinitionApi->credential_definitions_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | [optional]
 **create_transaction_for_endorser** | **bool**| Create Transaction For Endorser&#39;s signature | [optional]
 **body** | [**CredentialDefinitionSendRequest**](CredentialDefinitionSendRequest.md)|  | [optional]

### Return type

[**TxnOrCredentialDefinitionSendResult**](TxnOrCredentialDefinitionSendResult.md)

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

