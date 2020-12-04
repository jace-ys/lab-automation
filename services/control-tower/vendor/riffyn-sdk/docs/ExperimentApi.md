# swagger_client.ExperimentApi

All URIs are relative to *https://api.riffyn.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_comment_to_experiment**](ExperimentApi.md#add_comment_to_experiment) | **POST** /experiment/{id}/comment | 
[**add_component_to_resource_type**](ExperimentApi.md#add_component_to_resource_type) | **POST** /experiment/{id}/activity/{activityId}/resource-type/{resourceDefId}/component | 
[**add_property_type_to_experiment**](ExperimentApi.md#add_property_type_to_experiment) | **POST** /experiment/{id}/activity/{activityId}/resource-type/{resourceDefId}/property-type | 
[**add_resource_type_to_experiment**](ExperimentApi.md#add_resource_type_to_experiment) | **POST** /experiment/{id}/activity/{activityId}/resource-type | 
[**add_summary_to_experiment**](ExperimentApi.md#add_summary_to_experiment) | **POST** /experiment/{id}/summary | 
[**add_tag_to_experiment**](ExperimentApi.md#add_tag_to_experiment) | **POST** /experiment/{id}/tag | 
[**apply_upload_config**](ExperimentApi.md#apply_upload_config) | **PUT** /experiment/{id}/activity/{activityId}/apply-config | 
[**apply_upload_config_collection**](ExperimentApi.md#apply_upload_config_collection) | **PUT** /experiment/{id}/apply-config-collection | 
[**clone_experiment**](ExperimentApi.md#clone_experiment) | **POST** /experiment/{id}/clone | 
[**create_experiment**](ExperimentApi.md#create_experiment) | **POST** /experiment | 
[**delete_component_from_resource_type**](ExperimentApi.md#delete_component_from_resource_type) | **DELETE** /experiment/{id}/activity/{activityId}/resource-type/{resourceDefId}/component/{componentId} | 
[**delete_experiment**](ExperimentApi.md#delete_experiment) | **DELETE** /experiment/{id} | 
[**delete_experiment_comment**](ExperimentApi.md#delete_experiment_comment) | **DELETE** /experiment/{id}/comment/{commentId} | 
[**delete_experiment_summary**](ExperimentApi.md#delete_experiment_summary) | **DELETE** /experiment/{id}/summary/{summaryId} | 
[**delete_property_type_from_experiment**](ExperimentApi.md#delete_property_type_from_experiment) | **DELETE** /experiment/{id}/activity/{activityId}/resource-type/{resourceDefId}/property-type/{propertyTypeId} | 
[**delete_resource_type_from_experiment**](ExperimentApi.md#delete_resource_type_from_experiment) | **DELETE** /experiment/{id}/activity/{activityId}/resource-type/{resourceDefId} | 
[**delete_tag_from_experiment**](ExperimentApi.md#delete_tag_from_experiment) | **DELETE** /experiment/{id}/tag/{tagId} | 
[**export_experiment_data**](ExperimentApi.md#export_experiment_data) | **PUT** /experiment/{id}/export/data | 
[**export_experiment_data_status**](ExperimentApi.md#export_experiment_data_status) | **GET** /experiment/{id}/export/data/status | 
[**get_experiment**](ExperimentApi.md#get_experiment) | **GET** /experiment/{id} | 
[**get_experiment_comment**](ExperimentApi.md#get_experiment_comment) | **GET** /experiment/{id}/comment/{commentId} | 
[**get_experiment_data_clean**](ExperimentApi.md#get_experiment_data_clean) | **GET** /experiment/{id}/step/{activityId}/data/clean | 
[**get_experiment_data_raw**](ExperimentApi.md#get_experiment_data_raw) | **GET** /experiment/{id}/step/{activityId}/data/raw | 
[**get_experiment_summary**](ExperimentApi.md#get_experiment_summary) | **GET** /experiment/{id}/summary | 
[**get_role_for_experiment**](ExperimentApi.md#get_role_for_experiment) | **GET** /experiment/{id}/role/{userId} | 
[**list_experiment_activities**](ExperimentApi.md#list_experiment_activities) | **GET** /experiment/{id}/activities | 
[**list_experiment_comments**](ExperimentApi.md#list_experiment_comments) | **GET** /experiment/{id}/comments | 
[**list_experiment_tags**](ExperimentApi.md#list_experiment_tags) | **GET** /experiment/{id}/tags | 
[**list_experiments**](ExperimentApi.md#list_experiments) | **GET** /experiments | 
[**list_replies_to_experiment_comment**](ExperimentApi.md#list_replies_to_experiment_comment) | **GET** /experiment/{id}/comment/{commentId}/replies | 
[**reply_to_expriment_comment**](ExperimentApi.md#reply_to_expriment_comment) | **POST** /experiment/{id}/comment/{commentId}/reply | 
[**share_experiment**](ExperimentApi.md#share_experiment) | **POST** /experiment/{id}/accessible-to | 
[**unshare_experiment**](ExperimentApi.md#unshare_experiment) | **PATCH** /experiment/{id}/accessible-to/{principalId} | 
[**update_experiment**](ExperimentApi.md#update_experiment) | **PATCH** /experiment/{id} | 
[**update_experiment_comment**](ExperimentApi.md#update_experiment_comment) | **PATCH** /experiment/{id}/comment/{commentId} | 
[**update_experiment_summary**](ExperimentApi.md#update_experiment_summary) | **PATCH** /experiment/{id}/summary/{summaryId} | 
[**update_property_type_on_experiment**](ExperimentApi.md#update_property_type_on_experiment) | **PATCH** /experiment/{id}/activity/{activityId}/resource-type/{resourceDefId}/property-type/{propertyTypeId} | 
[**update_resource_type_on_experiment**](ExperimentApi.md#update_resource_type_on_experiment) | **PATCH** /experiment/{id}/activity/{activityId}/resource-type/{resourceDefId} | 
[**upload_config_status**](ExperimentApi.md#upload_config_status) | **GET** /experiment/{id}/activity/{activityId}/apply-config/{taskId} | 
[**upload_data_file**](ExperimentApi.md#upload_data_file) | **POST** /experiment/{id}/activity/{activityId}/upload | 

# **add_comment_to_experiment**
> CommentResponse add_comment_to_experiment(body, id)



Adds a comment (or observation) to an experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.CommentBody() # CommentBody | A JSON object containing the options for creating the comment.
id = 'id_example' # str | The `_id` of the experiment you would like to add the comment to.

try:
    api_response = api_instance.add_comment_to_experiment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->add_comment_to_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentBody**](CommentBody.md)| A JSON object containing the options for creating the comment. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment you would like to add the comment to. | 

### Return type

[**CommentResponse**](CommentResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_component_to_resource_type**
> InlineResponse2003 add_component_to_resource_type(body, id, activity_id, resource_def_id)



Ad hoc addition of a component to a resource type on the `input` or `output` of an activity on an experiment. Only ad hoc added components can be deleted from the experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body3() # Body3 | A JSON object containing the options for adding the component.
id = 'id_example' # str | The `_id` of the experiment the component is being added to.
activity_id = 'activity_id_example' # str | The `_id` of the activity the component is being added to. Refers to the Process Activity `_id` from the `listActivities` endpoint.
resource_def_id = 'resource_def_id_example' # str | The `_id` of the `input` or `output` on the activity for the component being added.

try:
    api_response = api_instance.add_component_to_resource_type(body, id, activity_id, resource_def_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->add_component_to_resource_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body3**](Body3.md)| A JSON object containing the options for adding the component. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment the component is being added to. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity the component is being added to. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. | 
 **resource_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; on the activity for the component being added. | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_property_type_to_experiment**
> InlineResponse2005 add_property_type_to_experiment(body, id, activity_id, resource_def_id)



Ad hoc addition of a property type to a resource type on the `input` or `output` of an activity of a experiment. Only ad hoc added property types can be deleted from the experiment. Will be created with default unit for the property type.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body4() # Body4 | A JSON object containing the options for adding the property type.
id = 'id_example' # str | The `_id` of the experiment.
activity_id = 'activity_id_example' # str | The `_id` of the activity. Refers to the Process Activity `_id` from the `listActivities` endpoint.
resource_def_id = 'resource_def_id_example' # str | The `_id` of the `input` or `output` on the activity for the resource type the property type will be added to.

try:
    api_response = api_instance.add_property_type_to_experiment(body, id, activity_id, resource_def_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->add_property_type_to_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body4**](Body4.md)| A JSON object containing the options for adding the property type. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. | 
 **resource_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; on the activity for the resource type the property type will be added to. | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_resource_type_to_experiment**
> InlineResponse200 add_resource_type_to_experiment(body, id, activity_id)



Ad hoc addition of a resource type to the `input` or `output` of an activity on an experiment. Default components and properties of the resource type will be included. Only ad hoc resource types can be deleted from the experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddResourceDefBody() # AddResourceDefBody | A JSON object containing the options for adding the resource type.
id = 'id_example' # str | The `_id` of the experiment to manage the data to.
activity_id = 'activity_id_example' # str | The `_id` of the activity the resource type is being added to. Refers to the Process Activity `_id` from the `listActivities` endpoint.

try:
    api_response = api_instance.add_resource_type_to_experiment(body, id, activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->add_resource_type_to_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddResourceDefBody**](AddResourceDefBody.md)| A JSON object containing the options for adding the resource type. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment to manage the data to. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity the resource type is being added to. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_summary_to_experiment**
> SummaryResponse add_summary_to_experiment(body, id)



Adds a summary and a purpose for the specified experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.SummaryBody() # SummaryBody | A JSON object containing the options for creating the summary.
id = 'id_example' # str | The `_id` of the experiment you would like to add the summary to.

try:
    api_response = api_instance.add_summary_to_experiment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->add_summary_to_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SummaryBody**](SummaryBody.md)| A JSON object containing the options for creating the summary. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment you would like to add the summary to. | 

### Return type

[**SummaryResponse**](SummaryResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tag_to_experiment**
> Tag add_tag_to_experiment(body, id)



Adds a tag to an experiment. If the tag doesn't exist, it will create it and add it to the experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body | A JSON object containing the options for creating the tag.
id = 'id_example' # str | The `_id` of the experiment you would like to add the tag to.

try:
    api_response = api_instance.add_tag_to_experiment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->add_tag_to_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| A JSON object containing the options for creating the tag. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment you would like to add the tag to. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_upload_config**
> ApplyConfigResponse apply_upload_config(body, id, activity_id)



Apply an upload configuration (or parseConfig) to an uploaded dataFile to add data to an activity. Manual data is required if it exists for the upload configuration. Excess manual data is ignored.  To find upload configurations: `/process/:id/upload-configs`.  Retrieve `_id` returned when uploading dataFile:  `/experiment/:id/activity/:activityId/upload`. 

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApplyConfigBody() # ApplyConfigBody | A JSON object containing the ids required for applying the configuration.
id = 'id_example' # str | The `_id` of the experiment to manage the data to.
activity_id = 'activity_id_example' # str | The `_id` of activity (step) to add the data to. Refers to the Process Activity `_id` from the `listActivities` endpoint. When using the `listExperimentActivities` endpoint, use the `objectId`.

try:
    api_response = api_instance.apply_upload_config(body, id, activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->apply_upload_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyConfigBody**](ApplyConfigBody.md)| A JSON object containing the ids required for applying the configuration. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment to manage the data to. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of activity (step) to add the data to. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. When using the &#x60;listExperimentActivities&#x60; endpoint, use the &#x60;objectId&#x60;. | 

### Return type

[**ApplyConfigResponse**](ApplyConfigResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_upload_config_collection**
> ApplyConfigCollectionResponse apply_upload_config_collection(body, id)



Apply an upload configuration (or parseConfig) to an uploaded dataFile to add data to an experiment. A collection will apply all the upload configuration it contains. A collection may contain configurations for more than one activity. Manual data is required for each configuration where it exists. Excess manual data is ignored. 

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApplyConfigCollectionBody() # ApplyConfigCollectionBody | A JSON object containing the ids required for applying the configuration collection.
id = 'id_example' # str | The `_id` of the experiment to manage the data to.

try:
    api_response = api_instance.apply_upload_config_collection(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->apply_upload_config_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyConfigCollectionBody**](ApplyConfigCollectionBody.md)| A JSON object containing the ids required for applying the configuration collection. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment to manage the data to. | 

### Return type

[**ApplyConfigCollectionResponse**](ApplyConfigCollectionResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_experiment**
> Experiment clone_experiment(body, id)



Creates a new experiment, using an existing experiment as a template. Any run groups or runs that are associated. with the source experiment `_id` will also be cloned. Run data will not be cloned. 

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body1() # Body1 | A JSON object containing the options for creating the clone.
id = 'id_example' # str | The `_id` of the experiment you would like to clone.

try:
    api_response = api_instance.clone_experiment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->clone_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)| A JSON object containing the options for creating the clone. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment you would like to clone. | 

### Return type

[**Experiment**](Experiment.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_experiment**
> Experiment create_experiment(body)



Creates a new experiment for a process. Not specifying a `version` value will create the new experiment from the current (working) version of the specified process. 

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.NewExperimentBody() # NewExperimentBody | A JSON object containing the necessary properties to create a new experiment.

try:
    api_response = api_instance.create_experiment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->create_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewExperimentBody**](NewExperimentBody.md)| A JSON object containing the necessary properties to create a new experiment. | 

### Return type

[**Experiment**](Experiment.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_component_from_resource_type**
> InlineResponse2004 delete_component_from_resource_type(id, activity_id, resource_def_id, component_id)



Ad hoc removal of a component on a resource type from the `input` or `output` of an activity on an experiment. Only ad hoc added components can be deleted from the experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment the resource type.
activity_id = 'activity_id_example' # str | The `_id` of the activity the resource type. Refers to the Process Activity `_id` from the `listActivities` endpoint.
resource_def_id = 'resource_def_id_example' # str | The `_id` of the `input` or `output` on the activity for the the resource type.
component_id = 'component_id_example' # str | The resource type `_id` of the component being removed from a resource type on the `input` or `output` on the activity.

try:
    api_response = api_instance.delete_component_from_resource_type(id, activity_id, resource_def_id, component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->delete_component_from_resource_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment the resource type. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity the resource type. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. | 
 **resource_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; on the activity for the the resource type. | 
 **component_id** | **str**| The resource type &#x60;_id&#x60; of the component being removed from a resource type on the &#x60;input&#x60; or &#x60;output&#x60; on the activity. | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_experiment**
> SuccessfullyDelete delete_experiment(id)



Performs a 'soft delete' on an existing experiment. The experiment will still be accessible through the api when searching by `_id` on `getExperiment` endpoint or with the query parameter `deleted` on `listExperiments` endpoint. A deleted experiment will be marked as purged and remain in the database for 7 days. The experiment will then be permanently deleted. 

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.

try:
    api_response = api_instance.delete_experiment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->delete_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 

### Return type

[**SuccessfullyDelete**](SuccessfullyDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_experiment_comment**
> CommentDeleted delete_experiment_comment(id, comment_id)



Deletes the specific comment (or observation) associated with an experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
comment_id = 'comment_id_example' # str | The `_id` of the comment.

try:
    api_response = api_instance.delete_experiment_comment(id, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->delete_experiment_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **comment_id** | **str**| The &#x60;_id&#x60; of the comment. | 

### Return type

[**CommentDeleted**](CommentDeleted.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_experiment_summary**
> SummaryDeleted delete_experiment_summary(id, summary_id)



Deletes the summary and purpose for the specified experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
summary_id = 'summary_id_example' # str | The `_id` of the summary to be removed.

try:
    api_response = api_instance.delete_experiment_summary(id, summary_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->delete_experiment_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **summary_id** | **str**| The &#x60;_id&#x60; of the summary to be removed. | 

### Return type

[**SummaryDeleted**](SummaryDeleted.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property_type_from_experiment**
> SuccessfullyDelete delete_property_type_from_experiment(id, activity_id, resource_def_id, property_type_id)



Performs a 'soft delete' on an existing experiment. The experiment will still be accessible through the api when searching by `_id` on `getExperiment` endpoint or with the query parameter `deleted` on `listExperiments` endpoint. A deleted experiment will be marked as purged and remain in the database for 7 days. The experiment will then be permanently deleted. 

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
activity_id = 'activity_id_example' # str | The `_id` of the activity. Refers to the Process Activity `_id` from the `listActivities` endpoint. When using the `listExperimentActivities` endpoint, use the `objectId`.
resource_def_id = 'resource_def_id_example' # str | The `_id` of the `input` or `output` on the activity for the resource type.
property_type_id = 'property_type_id_example' # str | The `_id` of the property type.

try:
    api_response = api_instance.delete_property_type_from_experiment(id, activity_id, resource_def_id, property_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->delete_property_type_from_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. When using the &#x60;listExperimentActivities&#x60; endpoint, use the &#x60;objectId&#x60;. | 
 **resource_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; on the activity for the resource type. | 
 **property_type_id** | **str**| The &#x60;_id&#x60; of the property type. | 

### Return type

[**SuccessfullyDelete**](SuccessfullyDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_type_from_experiment**
> InlineResponse2001 delete_resource_type_from_experiment(id, activity_id, resource_def_id)



Ad hoc removal of a resource type from the `input` or `output` of an activity on an experiment. Only ad hoc added resource types can be deleted from the experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment the resource type is being deleted from.
activity_id = 'activity_id_example' # str | The `_id` of the activity the resource type is being deleted from. Refers to the Process Activity `_id` from the `listActivities` endpoint.
resource_def_id = 'resource_def_id_example' # str | The `_id` of the `input` or `output` on the activity for the the resource type.

try:
    api_response = api_instance.delete_resource_type_from_experiment(id, activity_id, resource_def_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->delete_resource_type_from_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment the resource type is being deleted from. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity the resource type is being deleted from. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. | 
 **resource_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; on the activity for the the resource type. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag_from_experiment**
> TagRemove delete_tag_from_experiment(id, tag_id)



Removes a tag from an experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
tag_id = 'tag_id_example' # str | The `_id` of the tag to be removed from the experiment.

try:
    api_response = api_instance.delete_tag_from_experiment(id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->delete_tag_from_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **tag_id** | **str**| The &#x60;_id&#x60; of the tag to be removed from the experiment. | 

### Return type

[**TagRemove**](TagRemove.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_experiment_data**
> Task export_experiment_data(id, filename=filename, file_type=file_type, refresh=refresh)



Triggers the export of experiment data or returns the latest exported data.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
filename = 'filename_example' # str | The desired name to be given to downloadable file. (optional)
file_type = 'file_type_example' # str | The desired data format type (defaults to `text/csv`) to be given to downloadable file. Can be one of `text/csv`, `binary/parquet`. (optional)
refresh = true # bool | If set to true forces a regeneration of all datatables regardless of being stale or not. (optional)

try:
    api_response = api_instance.export_experiment_data(id, filename=filename, file_type=file_type, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->export_experiment_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **filename** | **str**| The desired name to be given to downloadable file. | [optional] 
 **file_type** | **str**| The desired data format type (defaults to &#x60;text/csv&#x60;) to be given to downloadable file. Can be one of &#x60;text/csv&#x60;, &#x60;binary/parquet&#x60;. | [optional] 
 **refresh** | **bool**| If set to true forces a regeneration of all datatables regardless of being stale or not. | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_experiment_data_status**
> Task export_experiment_data_status(id, filename=filename, file_type=file_type)



Returns the status of the exported experiment data for the specified experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment that has been exported.
filename = 'filename_example' # str | The desired name to be given to downloadable file. (optional)
file_type = 'file_type_example' # str | The desired data format type (defaults to `text/csv`) to be given to downloadable file. Can be one of `text/csv`, `binary/parquet`. (optional)

try:
    api_response = api_instance.export_experiment_data_status(id, filename=filename, file_type=file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->export_experiment_data_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment that has been exported. | 
 **filename** | **str**| The desired name to be given to downloadable file. | [optional] 
 **file_type** | **str**| The desired data format type (defaults to &#x60;text/csv&#x60;) to be given to downloadable file. Can be one of &#x60;text/csv&#x60;, &#x60;binary/parquet&#x60;. | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiment**
> Experiment get_experiment(id)



Returns the detail for the specified experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.

try:
    api_response = api_instance.get_experiment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->get_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 

### Return type

[**Experiment**](Experiment.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiment_comment**
> Comment get_experiment_comment(id, comment_id)



Returns the specific comment (or observation) associated with an experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
comment_id = 'comment_id_example' # str | The `_id` of the comment.

try:
    api_response = api_instance.get_experiment_comment(id, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->get_experiment_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **comment_id** | **str**| The &#x60;_id&#x60; of the comment. | 

### Return type

[**Comment**](Comment.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiment_data_clean**
> DataTables get_experiment_data_clean(id, activity_id, rgid=rgid, rid=rid, rdid=rdid, vt=vt, rl=rl)



Returns the clean data tables for an activity (step). Data Cleaning transforms raw data tables that is collected onto runs into a more uniform and structured form.  Raw data is any data that is uploaded, acquired via the data agent, or manually entered. Each time one or more values of raw data are loaded onto a property on a run, that data is stored as a separate data group.  The relationship between data in separate groups is not made explicit until a Data Cleaning method is applied. For more information regarding data cleaning, please our article [Working with Data Cleanup Procedures](https://riffyn.zendesk.com/hc/en-us/articles/225456227-Working-with-Data-Cleanup-Procedures) 

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
activity_id = 'activity_id_example' # str | The `_id` of the activity (step). Refers to the Process level Activity `_id`.
rgid = ['rgid_example'] # list[str] | A comma spearated list of run group ids. The `runMap` and `datatables` objects will be filtered to only include data from runs in these run groups. E.g. `?rgid=PEHYK7LzGpqEWuNPQ,ypPdk7K5Hrai9djNi`  (optional)
rid = ['rid_example'] # list[str] | A comma spearated list of run ids. The `runMap` and `datatables` objects will be filtered to only include data from these runs. E.g. `?rid=MTokEKhfqLNJk6t8A,XmnkEwGoC3nJ9tA9y`  (optional)
rdid = ['rdid_example'] # list[str] | A comma spearated list of resourceDefIds. The `datatables` object will be filtered to only include runs that contain the specified values. E.g. `?rdid=BQZhhN7PnZTf2CqmE,ENKA9T2Ph7Wszbeaf`  (optional)
vt = 'vt_example' # str | Filters columns returned in the datatables to the specified `valueType`. Columns with no `valueType` property will still be included in the datatables.  (optional)
rl = 'rl_example' # str | Filter runs to only those that contain a resource with the specified resource label. You may look up the resource label using the `getResource` method.  (optional)

try:
    api_response = api_instance.get_experiment_data_clean(id, activity_id, rgid=rgid, rid=rid, rdid=rdid, vt=vt, rl=rl)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->get_experiment_data_clean: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity (step). Refers to the Process level Activity &#x60;_id&#x60;. | 
 **rgid** | [**list[str]**](str.md)| A comma spearated list of run group ids. The &#x60;runMap&#x60; and &#x60;datatables&#x60; objects will be filtered to only include data from runs in these run groups. E.g. &#x60;?rgid&#x3D;PEHYK7LzGpqEWuNPQ,ypPdk7K5Hrai9djNi&#x60;  | [optional] 
 **rid** | [**list[str]**](str.md)| A comma spearated list of run ids. The &#x60;runMap&#x60; and &#x60;datatables&#x60; objects will be filtered to only include data from these runs. E.g. &#x60;?rid&#x3D;MTokEKhfqLNJk6t8A,XmnkEwGoC3nJ9tA9y&#x60;  | [optional] 
 **rdid** | [**list[str]**](str.md)| A comma spearated list of resourceDefIds. The &#x60;datatables&#x60; object will be filtered to only include runs that contain the specified values. E.g. &#x60;?rdid&#x3D;BQZhhN7PnZTf2CqmE,ENKA9T2Ph7Wszbeaf&#x60;  | [optional] 
 **vt** | **str**| Filters columns returned in the datatables to the specified &#x60;valueType&#x60;. Columns with no &#x60;valueType&#x60; property will still be included in the datatables.  | [optional] 
 **rl** | **str**| Filter runs to only those that contain a resource with the specified resource label. You may look up the resource label using the &#x60;getResource&#x60; method.  | [optional] 

### Return type

[**DataTables**](DataTables.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiment_data_raw**
> DataTables get_experiment_data_raw(id, activity_id, rgid=rgid, rid=rid, rnum=rnum, rdid=rdid, vt=vt, rl=rl)



Returns the raw data tables for an activity (step). Raw data is any data that is uploaded, acquired via the data agent, or manually entered. Each time one or more values of raw data are loaded onto a property on a run, that data is stored as a separate data group.  The relationship between data in separate groups is not made explicit until a Data Cleaning method is applied. 

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
activity_id = 'activity_id_example' # str | The `_id` of the activity (step). Refers to the Process level Activity `_id`.
rgid = ['rgid_example'] # list[str] | A comma spearated list of run group ids. The `runMap` and `datatables` objects will be filtered to only include data from runs in these run groups. E.g. `?rgid=PEHYK7LzGpqEWuNPQ,ypPdk7K5Hrai9djNi`  (optional)
rid = ['rid_example'] # list[str] | A comma spearated list of run ids. The `runMap` and `datatables` objects will be filtered to only include data from these runs. E.g. `?rid=MTokEKhfqLNJk6t8A,XmnkEwGoC3nJ9tA9y`  (optional)
rnum = ['rnum_example'] # list[str] | A comma spearated list of run numbers. The `runMap` and `datatables` objects will be filtered to only include data from these runs. E.g. `?rnum=1,2,3,4,5`  (optional)
rdid = ['rdid_example'] # list[str] | A comma spearated list of resourceDefIds. The `datatables` object will be filtered to only include runs that contain the specified values. E.g. `?rdid=BQZhhN7PnZTf2CqmE,ENKA9T2Ph7Wszbeaf`  (optional)
vt = 'vt_example' # str | Filters columns returned in the datatables to the specified `valueType`. Columns with no `valueType` property will still be included in the datatables.  (optional)
rl = 'rl_example' # str | Filter runs to only those that contain a resource with the specified resource label. You may look up the resource label using the `getResource` method.  (optional)

try:
    api_response = api_instance.get_experiment_data_raw(id, activity_id, rgid=rgid, rid=rid, rnum=rnum, rdid=rdid, vt=vt, rl=rl)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->get_experiment_data_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity (step). Refers to the Process level Activity &#x60;_id&#x60;. | 
 **rgid** | [**list[str]**](str.md)| A comma spearated list of run group ids. The &#x60;runMap&#x60; and &#x60;datatables&#x60; objects will be filtered to only include data from runs in these run groups. E.g. &#x60;?rgid&#x3D;PEHYK7LzGpqEWuNPQ,ypPdk7K5Hrai9djNi&#x60;  | [optional] 
 **rid** | [**list[str]**](str.md)| A comma spearated list of run ids. The &#x60;runMap&#x60; and &#x60;datatables&#x60; objects will be filtered to only include data from these runs. E.g. &#x60;?rid&#x3D;MTokEKhfqLNJk6t8A,XmnkEwGoC3nJ9tA9y&#x60;  | [optional] 
 **rnum** | [**list[str]**](str.md)| A comma spearated list of run numbers. The &#x60;runMap&#x60; and &#x60;datatables&#x60; objects will be filtered to only include data from these runs. E.g. &#x60;?rnum&#x3D;1,2,3,4,5&#x60;  | [optional] 
 **rdid** | [**list[str]**](str.md)| A comma spearated list of resourceDefIds. The &#x60;datatables&#x60; object will be filtered to only include runs that contain the specified values. E.g. &#x60;?rdid&#x3D;BQZhhN7PnZTf2CqmE,ENKA9T2Ph7Wszbeaf&#x60;  | [optional] 
 **vt** | **str**| Filters columns returned in the datatables to the specified &#x60;valueType&#x60;. Columns with no &#x60;valueType&#x60; property will still be included in the datatables.  | [optional] 
 **rl** | **str**| Filter runs to only those that contain a resource with the specified resource label. You may look up the resource label using the &#x60;getResource&#x60; method.  | [optional] 

### Return type

[**DataTables**](DataTables.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiment_summary**
> ExperimentSummary get_experiment_summary(id)



Returns the summary and purpose for the specified experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.

try:
    api_response = api_instance.get_experiment_summary(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->get_experiment_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 

### Return type

[**ExperimentSummary**](ExperimentSummary.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_for_experiment**
> Role get_role_for_experiment(id, user_id)



Returns the highest role for the specified user for the specific experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
user_id = 'user_id_example' # str | The `_id` of the user.

try:
    api_response = api_instance.get_role_for_experiment(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->get_role_for_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **user_id** | **str**| The &#x60;_id&#x60; of the user. | 

### Return type

[**Role**](Role.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_experiment_activities**
> Activities list_experiment_activities(id, sort=sort, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator, public=public)



List or search the activities (steps) associated with an experiment. When using `activityId`, use `objectId` or refer to the `_id` on the Process level activity (`listActivities` endpoint).

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
sort = ['sort_example'] # list[str] | The sort order to use for the result set. To sort in descending order, prefix the field name with a dash(`-`). A comma separated list may be used to sort by more than one field (e.g. `name,-label`).  (optional)
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)
name = 'name_example' # str | Limits the result set to items with this exact name (case insensitive). (optional)
creator = 'creator_example' # str | Limits the result set to items created by the user with this username. (optional)
public = true # bool | Toggles the result set between public and private data. Default value is `false` (optional)

try:
    api_response = api_instance.list_experiment_activities(id, sort=sort, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator, public=public)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->list_experiment_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **sort** | [**list[str]**](str.md)| The sort order to use for the result set. To sort in descending order, prefix the field name with a dash(&#x60;-&#x60;). A comma separated list may be used to sort by more than one field (e.g. &#x60;name,-label&#x60;).  | [optional] 
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 
 **before** | **str**| Limits the result set to items created on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  | [optional] 
 **after** | **str**| Limits the result set to items created on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;).  | [optional] 
 **fields** | **str**| Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use &#x60;fields&#x3D;name,created&#x60;. To exclude the name and created fields from the results use &#x60;fields&#x3D;-name,-created&#x60;. Inclusion and exclusion options can not be set in the same query.  | [optional] 
 **name** | **str**| Limits the result set to items with this exact name (case insensitive). | [optional] 
 **creator** | **str**| Limits the result set to items created by the user with this username. | [optional] 
 **public** | **bool**| Toggles the result set between public and private data. Default value is &#x60;false&#x60; | [optional] 

### Return type

[**Activities**](Activities.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_experiment_comments**
> Comments list_experiment_comments(id, activity_id=activity_id, group_id=group_id, limit=limit, offset=offset, before=before, after=after, modified_before=modified_before, modified_after=modified_after, fields=fields, creator=creator)



Lists the comments (or observations) associated with an experiment. Includes activity, and group comments.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
activity_id = 'activity_id_example' # str | Limits the result set to items associated with the `_id` of the specified activity. Refers to the Process level Activity `_id`. (optional)
group_id = 'group_id_example' # str | Limits the result set to items associated with the `_id` of the specified group. The process `_id` is the `topGroupId`. (optional)
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)
modified_before = 'modified_before_example' # str | Limits the result set to items modified on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch, `1507650828`).  (optional)
modified_after = 'modified_after_example' # str | Limits the result set to items modified on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch, `1507650828`).  (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)
creator = 'creator_example' # str | Limits the result set to items created by the user with this username. (optional)

try:
    api_response = api_instance.list_experiment_comments(id, activity_id=activity_id, group_id=group_id, limit=limit, offset=offset, before=before, after=after, modified_before=modified_before, modified_after=modified_after, fields=fields, creator=creator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->list_experiment_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **activity_id** | **str**| Limits the result set to items associated with the &#x60;_id&#x60; of the specified activity. Refers to the Process level Activity &#x60;_id&#x60;. | [optional] 
 **group_id** | **str**| Limits the result set to items associated with the &#x60;_id&#x60; of the specified group. The process &#x60;_id&#x60; is the &#x60;topGroupId&#x60;. | [optional] 
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 
 **before** | **str**| Limits the result set to items created on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  | [optional] 
 **after** | **str**| Limits the result set to items created on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;).  | [optional] 
 **modified_before** | **str**| Limits the result set to items modified on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60; or epoch, &#x60;1507650828&#x60;).  | [optional] 
 **modified_after** | **str**| Limits the result set to items modified on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60; or epoch, &#x60;1507650828&#x60;).  | [optional] 
 **fields** | **str**| Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use &#x60;fields&#x3D;name,created&#x60;. To exclude the name and created fields from the results use &#x60;fields&#x3D;-name,-created&#x60;. Inclusion and exclusion options can not be set in the same query.  | [optional] 
 **creator** | **str**| Limits the result set to items created by the user with this username. | [optional] 

### Return type

[**Comments**](Comments.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_experiment_tags**
> Tags list_experiment_tags(id, name=name, limit=limit, offset=offset, before=before, after=after, modified_before=modified_before, modified_after=modified_after, fields=fields, creator=creator)



Returns the tags for the specified experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
name = 'name_example' # str | Limits the result set to items with this exact name (case insensitive). (optional)
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)
modified_before = 'modified_before_example' # str | Limits the result set to items modified on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch, `1507650828`).  (optional)
modified_after = 'modified_after_example' # str | Limits the result set to items modified on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch, `1507650828`).  (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)
creator = 'creator_example' # str | Limits the result set to items created by the user with this username. (optional)

try:
    api_response = api_instance.list_experiment_tags(id, name=name, limit=limit, offset=offset, before=before, after=after, modified_before=modified_before, modified_after=modified_after, fields=fields, creator=creator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->list_experiment_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **name** | **str**| Limits the result set to items with this exact name (case insensitive). | [optional] 
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 
 **before** | **str**| Limits the result set to items created on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  | [optional] 
 **after** | **str**| Limits the result set to items created on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;).  | [optional] 
 **modified_before** | **str**| Limits the result set to items modified on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60; or epoch, &#x60;1507650828&#x60;).  | [optional] 
 **modified_after** | **str**| Limits the result set to items modified on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60; or epoch, &#x60;1507650828&#x60;).  | [optional] 
 **fields** | **str**| Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use &#x60;fields&#x3D;name,created&#x60;. To exclude the name and created fields from the results use &#x60;fields&#x3D;-name,-created&#x60;. Inclusion and exclusion options can not be set in the same query.  | [optional] 
 **creator** | **str**| Limits the result set to items created by the user with this username. | [optional] 

### Return type

[**Tags**](Tags.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_experiments**
> Experiments list_experiments(sort=sort, top_group_id=top_group_id, limit=limit, modified_before=modified_before, modified_after=modified_after, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator, public=public, deleted=deleted)



List or search the user's experiments.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
sort = ['sort_example'] # list[str] | The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (`-`). A comma separated list may be used to sort by more than one field (e.g. `process_name,-label`).  (optional)
top_group_id = 'top_group_id_example' # str | Limits the result set to items associated with the `_id` of the specified process (optional)
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
modified_before = 'modified_before_example' # str | Limits the result set to items modified on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch, `1507650828`).  (optional)
modified_after = 'modified_after_example' # str | Limits the result set to items modified on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch, `1507650828`).  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)
name = 'name_example' # str | Limits the result set to items with this exact name (case insensitive). (optional)
creator = 'creator_example' # str | Limits the result set to items created by the user with this username. (optional)
public = true # bool | Toggles the result set between public and private data. Default value is `false` (optional)
deleted = true # bool | Limits the results to deleted items, excludes them, or returns both deleted and non-deleted items if set to `all `. Default value       is `false`, to only show non-deleted items.  (optional)

try:
    api_response = api_instance.list_experiments(sort=sort, top_group_id=top_group_id, limit=limit, modified_before=modified_before, modified_after=modified_after, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator, public=public, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->list_experiments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | [**list[str]**](str.md)| The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (&#x60;-&#x60;). A comma separated list may be used to sort by more than one field (e.g. &#x60;process_name,-label&#x60;).  | [optional] 
 **top_group_id** | **str**| Limits the result set to items associated with the &#x60;_id&#x60; of the specified process | [optional] 
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **modified_before** | **str**| Limits the result set to items modified on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60; or epoch, &#x60;1507650828&#x60;).  | [optional] 
 **modified_after** | **str**| Limits the result set to items modified on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60; or epoch, &#x60;1507650828&#x60;).  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 
 **before** | **str**| Limits the result set to items created on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  | [optional] 
 **after** | **str**| Limits the result set to items created on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;).  | [optional] 
 **fields** | **str**| Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use &#x60;fields&#x3D;name,created&#x60;. To exclude the name and created fields from the results use &#x60;fields&#x3D;-name,-created&#x60;. Inclusion and exclusion options can not be set in the same query.  | [optional] 
 **name** | **str**| Limits the result set to items with this exact name (case insensitive). | [optional] 
 **creator** | **str**| Limits the result set to items created by the user with this username. | [optional] 
 **public** | **bool**| Toggles the result set between public and private data. Default value is &#x60;false&#x60; | [optional] 
 **deleted** | **bool**| Limits the results to deleted items, excludes them, or returns both deleted and non-deleted items if set to &#x60;all &#x60;. Default value       is &#x60;false&#x60;, to only show non-deleted items.  | [optional] 

### Return type

[**Experiments**](Experiments.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replies_to_experiment_comment**
> Comments list_replies_to_experiment_comment(id, comment_id, limit=limit, offset=offset, before=before, after=after, modified_before=modified_before, modified_after=modified_after, fields=fields, creator=creator)



Lists replies to a specific comment (or observation) associated with an experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
comment_id = 'comment_id_example' # str | The `_id` of the comment.
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)
modified_before = 'modified_before_example' # str | Limits the result set to items modified on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch, `1507650828`).  (optional)
modified_after = 'modified_after_example' # str | Limits the result set to items modified on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch, `1507650828`).  (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)
creator = 'creator_example' # str | Limits the result set to items created by the user with this username. (optional)

try:
    api_response = api_instance.list_replies_to_experiment_comment(id, comment_id, limit=limit, offset=offset, before=before, after=after, modified_before=modified_before, modified_after=modified_after, fields=fields, creator=creator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->list_replies_to_experiment_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **comment_id** | **str**| The &#x60;_id&#x60; of the comment. | 
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 
 **before** | **str**| Limits the result set to items created on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  | [optional] 
 **after** | **str**| Limits the result set to items created on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;).  | [optional] 
 **modified_before** | **str**| Limits the result set to items modified on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60; or epoch, &#x60;1507650828&#x60;).  | [optional] 
 **modified_after** | **str**| Limits the result set to items modified on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60; or epoch, &#x60;1507650828&#x60;).  | [optional] 
 **fields** | **str**| Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use &#x60;fields&#x3D;name,created&#x60;. To exclude the name and created fields from the results use &#x60;fields&#x3D;-name,-created&#x60;. Inclusion and exclusion options can not be set in the same query.  | [optional] 
 **creator** | **str**| Limits the result set to items created by the user with this username. | [optional] 

### Return type

[**Comments**](Comments.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reply_to_expriment_comment**
> CommentResponse reply_to_expriment_comment(body, id, comment_id)



Replies to a specific comment (or observation) associated with an experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.CommentMessageBody() # CommentMessageBody | A JSON object containing the necessary properties to reply to a comment.
id = 'id_example' # str | The `_id` of the experiment.
comment_id = 'comment_id_example' # str | The `_id` of the comment.

try:
    api_response = api_instance.reply_to_expriment_comment(body, id, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->reply_to_expriment_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentMessageBody**](CommentMessageBody.md)| A JSON object containing the necessary properties to reply to a comment. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **comment_id** | **str**| The &#x60;_id&#x60; of the comment. | 

### Return type

[**CommentResponse**](CommentResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_experiment**
> SuccessShared share_experiment(body, id)



Share an existing experiment with a user, team, or organization.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.ShareExperimentBody() # ShareExperimentBody | A JSON object containing the necessary properties to share the property.
id = 'id_example' # str | The `_id` of the experiment.

try:
    api_response = api_instance.share_experiment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->share_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShareExperimentBody**](ShareExperimentBody.md)| A JSON object containing the necessary properties to share the property. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 

### Return type

[**SuccessShared**](SuccessShared.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unshare_experiment**
> SuccessfullyUnshared unshare_experiment(body, id, principal_id)



Revoke access to an existing experiment from a user, team, or organization.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.UnshareExperimentBody() # UnshareExperimentBody | A JSON object containing the necessary properties to revoke access to the experiment.
id = 'id_example' # str | The `_id` of the experiment.
principal_id = 'principal_id_example' # str | The `_id` of the entity being revoked access to the experiment.

try:
    api_response = api_instance.unshare_experiment(body, id, principal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->unshare_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnshareExperimentBody**](UnshareExperimentBody.md)| A JSON object containing the necessary properties to revoke access to the experiment. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **principal_id** | **str**| The &#x60;_id&#x60; of the entity being revoked access to the experiment. | 

### Return type

[**SuccessfullyUnshared**](SuccessfullyUnshared.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_experiment**
> Experiment update_experiment(body, id)



Updates an existing experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateExperimentBody() # UpdateExperimentBody | A JSON object containing the properties of the experiment you would like to update.
id = 'id_example' # str | The `_id` of the experiment.

try:
    api_response = api_instance.update_experiment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->update_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateExperimentBody**](UpdateExperimentBody.md)| A JSON object containing the properties of the experiment you would like to update. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 

### Return type

[**Experiment**](Experiment.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_experiment_comment**
> CommentUpdated update_experiment_comment(body, id, comment_id)



Updates the specific comment (or observation) associated with an experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.CommentMessageBody() # CommentMessageBody | A JSON object containing the necessary properties to create a new comment (or observation).
id = 'id_example' # str | The `_id` of the experiment.
comment_id = 'comment_id_example' # str | The `_id` of the comment.

try:
    api_response = api_instance.update_experiment_comment(body, id, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->update_experiment_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentMessageBody**](CommentMessageBody.md)| A JSON object containing the necessary properties to create a new comment (or observation). | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **comment_id** | **str**| The &#x60;_id&#x60; of the comment. | 

### Return type

[**CommentUpdated**](CommentUpdated.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_experiment_summary**
> ExperimentSummary update_experiment_summary(body, id, summary_id)



Updates the summary and purpose for the specified experiment.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.SummaryBody() # SummaryBody | A JSON object containing the options for creating the summary.
id = 'id_example' # str | The `_id` of the experiment.
summary_id = 'summary_id_example' # str | The `_id` of the summary.

try:
    api_response = api_instance.update_experiment_summary(body, id, summary_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->update_experiment_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SummaryBody**](SummaryBody.md)| A JSON object containing the options for creating the summary. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **summary_id** | **str**| The &#x60;_id&#x60; of the summary. | 

### Return type

[**ExperimentSummary**](ExperimentSummary.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_property_type_on_experiment**
> InlineResponse2006 update_property_type_on_experiment(id, activity_id, resource_def_id, property_type_id, body=body)



Ad hoc update of a property type on a resource type on the `input` or `output` of an activity on a experiment. Both ad hoc and process design property types can be updated from the experiment but changes will not appear in process design. Allows for setting a different unit than the default unit for the property.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment.
activity_id = 'activity_id_example' # str | The `_id` of the activity. Refers to the Process Activity `_id` from the `listActivities` endpoint. When using the `listExperimentActivities` endpoint, use the `objectId`.
resource_def_id = 'resource_def_id_example' # str | The `_id` of the `input` or `output` on the activity for the resource type.
property_type_id = 'property_type_id_example' # str | The `_id` of the property type.
body = swagger_client.Body5() # Body5 | A JSON object containing the options for removing the property type. (optional)

try:
    api_response = api_instance.update_property_type_on_experiment(id, activity_id, resource_def_id, property_type_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->update_property_type_on_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. When using the &#x60;listExperimentActivities&#x60; endpoint, use the &#x60;objectId&#x60;. | 
 **resource_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; on the activity for the resource type. | 
 **property_type_id** | **str**| The &#x60;_id&#x60; of the property type. | 
 **body** | [**Body5**](Body5.md)| A JSON object containing the options for removing the property type. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource_type_on_experiment**
> InlineResponse2002 update_resource_type_on_experiment(body, id, activity_id, resource_def_id)



Change a resource type in the `input` or `output` of an activity on an experiment. Both ad hoc and process design resource types can be changed from the experiment but changes will not appear in process design.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body2() # Body2 | A JSON object containing the options for changing the resource type.
id = 'id_example' # str | The `_id` of the experiment the resource type is being changed for.
activity_id = 'activity_id_example' # str | The `_id` of the activity the resource type is being changed for.
resource_def_id = 'resource_def_id_example' # str | The `_id` of the `input` or `output` on the activity for the resource type being changed.

try:
    api_response = api_instance.update_resource_type_on_experiment(body, id, activity_id, resource_def_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->update_resource_type_on_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)| A JSON object containing the options for changing the resource type. | 
 **id** | **str**| The &#x60;_id&#x60; of the experiment the resource type is being changed for. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity the resource type is being changed for. | 
 **resource_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; on the activity for the resource type being changed. | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_config_status**
> FileUploadStatusResponse upload_config_status(id, activity_id, task_id)



Returns the status of the selected data uploaded from a file and a upload configuration. 

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment to manage the data to.
activity_id = 'activity_id_example' # str | The `_id` of activity (step) to add the data to. Refers to the Process Activity `_id` from the `listActivities` endpoint. When using the `listExperimentActivities` endpoint, use the `objectId`.
task_id = 'task_id_example' # str | The `_id` of the task for the applied upload config`.

try:
    api_response = api_instance.upload_config_status(id, activity_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->upload_config_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment to manage the data to. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of activity (step) to add the data to. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. When using the &#x60;listExperimentActivities&#x60; endpoint, use the &#x60;objectId&#x60;. | 
 **task_id** | **str**| The &#x60;_id&#x60; of the task for the applied upload config&#x60;. | 

### Return type

[**FileUploadStatusResponse**](FileUploadStatusResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_data_file**
> UploadFileResponse upload_data_file(id, activity_id, name=name)



Upload a file to be used with an upload configuration to add data to an activity. The file to be uploaded should be attached to the request body as a binary, or in curl request, include path to file `-T/Folder/path/to/File`. (Sample code is incomplete.) Content-Type for file must be one of these MIME types:  (the default is a .csv file, as illustrated in sample code)   | Ext.  | MIME Type                                                                  |  | ----- | -------------------------------------------------------------------------- |  | .csv  | text/csv                                                                   |  | .tsv  | text/tab-separated-values                                                  |  | .dsv  | text/csv                                                                   |  | .tab  | text/plain                                                                 |  | .txt  | text/plain                                                                 |  | .xlsx | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet          |  | .xls  | application/vnd.ms-excel                                                   |  | .xlsm | application/vnd.ms-excel.sheet.macroenabled.12                             | 

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the experiment to manage the data to.
activity_id = 'activity_id_example' # str | The `_id` of activity (step) to add the data to. Refers to the Process Activity `_id` from the `listActivities` endpoint. When using the `listExperimentActivities` endpoint, use the `objectId`.
name = 'name_example' # str | The name to be attributed to the file being uploaded. The file extension on the name will define how the file is parsed. If no extension is defined the file will be parsed as a character separated file. File extension and content-type must correspond (see chart in description). When using the file extension the content-type can be omitted. (optional)

try:
    api_response = api_instance.upload_data_file(id, activity_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->upload_data_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the experiment to manage the data to. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of activity (step) to add the data to. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. When using the &#x60;listExperimentActivities&#x60; endpoint, use the &#x60;objectId&#x60;. | 
 **name** | **str**| The name to be attributed to the file being uploaded. The file extension on the name will define how the file is parsed. If no extension is defined the file will be parsed as a character separated file. File extension and content-type must correspond (see chart in description). When using the file extension the content-type can be omitted. | [optional] 

### Return type

[**UploadFileResponse**](UploadFileResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

