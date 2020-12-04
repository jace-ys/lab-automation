# Run

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the run | [optional] 
**name** | **str** | The name of the item | [optional] 
**description** | **str** | A brief description of the run | [optional] 
**activity_id** | **str** | The activity (step) ID this run is associated with. Refers to the Process level Activity &#x60;_id&#x60;. | [optional] 
**activity_version** | **str** | The version of the activity (step) this run is associated with | [optional] 
**experiment_id** | **str** | The experiment ID this run is associated with | [optional] 
**group_id** | **str** | The run group ID this run is associated with | [optional] 
**overrides_map** | **object** | An object that assigns an override value to property for this run. The keys for this object are a hash of &#x60;activityId | resourceDefId | componentId | propertyTypeId&#x60;, and the value for the object is the value you want to assign for the property specified in the hash  example  {   \&quot;RS2vW87PNg33T4HTQ |EnGj979ADGJJZSPMF | null | concentration\&quot;: \&quot;1\&quot; }  | [optional] 
**status** | **str** | The status of the run. Possible values are &#x60;new&#x60;, &#x60;running&#x60;, &#x60;stopped&#x60;, &#x60;completed&#x60;, &#x60;deleted&#x60; | [optional] 
**inputs** | [**list[RunResourceDef]**](RunResourceDef.md) | A list of input resources for the run | [optional] 
**outputs** | [**list[RunResourceDef]**](RunResourceDef.md) | A list of output resources for the run | [optional] 
**type** | **str** | The type of this run. Allowed values are &#x60;blank&#x60;, &#x60;calibration&#x60;, &#x60;reference&#x60;, &#x60;sample&#x60;, &#x60;standard&#x60;, &#x60;trial&#x60; | [optional] 
**num** | **int** | A numerical representation of the run number. Can be used for sorting. | [optional] 
**propagated_from_runs** | **list[str]** | The list of upstream runs that feed resources into this run. | [optional] 
**creator** | **str** | The username of the user that created this run group | [optional] 
**created** | [**Created**](Created.md) |  | [optional] 
**label** | **str** |  | [optional] 
**modified** | **datetime** | The last modified date of the run. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

