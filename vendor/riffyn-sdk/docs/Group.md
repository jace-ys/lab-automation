# Group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the process (group) | [optional] 
**name** | **str** | The name of the item | [optional] 
**top_level** | **bool** | Indicates whether the group is a process or a subgroup of a process. | [optional] 
**description** | **str** |  | [optional] 
**connections** | [**list[ConnectionLine]**](ConnectionLine.md) |  | [optional] 
**entities** | [**list[GroupEntities]**](GroupEntities.md) |  | [optional] 
**top_group_id** | **str** | The process this group belongs to. | [optional] 
**shareable** | **bool** | Indicates if the process can be shared with other users | [optional] 
**accessible_to** | [**AccessibleTo**](AccessibleTo.md) |  | [optional] 
**public** | [**Public**](Public.md) |  | [optional] 
**activity_order** | **list[str]** | An array of activity/step IDs as ordered in the &#x60;getProcess&#x60; endpoint. | [optional] 
**instruction_exceptions** | **list[str]** | Exceptions to the order of instructions. | [optional] 
**status** | **str** |  | [optional] 
**compliant** | **bool** | 21CRF compliant. | [optional] 
**signers** | **list[str]** |  | [optional] 
**req_signatures** | **int** | The number of signatures required for approval. | [optional] 
**locked** | **bool** | If true, edits are disabled pending approval of signatures. | [optional] 
**permissions** | [**Permissions**](Permissions.md) |  | [optional] 
**modified_by** | [**ModifiedBy**](ModifiedBy.md) |  | [optional] 
**creator** | [**Creator**](Creator.md) |  | [optional] 
**created** | [**Created**](Created.md) |  | [optional] 
**org** | [**Org**](Org.md) |  | [optional] 
**modified** | [**Modified**](Modified.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**object_id** | **str** |  | [optional] 
**parent** | [**GroupParent**](GroupParent.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

