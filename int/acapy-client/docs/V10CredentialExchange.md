# V10CredentialExchange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_issue** | **bool** | Issuer choice to issue to request in this credential exchange | [optional] 
**auto_offer** | **bool** | Holder choice to accept offer in this credential exchange | [optional] 
**auto_remove** | **bool** | Issuer choice to remove this credential exchange record when complete | [optional] 
**connection_id** | **str** | Connection identifier | [optional] 
**created_at** | **str** | Time of record creation | [optional] 
**credential** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Credential as stored | [optional] 
**credential_definition_id** | **str** | Credential definition identifier | [optional] 
**credential_exchange_id** | **str** | Credential exchange identifier | [optional] 
**credential_id** | **str** | Credential identifier | [optional] 
**credential_offer** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | (Indy) credential offer | [optional] 
**credential_offer_dict** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Serialized credential offer message | [optional] 
**credential_proposal_dict** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Serialized credential proposal message | [optional] 
**credential_request** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | (Indy) credential request | [optional] 
**credential_request_metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | (Indy) credential request metadata | [optional] 
**error_msg** | **str** | Error message | [optional] 
**initiator** | **str** | Issue-credential exchange initiator: self or external | [optional] 
**parent_thread_id** | **str** | Parent thread identifier | [optional] 
**raw_credential** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Credential as received, prior to storage in holder wallet | [optional] 
**revoc_reg_id** | **str** | Revocation registry identifier | [optional] 
**revocation_id** | **str** | Credential identifier within revocation registry | [optional] 
**role** | **str** | Issue-credential exchange role: holder or issuer | [optional] 
**schema_id** | **str** | Schema identifier | [optional] 
**state** | **str** | Issue-credential exchange state | [optional] 
**thread_id** | **str** | Thread identifier | [optional] 
**trace** | **bool** | Record trace information, based on agent configuration | [optional] 
**updated_at** | **str** | Time of last record update | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


