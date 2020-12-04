# PropertyDef

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The &#x60;_id&#x60; of the property type. | [optional] 
**name** | **str** | The &#x60;name&#x60; of the property type. | [optional] 
**specs** | [**Spec**](Spec.md) |  | [optional] 
**hint** | [**Hint**](Hint.md) |  | [optional] 
**rules** | [**list[PropertyRule]**](PropertyRule.md) |  | [optional] 
**immutable** | **bool** | Indicates if the values for this property can be changed, once set. | [optional] 
**adhoc** | **bool** | If &#x60;true&#x60;, this property is custom to the experiment and does not exist at the process level. | [optional] 
**key** | **str** | A string value that uniquely identifies this property in the &#x60;adhocItems&#x60; list. | [optional] 
**unit** | [**PropertyDefUnit**](PropertyDefUnit.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

