# UnsetRunOverridesBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_ids** | **list[str]** | If specified, the &#x60;overrideKey&#x60; will be removed from all runs contained in the list of &#x60;runIds&#x60;. If an &#x60;activityId&#x60; is also specified, this list will be ignored.  | [optional] 
**activity_id** | **str** | If specified, the &#x60;overrideKey&#x60; will be removed from all runs in the activity. | [optional] 
**override_key** | **object** | A string representing a key from the &#x60;overridesMap&#x60; that you want to remove, in the format of &#x60;activityId | resourceDefId | componentId | propertyTypeId&#x60;.  example:  {   \&quot;RS2vW87PNg33T4HTQ |EnGj979ADGJJZSPMF | null | concentration\&quot;: \&quot;1\&quot; }  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

