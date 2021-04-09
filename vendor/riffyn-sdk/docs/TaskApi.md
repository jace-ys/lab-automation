# riffyn_nexus_sdk_v1.TaskApi

All URIs are relative to *deployment_url/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task**](TaskApi.md#get_task) | **GET** /task/{id} | getTask
[**list_tasks**](TaskApi.md#list_tasks) | **GET** /tasks | listTasks

# **get_task**
> Task get_task(id)

getTask

Returns the details for the specified task of the exported experiment.

### Example
```python
from __future__ import print_function
import time
import riffyn_nexus_sdk_v1
from riffyn_nexus_sdk_v1.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = riffyn_nexus_sdk_v1.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = riffyn_nexus_sdk_v1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = riffyn_nexus_sdk_v1.TaskApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the task.

try:
    # getTask
    api_response = api_instance.get_task(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the task. | 

### Return type

[**Task**](Task.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks**
> InlineResponse20019 list_tasks(stale=stale, state=state, file_type=file_type, limit=limit, offset=offset, created_on=created_on, modified_before=modified_before, modified_after=modified_after, before=before, after=after)

listTasks

List of experiment tasks.

### Example
```python
from __future__ import print_function
import time
import riffyn_nexus_sdk_v1
from riffyn_nexus_sdk_v1.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = riffyn_nexus_sdk_v1.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = riffyn_nexus_sdk_v1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = riffyn_nexus_sdk_v1.TaskApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
stale = true # bool | Limits the records returned to the ones that are stale e.g. stale=true  (optional)
state = 'state_example' # str | Limits the records returned to the ones that are in a specific state. Will be one of: `new`, `initializing`, `initialized`, `wip`, `success`, or `failed`.  (optional)
file_type = 'file_type_example' # str | The desired data format type (defaults to `text/csv`) to be given to downloadable file. Can be one of `text/csv`, `binary/parquet`. (optional)
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
created_on = 'created_on_example' # str | Limits the result set to items created on the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch in milliseconds, `1507650828998`).  (optional)
modified_before = 'modified_before_example' # str | Limits the result set to items modified on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch, `1507650828`).  (optional)
modified_after = 'modified_after_example' # str | Limits the result set to items modified on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch, `1507650828`).  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)

try:
    # listTasks
    api_response = api_instance.list_tasks(stale=stale, state=state, file_type=file_type, limit=limit, offset=offset, created_on=created_on, modified_before=modified_before, modified_after=modified_after, before=before, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->list_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stale** | **bool**| Limits the records returned to the ones that are stale e.g. stale&#x3D;true  | [optional] 
 **state** | **str**| Limits the records returned to the ones that are in a specific state. Will be one of: &#x60;new&#x60;, &#x60;initializing&#x60;, &#x60;initialized&#x60;, &#x60;wip&#x60;, &#x60;success&#x60;, or &#x60;failed&#x60;.  | [optional] 
 **file_type** | **str**| The desired data format type (defaults to &#x60;text/csv&#x60;) to be given to downloadable file. Can be one of &#x60;text/csv&#x60;, &#x60;binary/parquet&#x60;. | [optional] 
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 
 **created_on** | **str**| Limits the result set to items created on the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60; or epoch in milliseconds, &#x60;1507650828998&#x60;).  | [optional] 
 **modified_before** | **str**| Limits the result set to items modified on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60; or epoch, &#x60;1507650828&#x60;).  | [optional] 
 **modified_after** | **str**| Limits the result set to items modified on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60; or epoch, &#x60;1507650828&#x60;).  | [optional] 
 **before** | **str**| Limits the result set to items created on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  | [optional] 
 **after** | **str**| Limits the result set to items created on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;).  | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

