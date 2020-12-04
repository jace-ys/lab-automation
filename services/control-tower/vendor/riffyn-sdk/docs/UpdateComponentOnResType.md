# UpdateComponentOnResType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type_id** | **str** | The &#x60;_id&#x60; of the resource type of the component being updated on the activity input or output.  | 
**propagate** | **bool** | Propagates the updated component to connected instances of the resource type on the activity. Defaults to true if not set to false. | [optional] 
**propagation_direction** | **str** | Direction of propagation. Will be one of &#x60;upstream&#x60; or &#x60;downstream&#x60;. Defaults to &#x60;downstream&#x60; if not set. Not required if &#x60;propagate&#x60; is not defined. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

