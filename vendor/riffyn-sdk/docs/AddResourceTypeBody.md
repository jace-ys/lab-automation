# AddResourceTypeBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type_id** | **str** | The &#x60;_id&#x60; of the resource type being added to the activity input or output.  | 
**direction** | **str** | The direction on the activity the resource type is being added to. This will be one of these direction: &#x60;input&#x60;, or &#x60;output&#x60;.  | 
**sample** | **bool** | Creates a pass-through resource by default or if &#x60;sample&#x60; is set to false. If &#x60;true&#x60; marks the resource generated on output as a sample of the resource type, making it a unique resource with a unique generated name and id.  | [optional] 
**set_res_def_id_to** | **str** | Sets the &#x60;resourceDefId&#x60; for the created &#x60;resourceType&#x60; on the step. Must be a valid &#x60;_id&#x60; from the &#x60;input&#x60; or &#x60;output&#x60; of an activity or returned from &#x60;addResourceTypeToExperiment&#x60; endpoint. This allows the &#x60;resourceDefId&#x60; created as an &#x27;ad hoc&#x27; modification on an experiment to be added to the working version of the process. A &#x60;resourceDefId&#x60; must be unique in the process.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

