# Activity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the activity (step), or experiment activity. When using experiment activities, use the &#x60;objectId&#x60;. | [optional] 
**name** | **str** | The name of the item. | [optional] 
**description** | **str** | A description of what happens happens during this activity. | [optional] 
**adhoc_items** | **object** | An object containing the &#x60;key&#x60; values from all PropertyDefs, ResourceDefs, and Components that are marked as &#x60;adhoc&#x60; example: {u3cy94rmwFFeCzoad | GytGXYEZqAPMKnM55}  | [optional] 
**inputs** | [**list[ResourceDef]**](ResourceDef.md) |  | [optional] 
**outputs** | [**list[ResourceDef]**](ResourceDef.md) |  | [optional] 
**instructions** | **list[str]** | Any instructions that would be helpful to the operator at experiment run time. | [optional] 
**default_number_of_runs** | **str** |  | [optional] 
**top_group_id** | **str** | The &#x60;_id&#x60; of the process that this activity is associated with. | [optional] 
**num** | **int** | A value that represents the \&quot;number\&quot; of this activity. This is value does NOT indicate the order in which the activities (steps) should be processed.  | [optional] 
**run_time** | **int** |  | [optional] 
**shareable** | **bool** | Indicates if the activity can be shared with other users. | [optional] 
**public** | **bool** | Indicates if the activity is visible to all users. | [optional] 
**creator** | **str** | The username of the user that created this activity | [optional] 
**created** | [**Created**](Created.md) |  | [optional] 
**modified** | [**Modified**](Modified.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**object_id** | **str** | The &#x60;_id&#x60; of the corresponding activity on the Process level. Use this value in endpoint paths.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

