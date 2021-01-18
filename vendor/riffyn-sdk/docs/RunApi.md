# swagger_client.RunApi

All URIs are relative to *https://api.riffyn.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_batch_run_data**](RunApi.md#add_batch_run_data) | **POST** /experiment/{id}/activity/{activityId}/add-batch-run-data | 
[**add_run_data**](RunApi.md#add_run_data) | **POST** /experiment/{id}/activity/{activityId}/add-run-data | 
[**assign_input**](RunApi.md#assign_input) | **POST** /experiment/{id}/assign-input | 
[**connect_runs_along_path**](RunApi.md#connect_runs_along_path) | **POST** /experiment/{id}/connect-runs | 
[**create_run_group**](RunApi.md#create_run_group) | **POST** /experiment/{id}/activity/{activityId}/run-group | 
[**create_runs**](RunApi.md#create_runs) | **POST** /experiment/{id}/add-runs | 
[**delete_run_data**](RunApi.md#delete_run_data) | **DELETE** /v1/experiment/{id}/activity/{activityId}/delete-run-data | 
[**get_run**](RunApi.md#get_run) | **GET** /experiment/{id}/run/{runId} | 
[**list_run_groups**](RunApi.md#list_run_groups) | **GET** /experiment/{id}/run-groups | 
[**list_run_paths**](RunApi.md#list_run_paths) | **GET** /experiment/{id}/run-paths | 
[**list_runs**](RunApi.md#list_runs) | **GET** /experiment/{id}/run-group/{groupId}/runs | 
[**propagate_runs_along_path**](RunApi.md#propagate_runs_along_path) | **POST** /experiment/{id}/propagate-runs | 
[**set_run_overrides**](RunApi.md#set_run_overrides) | **POST** /experiment/{id}/run-overrides/set | 
[**unset_run_overrides**](RunApi.md#unset_run_overrides) | **POST** /experiment/{id}/run-overrides/unset | 
[**update_run**](RunApi.md#update_run) | **PATCH** /experiment/{id}/run/{runId} | 
[**update_run_status**](RunApi.md#update_run_status) | **PUT** /experiment/{id}/run/{runId} | 

# **add_batch_run_data**
> RunDataResponse add_batch_run_data(body, id, activity_id)



Writes values to multiple `propertyTypeId` and `resourceDefId` in one api call. A batch is a set of data objects which conform to the addRunData endpoint format. Each object within the batch array writes data to one `propertyTypeId` within a `resourceDefId` and can specify an `eventGroupId`. Multiple values can be sent for each data object by specifying a list of `eventId` and `value` objects. Data is added to a specific `eventGroupId`, a specific `runGroupId`, or a specific list of `runIds`. One of `runGroupId`, or `runIds` must be included in the request. Define the correct runId When using `eventGroupId`. Use `append` unless previously entered data is to be overwritten. Each element of batch data may be entered in a different order than in the request. To set values to one `propertyTypeId`, `resourceDefId`, and `eventGroupId` use `addRunData` endpoint. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddBatchDataToInputBody() # AddBatchDataToInputBody | A JSON object containing the batchData composed of a list of JSON objects with the necessary properties to add data.
id = 'id_example' # str | The `_id` of the experiment to manage the data to.
activity_id = 'activity_id_example' # str | The `_id` of activity (step) to add the data to. Refers to the Process Activity `_id` from the `listActivities` endpoint. When using the `listExperimentActivities` endpoint, use the `objectId`.

try:
    api_response = api_instance.add_batch_run_data(body, id, activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->add_batch_run_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddBatchDataToInputBody**](AddBatchDataToInputBody.md)| A JSON object containing the batchData composed of a list of JSON objects with the necessary properties to add data. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment to manage the data to. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of activity (step) to add the data to. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. When using the &#x60;listExperimentActivities&#x60; endpoint, use the &#x60;objectId&#x60;. | 

### Return type

[**RunDataResponse**](RunDataResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_run_data**
> RunDataResponse add_run_data(body, id, activity_id)



Write values to one `propertyTypeId` within a `resourceDefId`. Multiple values can be sent by specifying a list of `eventId` and `value` objects. Data is added to a specific `eventGroupId`, a specific list of `runIds`, or a `runGroupId`. One of `runGroupId`, or `runIds` must be included in the request. Define only the correct runId when using `eventGroupId`. Use `append` unless previously entered data is to be overwritten. To set values to multiple `propertyTypeId`, `resourceDefId`, and `eventGroupId` use `batchAddRunData` endpoint. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddDataToInputBody() # AddDataToInputBody | A JSON object containing the necessary properties to add data.
id = 'id_example' # str | The `_id` of the experiment to manage the data to.
activity_id = 'activity_id_example' # str | The `_id` of activity (step) to add the data to. Refers to the Process Activity `_id` from the `listActivities` endpoint. When using the `listExperimentActivities` endpoint, use the `objectId`.

try:
    api_response = api_instance.add_run_data(body, id, activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->add_run_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddDataToInputBody**](AddDataToInputBody.md)| A JSON object containing the necessary properties to add data. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment to manage the data to. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of activity (step) to add the data to. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. When using the &#x60;listExperimentActivities&#x60; endpoint, use the &#x60;objectId&#x60;. | 

### Return type

[**RunDataResponse**](RunDataResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_input**
> Run assign_input(body, id)



Assigns a resource to a single input ( or `resourceDef` ) by `name` or by `resourceId`. Can be assigned to all runs for an activity (step) or for specific runs defined by an array of `runIds`. The `activityId` refers to the Process level activity `_id`. You must define either an `activityId` or an array of `runIds`, but not both. If you are adding a resource by `name` define only `runIds`. You can define a resource by `name` that does not have a `resourceId` in the resource inventory. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetResourceBody() # SetResourceBody | A JSON object containing the necessary properties to assign the resource.
id = 'id_example' # str | The `_id` of the experiment.

try:
    api_response = api_instance.assign_input(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->assign_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetResourceBody**](SetResourceBody.md)| A JSON object containing the necessary properties to assign the resource. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 

### Return type

[**Run**](Run.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_runs_along_path**
> SuccessMessage connect_runs_along_path(body, id)



Connects runs, along a path, between two activities (steps) of an experiment. Connection will result in propagated runs on the activities included in the path. Define the activity id where the runs should split. To connect a run to multiple runs repeat run connection pattern accordingly: `upstreamRunIds: [runA, runB]` `downstreamRunIds: [run1, run2, run1, run2]` `ratio: [1,2]` results in runA being connected to run1 and run2 and runB will also be connected to run1 and run2.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectRunsAlongPathBody() # ConnectRunsAlongPathBody | 
id = 'id_example' # str | The `_id` of the experiment.

try:
    api_response = api_instance.connect_runs_along_path(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->connect_runs_along_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectRunsAlongPathBody**](ConnectRunsAlongPathBody.md)|  | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_run_group**
> RunGroup create_run_group(body, id, activity_id)



Create a new run group for a specific activity in an experiment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
body = swagger_client.NewRunGroupBody() # NewRunGroupBody | A JSON object containing the necessary properties to create a new run. group
id = 'id_example' # str | The `_id` of the experiment to create the run group.
activity_id = 'activity_id_example' # str | The `_id` of activity (step) to add the data to. Refers to the Process Activity `_id` from the `listActivities` endpoint. When using the `listExperimentActivities` endpoint, use the `objectId`.

try:
    api_response = api_instance.create_run_group(body, id, activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->create_run_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewRunGroupBody**](NewRunGroupBody.md)| A JSON object containing the necessary properties to create a new run. group | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment to create the run group. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of activity (step) to add the data to. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. When using the &#x60;listExperimentActivities&#x60; endpoint, use the &#x60;objectId&#x60;. | 

### Return type

[**RunGroup**](RunGroup.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_runs**
> Runs create_runs(body, id)



Creates new runs for a specific activity, or run group, in an experiment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
body = swagger_client.NewRunsBody() # NewRunsBody | A JSON object containing the necessary properties to create new runs.
id = 'id_example' # str | The `_id` of the experiment.

try:
    api_response = api_instance.create_runs(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->create_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewRunsBody**](NewRunsBody.md)| A JSON object containing the necessary properties to create new runs. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 

### Return type

[**Runs**](Runs.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_run_data**
> SuccessfullyDelete delete_run_data(body, id, activity_id)



Deletes values to one `propertyTypeId` within a `resourceDefId`. Data is deleted from a list of `runIds` and can specify `eventGroupId`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
body = NULL # object | A JSON object containing the necessary properties to remove data
id = 'id_example' # str | The `_id` of the experiment to manage the data to.
activity_id = 'activity_id_example' # str | The `_id` of activity (step) to add the data to. Refers to the Process Activity `_id` from the `listActivities` endpoint. When using the `listExperimentActivities` endpoint, use the `objectId`.

try:
    api_response = api_instance.delete_run_data(body, id, activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->delete_run_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| A JSON object containing the necessary properties to remove data | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment to manage the data to. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of activity (step) to add the data to. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. When using the &#x60;listExperimentActivities&#x60; endpoint, use the &#x60;objectId&#x60;. | 

### Return type

[**SuccessfullyDelete**](SuccessfullyDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run**
> Run get_run(id, run_id)



Get a specific run for an experiment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
run_id = 'run_id_example' # str | The `_id` of the run.

try:
    api_response = api_instance.get_run(id, run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **run_id** | **str**| The &#x60;_id&#x60; of the run. | 

### Return type

[**Run**](Run.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_run_groups**
> RunGroups list_run_groups(id, sort=sort, activity_id=activity_id, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator)



List or search the run groups for a specific experiment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
sort = ['sort_example'] # list[str] | The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (`-`). A comma separated list may be used to sort by more than one field (e.g. `name,-label`).  (optional)
activity_id = 'activity_id_example' # str | Limits the result set to items associated with the `_id` of the specified activity. Refers to the Process level Activity `_id`. (optional)
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)
name = 'name_example' # str | Limits the result set to items with this exact name (case insensitive). (optional)
creator = 'creator_example' # str | Limits the result set to items created by the user with this username. (optional)

try:
    api_response = api_instance.list_run_groups(id, sort=sort, activity_id=activity_id, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->list_run_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **sort** | [**list[str]**](str.md)| The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (&#x60;-&#x60;). A comma separated list may be used to sort by more than one field (e.g. &#x60;name,-label&#x60;).  | [optional] 
 **activity_id** | **str**| Limits the result set to items associated with the &#x60;_id&#x60; of the specified activity. Refers to the Process level Activity &#x60;_id&#x60;. | [optional] 
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 
 **before** | **str**| Limits the result set to items created on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  | [optional] 
 **after** | **str**| Limits the result set to items created on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;).  | [optional] 
 **fields** | **str**| Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use &#x60;fields&#x3D;name,created&#x60;. To exclude the name and created fields from the results use &#x60;fields&#x3D;-name,-created&#x60;. Inclusion and exclusion options can not be set in the same query.  | [optional] 
 **name** | **str**| Limits the result set to items with this exact name (case insensitive). | [optional] 
 **creator** | **str**| Limits the result set to items created by the user with this username. | [optional] 

### Return type

[**RunGroups**](RunGroups.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_run_paths**
> RunPaths list_run_paths(id, start, end)



Returns an array of potential run paths between two activities. If there are no possible paths between the `start` and `end` activities (steps), an empty array will be returned. Requires a path query: `?start={startActivityId}&end={endActivityId}`. The results of this query can be used to propagate runs down a specific path, using a specific `activitiesOrder` array. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
start = 'start_example' # str | The `_id` of the starting process activity (step). This refers to the Process level activity `_id` (`listActivities` endpoint), use `objectId` when using the `listExperimentActivities` endpoint.
end = 'end_example' # str | The `_id` of the ending process activity (step). This refers to the Process level activity `_id` (`listActivities` endpoint), use `objectId` when using the `listExperimentActivities` endpoint.

try:
    api_response = api_instance.list_run_paths(id, start, end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->list_run_paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **start** | **str**| The &#x60;_id&#x60; of the starting process activity (step). This refers to the Process level activity &#x60;_id&#x60; (&#x60;listActivities&#x60; endpoint), use &#x60;objectId&#x60; when using the &#x60;listExperimentActivities&#x60; endpoint. | 
 **end** | **str**| The &#x60;_id&#x60; of the ending process activity (step). This refers to the Process level activity &#x60;_id&#x60; (&#x60;listActivities&#x60; endpoint), use &#x60;objectId&#x60; when using the &#x60;listExperimentActivities&#x60; endpoint. | 

### Return type

[**RunPaths**](RunPaths.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_runs**
> Runs list_runs(id, group_id, sort=sort, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator, modified_before=modified_before, modified_after=modified_after)



List or search the runs for a specific experiment and run group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
group_id = 'group_id_example' # str | The `_id` of the run group, for the specified experiment.
sort = ['sort_example'] # list[str] | The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (`-`). A comma separated list may be used to sort by more than one field (e.g. `process_name,-label`).  (optional)
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)
name = 'name_example' # str | Limits the result set to items with this exact name (case insensitive). (optional)
creator = 'creator_example' # str | Limits the result set to items created by the user with this username. (optional)
modified_before = 'modified_before_example' # str | Limits the result set to items modified on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch, `1507650828`).  (optional)
modified_after = 'modified_after_example' # str | Limits the result set to items modified on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch, `1507650828`).  (optional)

try:
    api_response = api_instance.list_runs(id, group_id, sort=sort, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator, modified_before=modified_before, modified_after=modified_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->list_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **group_id** | **str**| The &#x60;_id&#x60; of the run group, for the specified experiment. | 
 **sort** | [**list[str]**](str.md)| The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (&#x60;-&#x60;). A comma separated list may be used to sort by more than one field (e.g. &#x60;process_name,-label&#x60;).  | [optional] 
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 
 **before** | **str**| Limits the result set to items created on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  | [optional] 
 **after** | **str**| Limits the result set to items created on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;).  | [optional] 
 **fields** | **str**| Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use &#x60;fields&#x3D;name,created&#x60;. To exclude the name and created fields from the results use &#x60;fields&#x3D;-name,-created&#x60;. Inclusion and exclusion options can not be set in the same query.  | [optional] 
 **name** | **str**| Limits the result set to items with this exact name (case insensitive). | [optional] 
 **creator** | **str**| Limits the result set to items created by the user with this username. | [optional] 
 **modified_before** | **str**| Limits the result set to items modified on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60; or epoch, &#x60;1507650828&#x60;).  | [optional] 
 **modified_after** | **str**| Limits the result set to items modified on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60; or epoch, &#x60;1507650828&#x60;).  | [optional] 

### Return type

[**Runs**](Runs.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **propagate_runs_along_path**
> Run propagate_runs_along_path(body, id)



Propagates runs, along a path, between two activities (steps) of an experiment. Before you can call this endpoint, you must first obtain the list of run paths from the `/experiment/{id}/run-paths` endpoint, and decide which path you want to use. The response will be a the list of runs generated in the `downstreamRunGroupId`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
body = swagger_client.PropagateRunsBody() # PropagateRunsBody | 
id = 'id_example' # str | The `_id` of the experiment.

try:
    api_response = api_instance.propagate_runs_along_path(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->propagate_runs_along_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PropagateRunsBody**](PropagateRunsBody.md)|  | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 

### Return type

[**Run**](Run.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_run_overrides**
> SuccessMessage set_run_overrides(body, id)



Sets `overrideMap` values for one or more properties in either a list of runs, or an entire activity (step).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetRunOverridesBody() # SetRunOverridesBody | 
id = 'id_example' # str | The `_id` of the experiment.

try:
    api_response = api_instance.set_run_overrides(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->set_run_overrides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetRunOverridesBody**](SetRunOverridesBody.md)|  | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_run_overrides**
> SuccessMessage unset_run_overrides(body, id)



Unsets a single `overrideMap` key, for either a list of runs, or an entire activity (step).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
body = swagger_client.UnsetRunOverridesBody() # UnsetRunOverridesBody | The `_id` of the experiment.
id = 'id_example' # str | The `_id` of the experiment.

try:
    api_response = api_instance.unset_run_overrides(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->unset_run_overrides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnsetRunOverridesBody**](UnsetRunOverridesBody.md)| The &#x60;_id&#x60; of the experiment. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_run**
> Run update_run(id, run_id, body=body)



Update the name, description or type of a run for a specific experiment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
run_id = 'run_id_example' # str | The `_id` of the run to be updated.
body = swagger_client.UpdateRunBody() # UpdateRunBody | A JSON object containing the properties of the run you would like to update. (optional)

try:
    api_response = api_instance.update_run(id, run_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->update_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **run_id** | **str**| The &#x60;_id&#x60; of the run to be updated. | 
 **body** | [**UpdateRunBody**](UpdateRunBody.md)| A JSON object containing the properties of the run you would like to update. | [optional] 

### Return type

[**Run**](Run.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_run_status**
> RunStatus update_run_status(id, run_id, body=body)



Update the status of a run for a specific experiment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RunApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
run_id = 'run_id_example' # str | The `_id` of the run to be updated.
body = swagger_client.UpdateRunStatusBody() # UpdateRunStatusBody | A JSON object containing the properties of the run you would like to update. (optional)

try:
    api_response = api_instance.update_run_status(id, run_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->update_run_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **run_id** | **str**| The &#x60;_id&#x60; of the run to be updated. | 
 **body** | [**UpdateRunStatusBody**](UpdateRunStatusBody.md)| A JSON object containing the properties of the run you would like to update. | [optional] 

### Return type

[**RunStatus**](RunStatus.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

