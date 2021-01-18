# RunGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the run group. | [optional] 
**name** | **str** | The name of the item | [optional] 
**description** | **str** | A brief description of this run group. | [optional] 
**experiment_id** | **str** | The unique id of the experiment this run group is associated with. | [optional] 
**activity_id** | **str** | The unique id of the activity (step) this run group is associated with. Refers to the Process level Activity &#x60;_id&#x60;. | [optional] 
**activity_version** | **str** | The version number of the activity this run group was created on. | [optional] 
**num** | **int** | A numeric value, used to represent the sort order of the groups within the activity (step) and experiment. | [optional] 
**label** | **str** | The label for the run group. | [optional] 
**default** | **bool** | Indicates if this is the default run group for the activity and experiment. | [optional] 
**creator** | **str** | The username of the user that created this run group. | [optional] 
**created** | [**Created**](Created.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

