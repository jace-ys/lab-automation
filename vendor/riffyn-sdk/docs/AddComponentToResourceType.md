# AddComponentToResourceType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type_id** | **str** | The &#x60;_id&#x60; of the resource type of the component being added to the activity input or output.  | 
**properties** | **list[str]** |  | [optional] 
**clear_existing_properties** | **bool** | If set to &#x60;true&#x60; and no &#x60;properties&#x60; are being included in the request body, &#x60;clearExistingProperties&#x60; will remove default properties on the component being added. | [optional] 
**propagate** | **bool** | Propagates addition of the component to all connected instances of the resource type. Property types that are added to the component will not be propagated, only the default properties of the component. Propagate defaults to &#x60;true&#x60; if not set to &#x60;false&#x60;. | [optional] 
**propagation_direction** | **str** | Direction of propagation. Will be one of &#x60;upstream&#x60; or &#x60;downstream&#x60;. Defaults to &#x60;downstream&#x60; if not set. Not required if &#x60;propagate&#x60; is not defined. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

