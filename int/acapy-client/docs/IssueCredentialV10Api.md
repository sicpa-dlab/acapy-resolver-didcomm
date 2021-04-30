# acapy_client.IssueCredentialV10Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**issue_credential_create_post**](IssueCredentialV10Api.md#issue_credential_create_post) | **POST** /issue-credential/create | Send holder a credential, automating entire flow
[**issue_credential_records_cred_ex_id_delete**](IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_delete) | **DELETE** /issue-credential/records/{cred_ex_id} | Remove an existing credential exchange record
[**issue_credential_records_cred_ex_id_get**](IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_get) | **GET** /issue-credential/records/{cred_ex_id} | Fetch a single credential exchange record
[**issue_credential_records_cred_ex_id_issue_post**](IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_issue_post) | **POST** /issue-credential/records/{cred_ex_id}/issue | Send holder a credential
[**issue_credential_records_cred_ex_id_problem_report_post**](IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_problem_report_post) | **POST** /issue-credential/records/{cred_ex_id}/problem-report | Send a problem report for credential exchange
[**issue_credential_records_cred_ex_id_send_offer_post**](IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_send_offer_post) | **POST** /issue-credential/records/{cred_ex_id}/send-offer | Send holder a credential offer in reference to a proposal with preview
[**issue_credential_records_cred_ex_id_send_request_post**](IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_send_request_post) | **POST** /issue-credential/records/{cred_ex_id}/send-request | Send issuer a credential request
[**issue_credential_records_cred_ex_id_store_post**](IssueCredentialV10Api.md#issue_credential_records_cred_ex_id_store_post) | **POST** /issue-credential/records/{cred_ex_id}/store | Store a received credential
[**issue_credential_records_get**](IssueCredentialV10Api.md#issue_credential_records_get) | **GET** /issue-credential/records | Fetch all credential exchange records
[**issue_credential_send_offer_post**](IssueCredentialV10Api.md#issue_credential_send_offer_post) | **POST** /issue-credential/send-offer | Send holder a credential offer, independent of any proposal
[**issue_credential_send_post**](IssueCredentialV10Api.md#issue_credential_send_post) | **POST** /issue-credential/send | Send holder a credential, automating entire flow
[**issue_credential_send_proposal_post**](IssueCredentialV10Api.md#issue_credential_send_proposal_post) | **POST** /issue-credential/send-proposal | Send issuer a credential proposal


# **issue_credential_create_post**
> V10CredentialExchange issue_credential_create_post()

Send holder a credential, automating entire flow

### Example

```python
import time
import acapy_client
from acapy_client.api import issue_credential_v1_0_api
from acapy_client.model.v10_credential_create import V10CredentialCreate
from acapy_client.model.v10_credential_exchange import V10CredentialExchange
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = issue_credential_v1_0_api.IssueCredentialV10Api(api_client)
    body = V10CredentialCreate(
        auto_remove=True,
        comment="comment_example",
        cred_def_id="cred_def_id_example",
        credential_proposal=CredentialPreview(
            type="type_example",
            attributes=[
                CredAttrSpec(
                    mime_type="mime_type_example",
                    name="name_example",
                    value="value_example",
                ),
            ],
        ),
        issuer_did="issuer_did_example",
        schema_id="schema_id_example",
        schema_issuer_did="schema_issuer_did_example",
        schema_name="schema_name_example",
        schema_version="schema_version_example",
        trace=True,
    ) # V10CredentialCreate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send holder a credential, automating entire flow
        api_response = api_instance.issue_credential_create_post(body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IssueCredentialV10Api->issue_credential_create_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10CredentialCreate**](V10CredentialCreate.md)|  | [optional]

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

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

# **issue_credential_records_cred_ex_id_delete**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} issue_credential_records_cred_ex_id_delete(cred_ex_id)

Remove an existing credential exchange record

### Example

```python
import time
import acapy_client
from acapy_client.api import issue_credential_v1_0_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = issue_credential_v1_0_api.IssueCredentialV10Api(api_client)
    cred_ex_id = "cred_ex_id_example" # str | Credential exchange identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove an existing credential exchange record
        api_response = api_instance.issue_credential_records_cred_ex_id_delete(cred_ex_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier |

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

# **issue_credential_records_cred_ex_id_get**
> V10CredentialExchange issue_credential_records_cred_ex_id_get(cred_ex_id)

Fetch a single credential exchange record

### Example

```python
import time
import acapy_client
from acapy_client.api import issue_credential_v1_0_api
from acapy_client.model.v10_credential_exchange import V10CredentialExchange
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = issue_credential_v1_0_api.IssueCredentialV10Api(api_client)
    cred_ex_id = "cred_ex_id_example" # str | Credential exchange identifier

    # example passing only required values which don't have defaults set
    try:
        # Fetch a single credential exchange record
        api_response = api_instance.issue_credential_records_cred_ex_id_get(cred_ex_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier |

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

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

# **issue_credential_records_cred_ex_id_issue_post**
> V10CredentialExchange issue_credential_records_cred_ex_id_issue_post(cred_ex_id)

Send holder a credential

### Example

```python
import time
import acapy_client
from acapy_client.api import issue_credential_v1_0_api
from acapy_client.model.v10_credential_issue_request import V10CredentialIssueRequest
from acapy_client.model.v10_credential_exchange import V10CredentialExchange
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = issue_credential_v1_0_api.IssueCredentialV10Api(api_client)
    cred_ex_id = "cred_ex_id_example" # str | Credential exchange identifier
    body = V10CredentialIssueRequest(
        comment="comment_example",
    ) # V10CredentialIssueRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send holder a credential
        api_response = api_instance.issue_credential_records_cred_ex_id_issue_post(cred_ex_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_issue_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send holder a credential
        api_response = api_instance.issue_credential_records_cred_ex_id_issue_post(cred_ex_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_issue_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier |
 **body** | [**V10CredentialIssueRequest**](V10CredentialIssueRequest.md)|  | [optional]

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

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

# **issue_credential_records_cred_ex_id_problem_report_post**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} issue_credential_records_cred_ex_id_problem_report_post(cred_ex_id)

Send a problem report for credential exchange

### Example

```python
import time
import acapy_client
from acapy_client.api import issue_credential_v1_0_api
from acapy_client.model.v10_credential_problem_report_request import V10CredentialProblemReportRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = issue_credential_v1_0_api.IssueCredentialV10Api(api_client)
    cred_ex_id = "cred_ex_id_example" # str | Credential exchange identifier
    body = V10CredentialProblemReportRequest(
        explain_ltxt="explain_ltxt_example",
    ) # V10CredentialProblemReportRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a problem report for credential exchange
        api_response = api_instance.issue_credential_records_cred_ex_id_problem_report_post(cred_ex_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_problem_report_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a problem report for credential exchange
        api_response = api_instance.issue_credential_records_cred_ex_id_problem_report_post(cred_ex_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_problem_report_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier |
 **body** | [**V10CredentialProblemReportRequest**](V10CredentialProblemReportRequest.md)|  | [optional]

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

# **issue_credential_records_cred_ex_id_send_offer_post**
> V10CredentialExchange issue_credential_records_cred_ex_id_send_offer_post(cred_ex_id)

Send holder a credential offer in reference to a proposal with preview

### Example

```python
import time
import acapy_client
from acapy_client.api import issue_credential_v1_0_api
from acapy_client.model.v10_credential_bound_offer_request import V10CredentialBoundOfferRequest
from acapy_client.model.v10_credential_exchange import V10CredentialExchange
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = issue_credential_v1_0_api.IssueCredentialV10Api(api_client)
    cred_ex_id = "cred_ex_id_example" # str | Credential exchange identifier
    body = V10CredentialBoundOfferRequest(
        counter_proposal={},
    ) # V10CredentialBoundOfferRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send holder a credential offer in reference to a proposal with preview
        api_response = api_instance.issue_credential_records_cred_ex_id_send_offer_post(cred_ex_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_send_offer_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send holder a credential offer in reference to a proposal with preview
        api_response = api_instance.issue_credential_records_cred_ex_id_send_offer_post(cred_ex_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_send_offer_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier |
 **body** | [**V10CredentialBoundOfferRequest**](V10CredentialBoundOfferRequest.md)|  | [optional]

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

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

# **issue_credential_records_cred_ex_id_send_request_post**
> V10CredentialExchange issue_credential_records_cred_ex_id_send_request_post(cred_ex_id)

Send issuer a credential request

### Example

```python
import time
import acapy_client
from acapy_client.api import issue_credential_v1_0_api
from acapy_client.model.v10_credential_exchange import V10CredentialExchange
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = issue_credential_v1_0_api.IssueCredentialV10Api(api_client)
    cred_ex_id = "cred_ex_id_example" # str | Credential exchange identifier

    # example passing only required values which don't have defaults set
    try:
        # Send issuer a credential request
        api_response = api_instance.issue_credential_records_cred_ex_id_send_request_post(cred_ex_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_send_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier |

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

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

# **issue_credential_records_cred_ex_id_store_post**
> V10CredentialExchange issue_credential_records_cred_ex_id_store_post(cred_ex_id)

Store a received credential

### Example

```python
import time
import acapy_client
from acapy_client.api import issue_credential_v1_0_api
from acapy_client.model.v10_credential_exchange import V10CredentialExchange
from acapy_client.model.v10_credential_store_request import V10CredentialStoreRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = issue_credential_v1_0_api.IssueCredentialV10Api(api_client)
    cred_ex_id = "cred_ex_id_example" # str | Credential exchange identifier
    body = V10CredentialStoreRequest(
        credential_id="credential_id_example",
    ) # V10CredentialStoreRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Store a received credential
        api_response = api_instance.issue_credential_records_cred_ex_id_store_post(cred_ex_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_store_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Store a received credential
        api_response = api_instance.issue_credential_records_cred_ex_id_store_post(cred_ex_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IssueCredentialV10Api->issue_credential_records_cred_ex_id_store_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier |
 **body** | [**V10CredentialStoreRequest**](V10CredentialStoreRequest.md)|  | [optional]

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

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

# **issue_credential_records_get**
> V10CredentialExchangeListResult issue_credential_records_get()

Fetch all credential exchange records

### Example

```python
import time
import acapy_client
from acapy_client.api import issue_credential_v1_0_api
from acapy_client.model.v10_credential_exchange_list_result import V10CredentialExchangeListResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = issue_credential_v1_0_api.IssueCredentialV10Api(api_client)
    connection_id = "connection_id_example" # str | Connection identifier (optional)
    role = "issuer" # str | Role assigned in credential exchange (optional)
    state = "proposal_sent" # str | Credential exchange state (optional)
    thread_id = "thread_id_example" # str | Thread identifier (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all credential exchange records
        api_response = api_instance.issue_credential_records_get(connection_id=connection_id, role=role, state=state, thread_id=thread_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IssueCredentialV10Api->issue_credential_records_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection identifier | [optional]
 **role** | **str**| Role assigned in credential exchange | [optional]
 **state** | **str**| Credential exchange state | [optional]
 **thread_id** | **str**| Thread identifier | [optional]

### Return type

[**V10CredentialExchangeListResult**](V10CredentialExchangeListResult.md)

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

# **issue_credential_send_offer_post**
> V10CredentialExchange issue_credential_send_offer_post()

Send holder a credential offer, independent of any proposal

### Example

```python
import time
import acapy_client
from acapy_client.api import issue_credential_v1_0_api
from acapy_client.model.v10_credential_free_offer_request import V10CredentialFreeOfferRequest
from acapy_client.model.v10_credential_exchange import V10CredentialExchange
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = issue_credential_v1_0_api.IssueCredentialV10Api(api_client)
    body = V10CredentialFreeOfferRequest(
        auto_issue=True,
        auto_remove=True,
        comment="comment_example",
        connection_id="connection_id_example",
        cred_def_id="cred_def_id_example",
        credential_preview=CredentialPreview(
            type="type_example",
            attributes=[
                CredAttrSpec(
                    mime_type="mime_type_example",
                    name="name_example",
                    value="value_example",
                ),
            ],
        ),
        trace=True,
    ) # V10CredentialFreeOfferRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send holder a credential offer, independent of any proposal
        api_response = api_instance.issue_credential_send_offer_post(body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IssueCredentialV10Api->issue_credential_send_offer_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10CredentialFreeOfferRequest**](V10CredentialFreeOfferRequest.md)|  | [optional]

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

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

# **issue_credential_send_post**
> V10CredentialExchange issue_credential_send_post()

Send holder a credential, automating entire flow

### Example

```python
import time
import acapy_client
from acapy_client.api import issue_credential_v1_0_api
from acapy_client.model.v10_credential_proposal_request_mand import V10CredentialProposalRequestMand
from acapy_client.model.v10_credential_exchange import V10CredentialExchange
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = issue_credential_v1_0_api.IssueCredentialV10Api(api_client)
    body = V10CredentialProposalRequestMand(
        auto_remove=True,
        comment="comment_example",
        connection_id="connection_id_example",
        cred_def_id="cred_def_id_example",
        credential_proposal=CredentialPreview(
            type="type_example",
            attributes=[
                CredAttrSpec(
                    mime_type="mime_type_example",
                    name="name_example",
                    value="value_example",
                ),
            ],
        ),
        issuer_did="issuer_did_example",
        schema_id="schema_id_example",
        schema_issuer_did="schema_issuer_did_example",
        schema_name="schema_name_example",
        schema_version="schema_version_example",
        trace=True,
    ) # V10CredentialProposalRequestMand |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send holder a credential, automating entire flow
        api_response = api_instance.issue_credential_send_post(body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IssueCredentialV10Api->issue_credential_send_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10CredentialProposalRequestMand**](V10CredentialProposalRequestMand.md)|  | [optional]

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

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

# **issue_credential_send_proposal_post**
> V10CredentialExchange issue_credential_send_proposal_post()

Send issuer a credential proposal

### Example

```python
import time
import acapy_client
from acapy_client.api import issue_credential_v1_0_api
from acapy_client.model.v10_credential_proposal_request_opt import V10CredentialProposalRequestOpt
from acapy_client.model.v10_credential_exchange import V10CredentialExchange
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = issue_credential_v1_0_api.IssueCredentialV10Api(api_client)
    body = V10CredentialProposalRequestOpt(
        auto_remove=True,
        comment="comment_example",
        connection_id="connection_id_example",
        cred_def_id="cred_def_id_example",
        credential_proposal=CredentialPreview(
            type="type_example",
            attributes=[
                CredAttrSpec(
                    mime_type="mime_type_example",
                    name="name_example",
                    value="value_example",
                ),
            ],
        ),
        issuer_did="issuer_did_example",
        schema_id="schema_id_example",
        schema_issuer_did="schema_issuer_did_example",
        schema_name="schema_name_example",
        schema_version="schema_version_example",
        trace=True,
    ) # V10CredentialProposalRequestOpt |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send issuer a credential proposal
        api_response = api_instance.issue_credential_send_proposal_post(body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling IssueCredentialV10Api->issue_credential_send_proposal_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10CredentialProposalRequestOpt**](V10CredentialProposalRequestOpt.md)|  | [optional]

### Return type

[**V10CredentialExchange**](V10CredentialExchange.md)

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

