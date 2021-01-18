# NewRunsBodyOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The run group in which you would like to create the runs. &#x60;groupId&#x60; and &#x60;activityId&#x60; are mutually exclusive | [optional] 
**activity_id** | **str** | The _id of the activity (step) in which you would like to create the runs. Since no particular run group is specified, in this case, the new runs will be added to the default run group. &#x60;groupId&#x60; and &#x60;activityId&#x60; are mutually exclusive | [optional] 
**activity_version** | **str** | The &#x60;version.label&#x60; of the activity you are adding runs to. An incorrect value will result in an error | [optional] 
**type** | **str** | Allowed values are &#x60;blank&#x60;, &#x60;calibration&#x60;, &#x60;reference&#x60;, &#x60;sample&#x60;, &#x60;standard&#x60;, &#x60;trial&#x60; | [optional] 
**tags** | **list[str]** | A simple string array of tags to assign to the newly created runs | [optional] 
**intended_start** | **datetime** | The intended start date-time of these runs. The specified value can be either an Epoch timestamp (number of seconds since 1970-01-01), or an ISO date string. | [optional] 
**intended_stop** | **datetime** | The intended stop date-time of these runs. The specified value can be either an Epoch timestamp (number of seconds since 1970-01-01), or an ISO date string. Example: ISO: 2016-01-01T12:31:23.456Z or epoch: 1510879105. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

