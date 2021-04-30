# LDProofVCDetailOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proof_type** | **str** | The proof type used for the proof. Should match suites registered in the Linked Data Cryptographic Suite Registry | 
**challenge** | **str** | A challenge to include in the proof. SHOULD be provided by the requesting party of the credential (&#x3D;holder) | [optional] 
**created** | **str** | The date and time of the proof (with a maximum accuracy in seconds). Defaults to current system time | [optional] 
**credential_status** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The credential status mechanism to use for the credential. Omitting the property indicates the issued credential will not include a credential status | [optional] 
**domain** | **str** | The intended domain of validity for the proof | [optional] 
**proof_purpose** | **str** | The proof purpose used for the proof. Should match proof purposes registered in the Linked Data Proofs Specification | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


