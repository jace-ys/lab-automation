# Resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **str** | The &#x60;_id&#x60; of the ResourceType for this resource. | [optional] 
**type_name** | **str** | The &#x60;name&#x60; of the ResourceType for this resource. | [optional] 
**id** | **str** | The unique id of the resource. | [optional] 
**name** | **str** | The name of the item. | [optional] 
**label** | **str** | The label for this resource, typically in the format of &#x60;GR-&#x60; or &#x60;IR-&#x60; followed by the resource&#x27;s &#x60;_id&#x60;. | [optional] 
**description** | **str** | A description of what the resource is, or where this resource was created. | [optional] 
**experiment_id** | **str** | The &#x60;_id&#x60; of the Experiment where this resource was created. | [optional] 
**experiment_name** | **str** | The name of the Experiment where this resource was created. | [optional] 
**top_group_id** | **str** | The unique id of the process | [optional] 
**top_group_name** | **str** | The name of the process | [optional] 
**activity_id** | **str** | The &#x60;_id&#x60; of the activity (step). | [optional] 
**activity_name** | **str** | The name of the activity (step). | [optional] 
**run_id** | **str** | The &#x60;_id&#x60; of the Run where this resource was created. | [optional] 
**run_label** | **str** | A label that includes the activity id, experiment number, step number, and run number for this resource. | [optional] 
**genealogy** | **object** |  | [optional] 
**components** | [**list[ResourcesComponents]**](ResourcesComponents.md) | A list of components and their fixed properties for this resource. | [optional] 
**sharable** | **bool** | Indicates if the resource can be shared with other users. | [optional] 
**accessible_to** | [**AccessibleTo**](AccessibleTo.md) |  | [optional] 
**public** | **bool** | Indicates if the resource is visible to all users. | [optional] 
**permissions** | **int** | The permission level of the entity. | [optional] 
**creator** | **str** | The &#x60;username&#x60; of the user that created this resource. | [optional] 
**created** | [**Created**](Created.md) |  | [optional] 
**org** | [**Org**](Org.md) |  | [optional] 
**modified** | **datetime** | The last modified date of the resource. | [optional] 
**modified_by** | [**ModifiedBy**](ModifiedBy.md) |  | [optional] 
**properties** | [**list[ResourcesProperties]**](ResourcesProperties.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

