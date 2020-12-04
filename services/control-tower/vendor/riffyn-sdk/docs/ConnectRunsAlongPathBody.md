# ConnectRunsAlongPathBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upstream_run_ids** | **list[str]** | An array of run &#x60;_id&#x60;s from which you want to start the connection. These &#x60;_id&#x60;s must be from the first step in the &#x60;path&#x60; of activities. &#x60;upstreamRunIds&#x60; must be from the same &#x60;runGroup&#x60;. | [optional] 
**downstream_run_ids** | **list[str]** | An array of run &#x60;_id&#x60;s to which you want to connect. These &#x60;_id&#x60;s must be from the last step of the &#x60;path&#x60; of activities.&#x60;downstreamRunIds&#x60; must be from the same &#x60;runGroup&#x60;. | [optional] 
**path** | **list[str]** | A valid &#x60;activitiesOrder&#x60; array from one of the &#x60;v1/experiment/{id}/run-paths?start&#x3D;{startActivityId}&amp;end&#x3D;{endActivityId}&#x60; response items. This is an array of all the activity &#x60;_id&#x60;s, in step order, for the connecting runs. Refers to the process &#x60;activityId&#x60;. When using the experiment activities, use &#x60;objectId&#x60;. | [optional] 
**split_after** | **str** | The &#x60;activityId&#x60; after which the split should happen. Must be a valid &#x60;activityId&#x60; from the path array. | [optional] 
**ratio** | **list[int]** | The ratio of upstreamRunIds to downstreamRunIds such as [ 1, 2 ]. One of the integers must be a 1. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

