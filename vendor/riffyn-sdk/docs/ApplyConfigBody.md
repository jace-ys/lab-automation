# ApplyConfigBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | The &#x60;_id&#x60; of the upload configuration being applied to the dataFile from &#x60;/v1/process/:id/upload-configs&#x60;. | 
**data_file_id** | **str** | The &#x60;_id&#x60; of the dataFile uploaded to &#x60;v1/experiment/:id/activity/:id/upload&#x60;. | 
**timezone** | **str** | Valid time zone such as &#x60;America/Los_Angeles&#x60;. | 
**group_id** | **str** | The &#x60;_id&#x60; of the run group the data will be added to. | [optional] 
**manual_data** | [**list[ApplyConfigBodyManualData]**](ApplyConfigBodyManualData.md) | The values for the manually set data fields in the upload configuration. The information for the manual data can be found at &#x60;v1/process/{id}/upload-config/{uploadConfigId}&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

