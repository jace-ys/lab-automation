# UpdateResourceTypeBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of resource type. If you do not provide this value, the existing name will be deleted. | [optional] 
**parents** | **str** | The parents of the resource type. | [optional] 
**definition** | **str** | A brief description of the new resource type. If you do not provide this value, the existing description will be deleted. | [optional] 
**properties** | [**list[UpdateResourceTypeBodyProperties]**](UpdateResourceTypeBodyProperties.md) | The full list of immutable property types and values you would like to assign to the resource type. Existing immutable values will be deleted and replaced with these values | [optional] 
**components** | [**list[UpdateResourceTypeBodyComponents]**](UpdateResourceTypeBodyComponents.md) | Defines the components of this resource type. E.g. The components of coffee are water and coffee grounds. | [optional] 
**source** | **str** | Indicates whether the resource type was created by Riffyn, or by a user. | [optional] 
**synonyms** | **str** | An array of synonyms for the resource type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

