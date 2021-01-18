# ResourceType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the resource type. | [optional] 
**name** | **str** | The name of the item. | [optional] 
**definition** | **str** | A brief description of this resource type | [optional] 
**parents** | [**list[ResourceTypeParents]**](ResourceTypeParents.md) | A list of parents for the resource type. | [optional] 
**synonyms** | **list[str]** | A list of additional names that may be used to help identify this resource type. | [optional] 
**source** | **str** | Indicates whether the resource type was created by Riffyn, or by a user. | [optional] 
**properties** | [**list[PropertyDef]**](PropertyDef.md) |  | [optional] 
**components** | [**list[Component]**](Component.md) |  | [optional] 
**sharable** | **bool** | Indicates if the resource type can be shared with other users | [optional] 
**public** | **bool** | Indicates if the resource type is visible to all users | [optional] 
**deleted** | **bool** | Indicates if the resource type has been soft deleted | [optional] 
**creator** | **str** | The username of the user that created this resource type | [optional] 
**created** | [**Created**](Created.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

