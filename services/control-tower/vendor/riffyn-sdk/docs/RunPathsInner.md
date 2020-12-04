# RunPathsInner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities_order** | **list[str]** | The \&quot;path\&quot; from a start activity (step) to an end activity (step), specified as an array of activity &#x60;_id&#x60;s. | [optional] 
**connections_traversed** | [**list[ConnectionLine]**](ConnectionLine.md) | The list of connections between each activity (step) in the path, and the resource &#x60;_id&#x60; and resource type of each connection. | [optional] 
**groups_traversed** | **list[str]** |  | [optional] 
**description** | **str** | A description of the path, from start to end, including each branch along the path. | [optional] 
**upstream_name** | **str** | The name of the upstream activity (step). | [optional] 
**downstream_name** | **str** | The name of the downstream activity (step). | [optional] 
**via** | **str** | A string that describes the branch locations within the start and end points of the path | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

