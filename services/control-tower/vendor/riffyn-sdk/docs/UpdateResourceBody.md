# UpdateResourceBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of resource. If you do not provide this value, the existing name will be deleted | 
**description** | **str** | A brief description of the new resource. If you do not provide this value, the existing description will be deleted | [optional] 
**properties** | [**list[UpdateResourceBodyProperties]**](UpdateResourceBodyProperties.md) | The full list of immutable property types and values you would like to assign to the resource. Existing immutable values will be deleted and replaced with these values | [optional] 
**components** | [**list[UpdateResourceBodyComponents]**](UpdateResourceBodyComponents.md) | Defines the components of this resource. E.g. The components of coffee are water and coffee grounds. | [optional] 
**is_instrument** | **bool** | Deprecated - Indicated if the new resource is an instrument. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

