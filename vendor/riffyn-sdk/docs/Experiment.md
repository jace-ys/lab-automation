# Experiment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the experiment. | [optional] 
**name** | **str** | The name of the item. | [optional] 
**num** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**overrides** | [**list[ExperimentOverrides]**](ExperimentOverrides.md) |  | [optional] 
**shareable** | **bool** | Indicates if the experiment can be shared with other users. | [optional] 
**accessible_to** | [**AccessibleTo**](AccessibleTo.md) |  | [optional] 
**public** | **bool** | Indicates if the experiment is visible to all users. | [optional] 
**modified_by** | [**ModifiedBy**](ModifiedBy.md) |  | [optional] 
**modified** | [**Modified**](Modified.md) |  | [optional] 
**status** | **str** | The status of the electronic signature. | [optional] 
**compliant** | **str** | 21CRF compliant. | [optional] 
**signers** | **list[str]** | The list of required signatures. | [optional] 
**top_group** | [**TopGroup**](TopGroup.md) |  | [optional] 
**permissions** | **int** | The permission level of the entity. | [optional] 
**creator** | **str** | The username of the user that created this experiment. | [optional] 
**created** | [**Created**](Created.md) |  | [optional] 
**org** | [**Org**](Org.md) |  | [optional] 
**linked_to** | **list[str]** |  | [optional] 
**activity_order** | **list[str]** | An array of activity/step IDs as ordered in the &#x60;getProcess&#x60; endpoint. | [optional] 
**description** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

