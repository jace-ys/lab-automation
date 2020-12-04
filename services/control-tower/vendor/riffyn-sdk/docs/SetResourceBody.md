# SetResourceBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** | The &#x60;_id&#x60; of the activity (step) that you would like to assign the resource to. Refers to the Process level Activity &#x60;_id&#x60;. Use this option if you want to apply the resource to all runs in an activity for the specified experiment. Use one of &#x60;activityId&#x60; or &#x60;runIds&#x60;, they are mutually exclusive. | 
**run_ids** | **list[str]** | The array of &#x60;_id&#x60;s from the runs you would like to assign the resource to. Use this option if you want to assign the resource to a subset of runs. Use one of &#x60;activityId&#x60; or &#x60;runIds&#x60;, they are mutually exclusive. | 
**resource_def_id** | **str** | The &#x60;_id&#x60; of the input resource type from the &#x60;inputs&#x60; array from the &#x60;listExperimentActivities&#x60; endpoint. Defines the specific use of the resource in an experiment. | 
**resource_id** | **str** | The &#x60;_id&#x60; of the resource inventory item you would like to assign. Define either a &#x60;name&#x60; or a &#x60;resourceId&#x60;.  | 
**name** | **str** | The &#x60;name&#x60; of the resource you would like to assign. If the &#x60;name&#x60; does not correspond to a unique resource from the resource library it will define a place holder with no &#x60;resourceId&#x60;. Use only &#x60;runIds&#x60; when using &#x60;name&#x60;. Define either a &#x60;name&#x60; or a &#x60;resourceId&#x60;. | 
**type_id** | **str** | The &#x60;resourceType&#x60; for the resource being assigned. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

