# RunDataResponseInner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_def_id** | **str** | The&#x60;resourceDefId&#x60; from the activity &#x60;inputs&#x60; or &#x60;outputs&#x60;. | [optional] 
**property_type_id** | **str** | The &#x60;_id&#x60; of the property type. | [optional] 
**event_group_id** | **str** | The &#x60;_id&#x60; of the event group for the property the data was added to. | [optional] 
**run_ids** | **list[str]** | An array of strings containing a specific list of run &#x60;_id&#x60;s. | [optional] 
**run_group_id** | **str** | The &#x60;_id&#x60; of the run group the data was added to. | [optional] 
**component_id** | **str** | The &#x60;_id&#x60; of the component. | [optional] 
**data** | **list[object]** | An object with the eventIds and the values that were added (Immutable properties will not return a data array). | [optional] 
**append** | **bool** | Indicates if the &#x60;values&#x60; was appended to the existing data. This field will only be returned if it was passed in the body. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

