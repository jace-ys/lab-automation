# SetRunOverridesBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_ids** | **list[str]** | If specified, the overrides will be applied to all runs contained in the list of &#x60;runIds&#x60;. You may only specify either &#x60;runIds&#x60; or &#x60;activityId&#x60;, but not both. Any error will be returned if both are specified.  | [optional] 
**activity_id** | **str** | If specified, the overrides will be applied to all runs in the activity. You may only specify either &#x60;runIds&#x60; or &#x60;activityId&#x60;, but not both. Any error will be returned if both are specified. Refers to the Process level Activity &#x60;_id&#x60;.  | [optional] 
**overrides** | **object** | overrides keys must be in the format of &#x60;activityId | resourceDefId | componentId | propertyTypeId&#x60;. The value can be type specific or a string. The value will be parsed based on the data type of the property type of the override. If you are not specifying a componentId, use the string &#x60;null&#x60; in place of the &#x60;componentId&#x60;.  example:  &#x60;&#x60;&#x60; {   \&quot;RS2vW87PNg33T4HTQ |EnGj979ADGJJZSPMF | null | concentration\&quot;: \&quot;1\&quot; } &#x60;&#x60;&#x60;  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

