# acapy_client.OutOfBandApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**out_of_band_create_invitation_post**](OutOfBandApi.md#out_of_band_create_invitation_post) | **POST** /out-of-band/create-invitation | Create a new connection invitation
[**out_of_band_receive_invitation_post**](OutOfBandApi.md#out_of_band_receive_invitation_post) | **POST** /out-of-band/receive-invitation | Receive a new connection invitation


# **out_of_band_create_invitation_post**
> InvitationRecord out_of_band_create_invitation_post()

Create a new connection invitation

### Example

```python
import time
import acapy_client
from acapy_client.api import out_of_band_api
from acapy_client.model.invitation_create_request import InvitationCreateRequest
from acapy_client.model.invitation_record import InvitationRecord
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = out_of_band_api.OutOfBandApi(api_client)
    auto_accept = "auto_accept_example" # str | Auto-accept connection (defaults to configuration) (optional)
    multi_use = True # bool | Create invitation for multiple use (default false) (optional)
    body = InvitationCreateRequest(
        alias="alias_example",
        attachments=[
            AttachmentDef(
                id="id_example",
                type="credential-offer",
            ),
        ],
        handshake_protocols=[
            "handshake_protocols_example",
        ],
        mediation_id="mediation_id_example",
        metadata={},
        my_label="my_label_example",
        use_public_did=True,
    ) # InvitationCreateRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new connection invitation
        api_response = api_instance.out_of_band_create_invitation_post(auto_accept=auto_accept, multi_use=multi_use, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling OutOfBandApi->out_of_band_create_invitation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_accept** | **str**| Auto-accept connection (defaults to configuration) | [optional]
 **multi_use** | **bool**| Create invitation for multiple use (default false) | [optional]
 **body** | [**InvitationCreateRequest**](InvitationCreateRequest.md)|  | [optional]

### Return type

[**InvitationRecord**](InvitationRecord.md)

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

# **out_of_band_receive_invitation_post**
> ConnRecord out_of_band_receive_invitation_post()

Receive a new connection invitation

### Example

```python
import time
import acapy_client
from acapy_client.api import out_of_band_api
from acapy_client.model.invitation_receive_request import InvitationReceiveRequest
from acapy_client.model.conn_record import ConnRecord
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acapy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acapy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = out_of_band_api.OutOfBandApi(api_client)
    alias = "alias_example" # str | Alias for connection (optional)
    auto_accept = "auto_accept_example" # str | Auto-accept connection (defaults to configuration) (optional)
    mediation_id = "mediation_id_example" # str | Identifier for active mediation record to be used (optional)
    use_existing_connection = True # bool | Use an existing connection, if possible (optional)
    body = InvitationReceiveRequest(
        id="id_example",
        handshake_protocols=[
            "handshake_protocols_example",
        ],
        label="label_example",
        requestsattach=[
            AttachDecorator(
                id="id_example",
                byte_count=1,
                data=AttachDecoratorData(
                    base64="base64_example",
                    json={},
                    jws={},
                    links=[
                        "links_example",
                    ],
                    sha256="sha256_example",
                ),
                description="description_example",
                filename="filename_example",
                lastmod_time="lastmod_time_example",
                mime_type="mime_type_example",
            ),
        ],
        service_blocks=[
            Service(
                did="did_example",
                id="id_example",
                recipient_keys=[
                    "recipient_keys_example",
                ],
                routing_keys=[
                    "routing_keys_example",
                ],
                service_endpoint="service_endpoint_example",
                type="type_example",
            ),
        ],
        service_dids=[
            "service_dids_example",
        ],
        services={},
    ) # InvitationReceiveRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Receive a new connection invitation
        api_response = api_instance.out_of_band_receive_invitation_post(alias=alias, auto_accept=auto_accept, mediation_id=mediation_id, use_existing_connection=use_existing_connection, body=body)
        pprint(api_response)
    except acapy_client.ApiException as e:
        print("Exception when calling OutOfBandApi->out_of_band_receive_invitation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias for connection | [optional]
 **auto_accept** | **str**| Auto-accept connection (defaults to configuration) | [optional]
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional]
 **use_existing_connection** | **bool**| Use an existing connection, if possible | [optional]
 **body** | [**InvitationReceiveRequest**](InvitationReceiveRequest.md)|  | [optional]

### Return type

[**ConnRecord**](ConnRecord.md)

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

