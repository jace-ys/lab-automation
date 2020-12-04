# AddDataToInputBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_def_id** | **str** | ResourceDefs are the &#x60;inputs&#x60; and &#x60;outputs&#x60; of the activity (step). A &#x60;resourceDefId&#x60; is the &#x60;_id&#x60; of one of those &#x60;inputs&#x60; or &#x60;outputs&#x60;. | 
**property_type_id** | **str** | The &#x60;_id&#x60; of the property type, for the property you&#x27;d like to add data to. Fixed properties may only be set with a single value. | 
**event_group_id** | **str** | The &#x60;_id&#x60; of the event group for the property you&#x27;d like to add data to. You must specify eventIds when using eventGroupId. You cannot specify an eventGroupId for a new event. You cannot add more eventIds than what exists in the eventGroup. When eventGroupId is used &#x60;runIds&#x60; must be included. &#x60;runGroupIds&#x60; and &#x60;append&#x60; cannot be used. | [optional] 
**run_group_id** | **str** | The &#x60;_id&#x60; of the run group you&#x27;d like to add data to. &#x60;runGroupId&#x60; can be used instead of &#x60;runIds&#x60;. One of &#x60;runGroupId&#x60; or &#x60;runIds&#x60; must be provided. | 
**run_ids** | **list[str]** | An array of strings containing a specific list of run &#x60;_id&#x60;s to add the values to. When &#x60;runIds&#x60; are defined &#x60;runGroupId&#x60; will be ignored. One of &#x60;runGroupId&#x60; or &#x60;runIds&#x60; must be provided. | 
**component_id** | **str** | The &#x60;_id&#x60; of the component you&#x27;d like to add data to. Components are defined in the &#x60;inputs&#x60; and &#x60;outputs&#x60; of the activity (step) | [optional] 
**values** | [**list[AddDataToInputBodyValues]**](AddDataToInputBodyValues.md) | An array of string values (Immutable properties are single-valued. If multiple values are provided only the first one will be used). For multivalued data, an object with the eventIds and the values to be added. Dates must be in ISO, &#x60;2018-08-31T15:53:48.998Z&#x60; time format. All other types of values will be parsed and converted to the appropriate data type indicated by the &#x60;propertyTypeId&#x60;. | 
**append** | **bool** | Indicates if the &#x60;values&#x60; should be appended to the existing data or overwrite the existing data for the specified &#x60;runsIds&#x60;, &#x60;runGroupId&#x60;, or &#x60;activityId&#x60;.  (Note: It does not apply to immutable properties.  Immutable properties will always be replaced). Default value is &#x60;false&#x60;. Append cannot be used when specifying an eventGroupId.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

