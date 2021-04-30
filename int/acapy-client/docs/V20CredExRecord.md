# V20CredExRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_issue** | **bool** | Issuer choice to issue to request in this credential exchange | [optional] 
**auto_offer** | **bool** | Holder choice to accept offer in this credential exchange | [optional] 
**auto_remove** | **bool** | Issuer choice to remove this credential exchange record when complete | [optional] 
**by_format** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Attachment content by format for proposal, offer, request, and issue | [optional] [readonly] 
**connection_id** | **str** | Connection identifier | [optional] 
**created_at** | **str** | Time of record creation | [optional] 
**cred_ex_id** | **str** | Credential exchange identifier | [optional] 
**cred_id_stored** | **str** | Credential identifier stored in wallet | [optional] 
**cred_issue** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Serialized credential issue message | [optional] 
**cred_offer** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Serialized credential offer message | [optional] 
**cred_preview** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Serialized credential preview from credential proposal | [optional] [readonly] 
**cred_proposal** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Serialized credential proposal message | [optional] 
**cred_request** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Serialized credential request message | [optional] 
**error_msg** | **str** | Error message | [optional] 
**initiator** | **str** | Issue-credential exchange initiator: self or external | [optional] 
**parent_thread_id** | **str** | Parent thread identifier | [optional] 
**role** | **str** | Issue-credential exchange role: holder or issuer | [optional] 
**state** | **str** | Issue-credential exchange state | [optional] 
**thread_id** | **str** | Thread identifier | [optional] 
**trace** | **bool** | Record trace information, based on agent configuration | [optional] 
**updated_at** | **str** | Time of last record update | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


