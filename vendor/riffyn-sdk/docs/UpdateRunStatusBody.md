# UpdateRunStatusBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the run to be updated. Must be one of: &#x60;start run&#x60;, &#x60;stop run&#x60;, &#x60;completed&#x60;, &#x60;reset&#x60;, &#x60;restart&#x60;. | [optional] 
**_date** | **datetime** | The date-time for the status of the run being updated. The specified value can be either an Epoch timestamp (number of seconds since 1970-01-01), or an ISO date string. If not provided, will default to current date and time. Example:  &#x27;ISO: 2016-01-01T12:31:23.456Z or epoch: 1510879105&#x27;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

