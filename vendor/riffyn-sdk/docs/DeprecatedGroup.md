# DeprecatedGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the process (group) | [optional] 
**name** | **str** | The name of the item | [optional] 
**top_level** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**connections** | [**list[ConnectionLine]**](ConnectionLine.md) |  | [optional] 
**entities** | [**list[DeprecatedGroupEntities]**](DeprecatedGroupEntities.md) |  | [optional] 
**top_group_id** | **str** |  | [optional] 
**shareable** | **bool** | Indicates if the process can be shared with other users. | [optional] 
**accessible_to** | [**AccessibleTo**](AccessibleTo.md) |  | [optional] 
**public** | **bool** | Indicates if the process is visible to all users. | [optional] 
**activity_order** | **list[str]** | An array of activity/step IDs as ordered in the &#x60;getProcess&#x60; endpoint. | [optional] 
**instruction_exceptions** | **list[str]** | Exceptions to the order of instructions. | [optional] 
**status** | **str** |  | [optional] 
**compliant** | **bool** | 21CRF compliant. | [optional] 
**signers** | **list[str]** |  | [optional] 
**permissions** | **int** | The permission level of the entity. | [optional] 
**creator** | **str** | The username of the user that created this process | [optional] 
**created** | [**Created**](Created.md) |  | [optional] 
**org** | [**Org**](Org.md) |  | [optional] 
**modified** | [**Modified**](Modified.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

