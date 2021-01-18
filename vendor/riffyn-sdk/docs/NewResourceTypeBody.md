# NewResourceTypeBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new resource type. | 
**source** | **str** | Indicates whether the resource type was created by Riffyn, or by a user. | [optional] 
**parents** | [**list[NewResourceTypeBodyParents]**](NewResourceTypeBodyParents.md) |  | 
**synonyms** | **str** | An array of synonyms for the resource type. | [optional] 
**definition** | **str** | A definition of the new resource type. | [optional] 
**properties** | [**list[NewResourceTypeBodyProperties]**](NewResourceTypeBodyProperties.md) | The list of property types you would like to assign to the new resource. | [optional] 
**components** | [**list[NewResourceTypeBodyComponents]**](NewResourceTypeBodyComponents.md) | Defines the components of this resource. E.g. The components of coffee are water and coffee grounds. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

