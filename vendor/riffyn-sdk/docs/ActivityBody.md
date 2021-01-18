# ActivityBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name for the activity being added. If no name is provided, it will default to &#x27;unnamed&#x27;. | [optional] 
**activity_id** | **str** | The &#x60;_id&#x60; of the existing activity which the new activity will be placed in relation to. If the existing activity is within a group, the &#x60;groupId&#x60; must be provided. If no activityId is provided the new activity will be created at the top level of the process. | [optional] 
**location** | **str** | Where the new activity should be placed in relation to the existing activity. Will be one of &#x60;before&#x60; or &#x60;after&#x60;. This field is required if an &#x60;activityId&#x60; is provided. | [optional] 
**resource_def_id** | **str** | The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; of the existing activity. This is the resource type that will be connected to the activity being created. If a resourceDef is defined, the activityId must also be defined. If resourceDefId is undefined, the activity will be created with an unassigned resource type and no connection. | [optional] 
**group_id** | **str** | The &#x60;_id&#x60; of the group for the existing activityId. Required if the existing activity is inside of a group. The created activity will also be included in this group. If the existing activity is at the top level of the process this field is unnecessary.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

