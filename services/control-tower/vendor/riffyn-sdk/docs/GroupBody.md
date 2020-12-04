# GroupBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the group being created. | [optional] 
**description** | **str** | The description of the group being created. | [optional] 
**parent_id** | **str** | The &#x60;_id&#x60; of the group or process this new group will be created in. A &#x60;parentId&#x60; is not required when creating a group at the top level of the process. | [optional] 
**entities** | [**list[GroupBodyEntities]**](GroupBodyEntities.md) |  | [optional] 
**propagate** | **bool** | Propagates the connection to parent if it exists. Defaults to true if not set to false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

