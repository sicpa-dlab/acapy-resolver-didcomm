# acapy_client.PresentProofV10Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**present_proof_create_request_post**](PresentProofV10Api.md#present_proof_create_request_post) | **POST** /present-proof/create-request | Creates a presentation request not bound to any proposal or connection
[**present_proof_records_get**](PresentProofV10Api.md#present_proof_records_get) | **GET** /present-proof/records | Fetch all present-proof exchange records
[**present_proof_records_pres_ex_id_credentials_get**](PresentProofV10Api.md#present_proof_records_pres_ex_id_credentials_get) | **GET** /present-proof/records/{pres_ex_id}/credentials | Fetch credentials for a presentation request from wallet
[**present_proof_records_pres_ex_id_delete**](PresentProofV10Api.md#present_proof_records_pres_ex_id_delete) | **DELETE** /present-proof/records/{pres_ex_id} | Remove an existing presentation exchange record
[**present_proof_records_pres_ex_id_get**](PresentProofV10Api.md#present_proof_records_pres_ex_id_get) | **GET** /present-proof/records/{pres_ex_id} | Fetch a single presentation exchange record
[**present_proof_records_pres_ex_id_problem_report_post**](PresentProofV10Api.md#present_proof_records_pres_ex_id_problem_report_post) | **POST** /present-proof/records/{pres_ex_id}/problem-report | Send a problem report for presentation exchange
[**present_proof_records_pres_ex_id_send_presentation_post**](PresentProofV10Api.md#present_proof_records_pres_ex_id_send_presentation_post) | **POST** /present-proof/records/{pres_ex_id}/send-presentation | Sends a proof presentation
[**present_proof_records_pres_ex_id_send_request_post**](PresentProofV10Api.md#present_proof_records_pres_ex_id_send_request_post) | **POST** /present-proof/records/{pres_ex_id}/send-request | Sends a presentation request in reference to a proposal
[**present_proof_records_pres_ex_id_verify_presentation_post**](PresentProofV10Api.md#present_proof_records_pres_ex_id_verify_presentation_post) | **POST** /present-proof/records/{pres_ex_id}/verify-presentation | Verify a received presentation
[**present_proof_send_proposal_post**](PresentProofV10Api.md#present_proof_send_proposal_post) | **POST** /present-proof/send-proposal | Sends a presentation proposal
[**present_proof_send_request_post**](PresentProofV10Api.md#present_proof_send_request_post) | **POST** /present-proof/send-request | Sends a free presentation request not bound to any proposal


# **present_proof_create_request_post**
> V10PresentationExchange present_proof_create_request_post()

Creates a presentation request not bound to any proposal or connection

### Example

```python
import time
import acapy_client
from acapy_client.api import present_proof_v1_0_api
from acapy_client.model.v10_presentation_exchange import V10PresentationExchange
from acapy_client.model.v10_presentation_create_request_request import V10PresentationCreateRequestRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    body = V10PresentationCreateRequestRequest(
        comment="comment_example",
        proof_request=IndyProofRequest(
            name="name_example",
            non_revoked={},
            nonce="nonce_example",
            requested_attributes={
                "key": IndyProofReqAttrSpec(
                    name="name_example",
                    names=[
                        "names_example",
                    ],
                    non_revoked={},
                    restrictions=[
                        {
                            "key": "key_example",
                        },
                    ],
                ),
            },
            requested_predicates={
                "key": IndyProofReqPredSpec(
                    name="name_example",
                    non_revoked={},
                    p_type="<",
                    p_value=1,
                    restrictions=[
                        IndyProofReqPredSpecRestrictions(
                            cred_def_id="cred_def_id_example",
                            issuer_did="issuer_did_example",
                            schema_id="schema_id_example",
                            schema_issuer_did="schema_issuer_did_example",
                            schema_name="schema_name_example",
                            schema_version="schema_version_example",
                        ),
                    ],
                ),
            },
            version="version_example",
        ),
        trace=True,
    ) # V10PresentationCreateRequestRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a presentation request not bound to any proposal or connection
        api_response = api_instance.present_proof_create_request_post(body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_create_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10PresentationCreateRequestRequest**](V10PresentationCreateRequestRequest.md)|  | [optional]

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

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

# **present_proof_records_get**
> V10PresentationExchangeList present_proof_records_get()

Fetch all present-proof exchange records

### Example

```python
import time
import acapy_client
from acapy_client.api import present_proof_v1_0_api
from acapy_client.model.v10_presentation_exchange_list import V10PresentationExchangeList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    connection_id = "connection_id_example" # str | Connection identifier (optional)
    role = "prover" # str | Role assigned in presentation exchange (optional)
    state = "proposal_sent" # str | Presentation exchange state (optional)
    thread_id = "thread_id_example" # str | Thread identifier (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all present-proof exchange records
        api_response = api_instance.present_proof_records_get(connection_id=connection_id, role=role, state=state, thread_id=thread_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection identifier | [optional]
 **role** | **str**| Role assigned in presentation exchange | [optional]
 **state** | **str**| Presentation exchange state | [optional]
 **thread_id** | **str**| Thread identifier | [optional]

### Return type

[**V10PresentationExchangeList**](V10PresentationExchangeList.md)

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

# **present_proof_records_pres_ex_id_credentials_get**
> [IndyCredPrecis] present_proof_records_pres_ex_id_credentials_get(pres_ex_id)

Fetch credentials for a presentation request from wallet

### Example

```python
import time
import acapy_client
from acapy_client.api import present_proof_v1_0_api
from acapy_client.model.indy_cred_precis import IndyCredPrecis
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    pres_ex_id = "pres_ex_id_example" # str | Presentation exchange identifier
    count = "count_example" # str | Maximum number to retrieve (optional)
    extra_query = "extra_query_example" # str | (JSON) object mapping referents to extra WQL queries (optional)
    referent = "referent_example" # str | Proof request referents of interest, comma-separated (optional)
    start = "start_example" # str | Start index (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch credentials for a presentation request from wallet
        api_response = api_instance.present_proof_records_pres_ex_id_credentials_get(pres_ex_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_credentials_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch credentials for a presentation request from wallet
        api_response = api_instance.present_proof_records_pres_ex_id_credentials_get(pres_ex_id, count=count, extra_query=extra_query, referent=referent, start=start)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_credentials_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier |
 **count** | **str**| Maximum number to retrieve | [optional]
 **extra_query** | **str**| (JSON) object mapping referents to extra WQL queries | [optional]
 **referent** | **str**| Proof request referents of interest, comma-separated | [optional]
 **start** | **str**| Start index | [optional]

### Return type

[**[IndyCredPrecis]**](IndyCredPrecis.md)

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

# **present_proof_records_pres_ex_id_delete**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} present_proof_records_pres_ex_id_delete(pres_ex_id)

Remove an existing presentation exchange record

### Example

```python
import time
import acapy_client
from acapy_client.api import present_proof_v1_0_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    pres_ex_id = "pres_ex_id_example" # str | Presentation exchange identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove an existing presentation exchange record
        api_response = api_instance.present_proof_records_pres_ex_id_delete(pres_ex_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier |

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

# **present_proof_records_pres_ex_id_get**
> V10PresentationExchange present_proof_records_pres_ex_id_get(pres_ex_id)

Fetch a single presentation exchange record

### Example

```python
import time
import acapy_client
from acapy_client.api import present_proof_v1_0_api
from acapy_client.model.v10_presentation_exchange import V10PresentationExchange
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    pres_ex_id = "pres_ex_id_example" # str | Presentation exchange identifier

    # example passing only required values which don't have defaults set
    try:
        # Fetch a single presentation exchange record
        api_response = api_instance.present_proof_records_pres_ex_id_get(pres_ex_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier |

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

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

# **present_proof_records_pres_ex_id_problem_report_post**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} present_proof_records_pres_ex_id_problem_report_post(pres_ex_id)

Send a problem report for presentation exchange

### Example

```python
import time
import acapy_client
from acapy_client.api import present_proof_v1_0_api
from acapy_client.model.v10_presentation_problem_report_request import V10PresentationProblemReportRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    pres_ex_id = "pres_ex_id_example" # str | Presentation exchange identifier
    body = V10PresentationProblemReportRequest(
        explain_ltxt="explain_ltxt_example",
    ) # V10PresentationProblemReportRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a problem report for presentation exchange
        api_response = api_instance.present_proof_records_pres_ex_id_problem_report_post(pres_ex_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_problem_report_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a problem report for presentation exchange
        api_response = api_instance.present_proof_records_pres_ex_id_problem_report_post(pres_ex_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_problem_report_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier |
 **body** | [**V10PresentationProblemReportRequest**](V10PresentationProblemReportRequest.md)|  | [optional]

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

# **present_proof_records_pres_ex_id_send_presentation_post**
> V10PresentationExchange present_proof_records_pres_ex_id_send_presentation_post(pres_ex_id)

Sends a proof presentation

### Example

```python
import time
import acapy_client
from acapy_client.api import present_proof_v1_0_api
from acapy_client.model.v10_presentation_exchange import V10PresentationExchange
from acapy_client.model.indy_pres_spec import IndyPresSpec
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    pres_ex_id = "pres_ex_id_example" # str | Presentation exchange identifier
    body = IndyPresSpec(
        requested_attributes={
            "key": IndyRequestedCredsRequestedAttr(
                cred_id="cred_id_example",
                revealed=True,
            ),
        },
        requested_predicates={
            "key": IndyRequestedCredsRequestedPred(
                cred_id="cred_id_example",
                timestamp=0,
            ),
        },
        self_attested_attributes={
            "key": "key_example",
        },
        trace=True,
    ) # IndyPresSpec |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Sends a proof presentation
        api_response = api_instance.present_proof_records_pres_ex_id_send_presentation_post(pres_ex_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_send_presentation_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sends a proof presentation
        api_response = api_instance.present_proof_records_pres_ex_id_send_presentation_post(pres_ex_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_send_presentation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier |
 **body** | [**IndyPresSpec**](IndyPresSpec.md)|  | [optional]

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

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

# **present_proof_records_pres_ex_id_send_request_post**
> V10PresentationExchange present_proof_records_pres_ex_id_send_request_post(pres_ex_id)

Sends a presentation request in reference to a proposal

### Example

```python
import time
import acapy_client
from acapy_client.api import present_proof_v1_0_api
from acapy_client.model.admin_api_message_tracing import AdminAPIMessageTracing
from acapy_client.model.v10_presentation_exchange import V10PresentationExchange
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    pres_ex_id = "pres_ex_id_example" # str | Presentation exchange identifier
    body = AdminAPIMessageTracing(
        trace=True,
    ) # AdminAPIMessageTracing |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Sends a presentation request in reference to a proposal
        api_response = api_instance.present_proof_records_pres_ex_id_send_request_post(pres_ex_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_send_request_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sends a presentation request in reference to a proposal
        api_response = api_instance.present_proof_records_pres_ex_id_send_request_post(pres_ex_id, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_send_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier |
 **body** | [**AdminAPIMessageTracing**](AdminAPIMessageTracing.md)|  | [optional]

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

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

# **present_proof_records_pres_ex_id_verify_presentation_post**
> V10PresentationExchange present_proof_records_pres_ex_id_verify_presentation_post(pres_ex_id)

Verify a received presentation

### Example

```python
import time
import acapy_client
from acapy_client.api import present_proof_v1_0_api
from acapy_client.model.v10_presentation_exchange import V10PresentationExchange
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    pres_ex_id = "pres_ex_id_example" # str | Presentation exchange identifier

    # example passing only required values which don't have defaults set
    try:
        # Verify a received presentation
        api_response = api_instance.present_proof_records_pres_ex_id_verify_presentation_post(pres_ex_id)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_verify_presentation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier |

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

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

# **present_proof_send_proposal_post**
> V10PresentationExchange present_proof_send_proposal_post()

Sends a presentation proposal

### Example

```python
import time
import acapy_client
from acapy_client.api import present_proof_v1_0_api
from acapy_client.model.v10_presentation_exchange import V10PresentationExchange
from acapy_client.model.v10_presentation_proposal_request import V10PresentationProposalRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    body = V10PresentationProposalRequest(
        auto_present=True,
        comment="comment_example",
        connection_id="connection_id_example",
        presentation_proposal=IndyPresPreview(
            type="type_example",
            attributes=[
                IndyPresAttrSpec(
                    cred_def_id="cred_def_id_example",
                    mime_type="mime_type_example",
                    name="name_example",
                    referent="referent_example",
                    value="value_example",
                ),
            ],
            predicates=[
                IndyPresPredSpec(
                    cred_def_id="cred_def_id_example",
                    name="name_example",
                    predicate="<",
                    threshold=1,
                ),
            ],
        ),
        trace=True,
    ) # V10PresentationProposalRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sends a presentation proposal
        api_response = api_instance.present_proof_send_proposal_post(body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_send_proposal_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10PresentationProposalRequest**](V10PresentationProposalRequest.md)|  | [optional]

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

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

# **present_proof_send_request_post**
> V10PresentationExchange present_proof_send_request_post()

Sends a free presentation request not bound to any proposal

### Example

```python
import time
import acapy_client
from acapy_client.api import present_proof_v1_0_api
from acapy_client.model.v10_presentation_exchange import V10PresentationExchange
from acapy_client.model.v10_presentation_send_request_request import V10PresentationSendRequestRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    body = V10PresentationSendRequestRequest(
        comment="comment_example",
        connection_id="connection_id_example",
        proof_request=IndyProofRequest(
            name="name_example",
            non_revoked={},
            nonce="nonce_example",
            requested_attributes={
                "key": IndyProofReqAttrSpec(
                    name="name_example",
                    names=[
                        "names_example",
                    ],
                    non_revoked={},
                    restrictions=[
                        {
                            "key": "key_example",
                        },
                    ],
                ),
            },
            requested_predicates={
                "key": IndyProofReqPredSpec(
                    name="name_example",
                    non_revoked={},
                    p_type="<",
                    p_value=1,
                    restrictions=[
                        IndyProofReqPredSpecRestrictions(
                            cred_def_id="cred_def_id_example",
                            issuer_did="issuer_did_example",
                            schema_id="schema_id_example",
                            schema_issuer_did="schema_issuer_did_example",
                            schema_name="schema_name_example",
                            schema_version="schema_version_example",
                        ),
                    ],
                ),
            },
            version="version_example",
        ),
        trace=True,
    ) # V10PresentationSendRequestRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sends a free presentation request not bound to any proposal
        api_response = api_instance.present_proof_send_request_post(body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_send_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10PresentationSendRequestRequest**](V10PresentationSendRequestRequest.md)|  | [optional]

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

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

