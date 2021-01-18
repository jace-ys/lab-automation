# ResourceDef

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique key that&#x27;s generated for each &#x60;input&#x60; or &#x60;output&#x60; of an activity. This value is referenced as &#x60;resourceDefId&#x60; in other data sets | [optional] 
**properties** | [**list[PropertyDef]**](PropertyDef.md) |  | [optional] 
**components** | [**list[Component]**](Component.md) |  | [optional] 
**sample** | **bool** |  | [optional] 
**direction** | **str** | Allowed values are &#x60;input&#x60; and &#x60;output&#x60;. | [optional] 
**name** | **str** | The &#x60;name&#x60; of the resource type associated with this resource definition. | [optional] 
**adhoc** | **bool** | If &#x60;true&#x60;, this resource is custom to the experiment and does not exist at the process level. | [optional] 
**key** | **str** | A string value that uniquely identifies this resource in the &#x60;adhocItems&#x60; list. | [optional] 
**type_id** | **str** | The &#x60;_id&#x60; of the resource type associated with this resource definition. | [optional] 
**type_name** | **str** | The &#x60;name&#x60; of the resource type associated with this resource definition. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

