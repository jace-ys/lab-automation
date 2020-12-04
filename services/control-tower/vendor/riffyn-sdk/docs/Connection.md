# Connection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_id** | **str** | The &#x60;_id&#x60; of the activity or group where the connection originates from. | 
**from_type** | **str** | The &#x60;type&#x60; is either &#x60;activity&#x60; or &#x60;group&#x60; for the entity being connected. | 
**from_res_def_id** | **str** | A &#x60;from&#x60; resourceDefId is the &#x60;_id&#x60; of one of the &#x60;outputs&#x60; of the process activity (step) that identifies the resource type being connected. The resourceDefId for a group must first be exported from the activity where the resource exists. | 
**to_id** | **str** | The &#x60;_id&#x60; of the activity or group where the connection is directed to. | 
**to_type** | **str** | The &#x60;type&#x60; is either &#x60;activity&#x60; or &#x60;group&#x60; for the entity being connected. | 
**to_res_def_id** | **str** | A &#x60;to&#x60; resourceDefId is the _id of one of the &#x60;inputs&#x60; of the process activity (step) that identifies the resource type being connected. The resourceDefId for a group must first be imported from the inner activity where the resource exists.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

