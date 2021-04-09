# riffyn_nexus_sdk_v1.ProcessActivityApi

All URIs are relative to *deployment_url/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_component_to_resource_def**](ProcessActivityApi.md#add_component_to_resource_def) | **POST** /process/{id}/activity/{activityId}/resource-type/{resourceDefId}/component | addComponentToResourceDef
[**add_property_type_to_activity**](ProcessActivityApi.md#add_property_type_to_activity) | **POST** /process/{id}/activity/{activityId}/resource-type/{resourceDefId}/property-type | addPropertyTypeToActivity
[**add_resource_type_to_activity**](ProcessActivityApi.md#add_resource_type_to_activity) | **POST** /process/{id}/activity/{activityId}/resource-type | addResourceTypeToActivity
[**create_activity**](ProcessActivityApi.md#create_activity) | **POST** /process/{id}/activity | createActivity
[**delete_activity**](ProcessActivityApi.md#delete_activity) | **DELETE** /process/{id}/activity/{activityId} | deleteActivity
[**delete_component_from_resource_def**](ProcessActivityApi.md#delete_component_from_resource_def) | **DELETE** /process/{id}/activity/{activityId}/resource-type/{resourceDefId}/component/{componentId} | deleteComponentFromResourceDef
[**delete_property_type_from_activity**](ProcessActivityApi.md#delete_property_type_from_activity) | **DELETE** /process/{id}/activity/{activityId}/resource-type/{resourceDefId}/property-type/{propertyTypeId} | deletePropertyTypeFromActivity
[**delete_resource_type_from_activity**](ProcessActivityApi.md#delete_resource_type_from_activity) | **DELETE** /process/{id}/activity/{activityId}/resource-type/{resourceDefId} | deleteResourceTypeFromActivity
[**get_activity**](ProcessActivityApi.md#get_activity) | **GET** /process/{id}/activity/{activityId} | getActivity
[**get_activity_version**](ProcessActivityApi.md#get_activity_version) | **GET** /process/{id}/activity/{activityId}/version/{versionLabel} | getActivityVersion
[**list_activities**](ProcessActivityApi.md#list_activities) | **GET** /process/{id}/activities | listActivities
[**list_activity_versions**](ProcessActivityApi.md#list_activity_versions) | **GET** /process/{id}/activity/{activityId}/versions | listActivityVersions
[**update_activity**](ProcessActivityApi.md#update_activity) | **PATCH** /process/{id}/activity/{activityId} | updateActivity
[**update_component_on_resource_def**](ProcessActivityApi.md#update_component_on_resource_def) | **PATCH** /process/{id}/activity/{activityId}/resource-type/{resourceDefId}/component/{componentId} | updateComponentOnResourceDef
[**update_property_type_on_activity**](ProcessActivityApi.md#update_property_type_on_activity) | **PATCH** /process/{id}/activity/{activityId}/resource-type/{resourceDefId}/property-type/{propertyTypeId} | updatePropertyTypeOnActivity
[**update_resource_type_on_activity**](ProcessActivityApi.md#update_resource_type_on_activity) | **PATCH** /process/{id}/activity/{activityId}/resource-type/{resourceDefId} | updateResourceTypeOnActivity

# **add_component_to_resource_def**
> InlineResponse2003 add_component_to_resource_def(id, activity_id, resource_def_id, body=body)

addComponentToResourceDef

Add a component on a resource type on the `input` or `output` of an activity on a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessActivityApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
activity_id = 'activity_id_example' # str | The `_id` of the activity. Refers to the Process Activity `_id` from the `listActivities` endpoint. When using the `listExperimentActivities` endpoint, use the `objectId`. 
resource_def_id = 'resource_def_id_example' # str | The `_id` of the `input` or `output` on the activity for the resource type the component will be added to.
body = riffyn_nexus_sdk_v1.AddComponentToResourceType() # AddComponentToResourceType | A JSON object containing the options for adding the component. (optional)

try:
    # addComponentToResourceDef
    api_response = api_instance.add_component_to_resource_def(id, activity_id, resource_def_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessActivityApi->add_component_to_resource_def: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. When using the &#x60;listExperimentActivities&#x60; endpoint, use the &#x60;objectId&#x60;.  | 
 **resource_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; on the activity for the resource type the component will be added to. | 
 **body** | [**AddComponentToResourceType**](AddComponentToResourceType.md)| A JSON object containing the options for adding the component. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_property_type_to_activity**
> InlineResponse2005 add_property_type_to_activity(body, id, activity_id, resource_def_id)

addPropertyTypeToActivity

Add a property type to a resource type on the `input` or `output` of an activity on a process. Property type will be created with default unit.

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
api_instance = riffyn_nexus_sdk_v1.ProcessActivityApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.AddPropertyTypeBody() # AddPropertyTypeBody | A JSON object containing the options for adding the property type.
id = 'id_example' # str | The `_id` of process.
activity_id = 'activity_id_example' # str | The `_id` of the activity.
resource_def_id = 'resource_def_id_example' # str | The `_id` of the `input` or `output` on the activity for the the resource type the property type is being added to.

try:
    # addPropertyTypeToActivity
    api_response = api_instance.add_property_type_to_activity(body, id, activity_id, resource_def_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessActivityApi->add_property_type_to_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddPropertyTypeBody**](AddPropertyTypeBody.md)| A JSON object containing the options for adding the property type. | 
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity. | 
 **resource_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; on the activity for the the resource type the property type is being added to. | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_resource_type_to_activity**
> InlineResponse2008 add_resource_type_to_activity(body, id, activity_id)

addResourceTypeToActivity

Add a resource type to the `input` or `output` of an activity on a process. Default components and property types for that resource type will be included.

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
api_instance = riffyn_nexus_sdk_v1.ProcessActivityApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.AddResourceTypeBody() # AddResourceTypeBody | A JSON object containing the options for creating the resource type.
id = 'id_example' # str | The `_id` of process the resource type is being added to.
activity_id = 'activity_id_example' # str | The `_id` of activity the resource type is being added to.

try:
    # addResourceTypeToActivity
    api_response = api_instance.add_resource_type_to_activity(body, id, activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessActivityApi->add_resource_type_to_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddResourceTypeBody**](AddResourceTypeBody.md)| A JSON object containing the options for creating the resource type. | 
 **id** | **str**| The &#x60;_id&#x60; of process the resource type is being added to. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of activity the resource type is being added to. | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_activity**
> Activity create_activity(body, id)

createActivity

Create a new activity (step) on a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessActivityApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.ActivityBody() # ActivityBody | A JSON object containing the necessary properties to create a new activity.
id = 'id_example' # str | The `_id` of process.

try:
    # createActivity
    api_response = api_instance.create_activity(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessActivityApi->create_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActivityBody**](ActivityBody.md)| A JSON object containing the necessary properties to create a new activity. | 
 **id** | **str**| The &#x60;_id&#x60; of process. | 

### Return type

[**Activity**](Activity.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_activity**
> InlineResponse2007 delete_activity(id, activity_id)

deleteActivity

Deletes the specified activity (step) from a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessActivityApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
activity_id = 'activity_id_example' # str | The `_id` of the activity.

try:
    # deleteActivity
    api_response = api_instance.delete_activity(id, activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessActivityApi->delete_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity. | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_component_from_resource_def**
> InlineResponse20013 delete_component_from_resource_def(id, activity_id, resource_def_id, component_id, propagate=propagate, propagation_direction=propagation_direction)

deleteComponentFromResourceDef

Removal of a component from a resource type on the `input` or `output` of an activity on a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessActivityApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
activity_id = 'activity_id_example' # str | The `_id` of the activity. Refers to the Process Activity `_id` from the `listActivities` endpoint. When using the `listExperimentActivities` endpoint, use the `objectId`. 
resource_def_id = 'resource_def_id_example' # str | The `_id` of the `input` or `output` on the activity for the resource type the component will be removed from.
component_id = 'component_id_example' # str | The `_id` of the resource type of the component being removed.
propagate = true # bool | Propagates the removal of the component to connected instances of the resource type on the activity. Defaults to true if not set to false. (optional)
propagation_direction = 'propagation_direction_example' # str | Direction of propagation. Will be one of `upstream` or `downstream`. Defaults to `downstream` if not set. Not required if `propagate` is not defined. (optional)

try:
    # deleteComponentFromResourceDef
    api_response = api_instance.delete_component_from_resource_def(id, activity_id, resource_def_id, component_id, propagate=propagate, propagation_direction=propagation_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessActivityApi->delete_component_from_resource_def: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. When using the &#x60;listExperimentActivities&#x60; endpoint, use the &#x60;objectId&#x60;.  | 
 **resource_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; on the activity for the resource type the component will be removed from. | 
 **component_id** | **str**| The &#x60;_id&#x60; of the resource type of the component being removed. | 
 **propagate** | **bool**| Propagates the removal of the component to connected instances of the resource type on the activity. Defaults to true if not set to false. | [optional] 
 **propagation_direction** | **str**| Direction of propagation. Will be one of &#x60;upstream&#x60; or &#x60;downstream&#x60;. Defaults to &#x60;downstream&#x60; if not set. Not required if &#x60;propagate&#x60; is not defined. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property_type_from_activity**
> InlineResponse20011 delete_property_type_from_activity(body, id, activity_id, resource_def_id, property_type_id)

deletePropertyTypeFromActivity

Removal of a property type from a resource type on the `input` or `output` of an activity on a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessActivityApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = NULL # object | A JSON object containing the options for removing the property type.
id = 'id_example' # str | The `_id` of the process.
activity_id = 'activity_id_example' # str | The `_id` of the activity. Refers to the Process Activity `_id` from the `listActivities` endpoint. When using the `listExperimentActivities` endpoint, use the `objectId`.
resource_def_id = 'resource_def_id_example' # str | The `_id` of the `input` or `output` on the activity for the resource type the property type will be updated on.
property_type_id = 'property_type_id_example' # str | The `_id` of the property type.

try:
    # deletePropertyTypeFromActivity
    api_response = api_instance.delete_property_type_from_activity(body, id, activity_id, resource_def_id, property_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessActivityApi->delete_property_type_from_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| A JSON object containing the options for removing the property type. | 
 **id** | **str**| The &#x60;_id&#x60; of the process. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. When using the &#x60;listExperimentActivities&#x60; endpoint, use the &#x60;objectId&#x60;. | 
 **resource_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; on the activity for the resource type the property type will be updated on. | 
 **property_type_id** | **str**| The &#x60;_id&#x60; of the property type. | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_type_from_activity**
> InlineResponse2009 delete_resource_type_from_activity(id, activity_id, resource_def_id)

deleteResourceTypeFromActivity

Deletes a resource type from the `input` or `output` of an activity on a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessActivityApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process the resource type is being deleted from.
activity_id = 'activity_id_example' # str | The `_id` of activity the resource type is being deleted from.
resource_def_id = 'resource_def_id_example' # str | The `_id` of the `input` or `output` on the activity for the resource type being deleted.

try:
    # deleteResourceTypeFromActivity
    api_response = api_instance.delete_resource_type_from_activity(id, activity_id, resource_def_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessActivityApi->delete_resource_type_from_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process the resource type is being deleted from. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of activity the resource type is being deleted from. | 
 **resource_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; on the activity for the resource type being deleted. | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity**
> Activity get_activity(id, activity_id)

getActivity

Returns the details for the specified activity (step) on a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessActivityApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
activity_id = 'activity_id_example' # str | The `_id` of the activity.

try:
    # getActivity
    api_response = api_instance.get_activity(id, activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessActivityApi->get_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity. | 

### Return type

[**Activity**](Activity.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_version**
> Activity get_activity_version(id, activity_id, version_label)

getActivityVersion

Returns design details on the specified activity and its version.

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
api_instance = riffyn_nexus_sdk_v1.ProcessActivityApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
activity_id = 'activity_id_example' # str | The `_id` of the activity.
version_label = 'version_label_example' # str | The `version.label` of the activity. Should be in the format of `0.01` or `1.00`.

try:
    # getActivityVersion
    api_response = api_instance.get_activity_version(id, activity_id, version_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessActivityApi->get_activity_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity. | 
 **version_label** | **str**| The &#x60;version.label&#x60; of the activity. Should be in the format of &#x60;0.01&#x60; or &#x60;1.00&#x60;. | 

### Return type

[**Activity**](Activity.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_activities**
> Activities list_activities(id, sort=sort, version=version, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator, public=public)

listActivities

List or search the activities (steps) associated with a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessActivityApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
sort = ['sort_example'] # list[str] | The sort order to use for the result set. To sort in descending order, prefix the field name with a dash(`-`). A comma separated list may be used to sort by more than one field (e.g. `name,-label`).  (optional)
version = 'version_example' # str | Limits the result set to the specified version label (optional)
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)
name = 'name_example' # str | Limits the result set to items with this exact name (case insensitive). (optional)
creator = 'creator_example' # str | Limits the result set to items created by the user with this username. (optional)
public = true # bool | Toggles the result set between public and private data. Default value is `false` (optional)

try:
    # listActivities
    api_response = api_instance.list_activities(id, sort=sort, version=version, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator, public=public)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessActivityApi->list_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **sort** | [**list[str]**](str.md)| The sort order to use for the result set. To sort in descending order, prefix the field name with a dash(&#x60;-&#x60;). A comma separated list may be used to sort by more than one field (e.g. &#x60;name,-label&#x60;).  | [optional] 
 **version** | **str**| Limits the result set to the specified version label | [optional] 
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

# **list_activity_versions**
> Activities list_activity_versions(id, activity_id)

listActivityVersions

Returns design details on all versions of specified activity associated with a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessActivityApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
activity_id = 'activity_id_example' # str | The `_id` of the activity.

try:
    # listActivityVersions
    api_response = api_instance.list_activity_versions(id, activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessActivityApi->list_activity_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity. | 

### Return type

[**Activities**](Activities.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_activity**
> Activity update_activity(body, id, activity_id)

updateActivity

Updates the detail for the specified activity (step) on a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessActivityApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.UpdateActivityBody() # UpdateActivityBody | A JSON object containing the necessary properties to update an activity.
id = 'id_example' # str | The `_id` of process.
activity_id = 'activity_id_example' # str | The `_id` of the activity.

try:
    # updateActivity
    api_response = api_instance.update_activity(body, id, activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessActivityApi->update_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateActivityBody**](UpdateActivityBody.md)| A JSON object containing the necessary properties to update an activity. | 
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity. | 

### Return type

[**Activity**](Activity.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_component_on_resource_def**
> InlineResponse2003 update_component_on_resource_def(id, activity_id, resource_def_id, component_id, body=body)

updateComponentOnResourceDef

Update a component on a resource type on the `input` or `output` of an activity on a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessActivityApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
activity_id = 'activity_id_example' # str | The `_id` of the activity. Refers to the Process Activity `_id` from the `listActivities` endpoint. When using the `listExperimentActivities` endpoint, use the `objectId`. 
resource_def_id = 'resource_def_id_example' # str | The `_id` of the `input` or `output` on the activity for the resource type the component will be updated on.
component_id = 'component_id_example' # str | The `_id` of the resource type being used as a component.
body = riffyn_nexus_sdk_v1.UpdateComponentOnResType() # UpdateComponentOnResType | A JSON object containing the options for adding the component. (optional)

try:
    # updateComponentOnResourceDef
    api_response = api_instance.update_component_on_resource_def(id, activity_id, resource_def_id, component_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessActivityApi->update_component_on_resource_def: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. When using the &#x60;listExperimentActivities&#x60; endpoint, use the &#x60;objectId&#x60;.  | 
 **resource_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; on the activity for the resource type the component will be updated on. | 
 **component_id** | **str**| The &#x60;_id&#x60; of the resource type being used as a component. | 
 **body** | [**UpdateComponentOnResType**](UpdateComponentOnResType.md)| A JSON object containing the options for adding the component. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_property_type_on_activity**
> InlineResponse20012 update_property_type_on_activity(id, activity_id, resource_def_id, property_type_id, body=body)

updatePropertyTypeOnActivity

Update a property type on a resource type on the `input` or `output` of an activity on a process. Allows for setting a different unit than the default unit for the property.

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
api_instance = riffyn_nexus_sdk_v1.ProcessActivityApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the process.
activity_id = 'activity_id_example' # str | The `_id` of the activity. Refers to the Process Activity `_id` from the `listActivities` endpoint. When using the `listExperimentActivities` endpoint, use the `objectId`.
resource_def_id = 'resource_def_id_example' # str | The `_id` of the `input` or `output` on the activity for the resource type the property type will be updated on.
property_type_id = 'property_type_id_example' # str | The `_id` of the property type.
body = riffyn_nexus_sdk_v1.Body7() # Body7 | A JSON object containing the options for removing the property type. (optional)

try:
    # updatePropertyTypeOnActivity
    api_response = api_instance.update_property_type_on_activity(id, activity_id, resource_def_id, property_type_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessActivityApi->update_property_type_on_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the process. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of the activity. Refers to the Process Activity &#x60;_id&#x60; from the &#x60;listActivities&#x60; endpoint. When using the &#x60;listExperimentActivities&#x60; endpoint, use the &#x60;objectId&#x60;. | 
 **resource_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; on the activity for the resource type the property type will be updated on. | 
 **property_type_id** | **str**| The &#x60;_id&#x60; of the property type. | 
 **body** | [**Body7**](Body7.md)| A JSON object containing the options for removing the property type. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource_type_on_activity**
> InlineResponse20010 update_resource_type_on_activity(body, id, activity_id, resource_def_id)

updateResourceTypeOnActivity

Change a resource type on the `input` or `output` of an activity on a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessActivityApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.Body6() # Body6 | A JSON object containing the options for updating the resource type.
id = 'id_example' # str | The `_id` of process the resource type is being updated on.
activity_id = 'activity_id_example' # str | The `_id` of activity the resource type is being updated on.
resource_def_id = 'resource_def_id_example' # str | The `_id` of the `input` or `output` on the activity for the resource type being updated.

try:
    # updateResourceTypeOnActivity
    api_response = api_instance.update_resource_type_on_activity(body, id, activity_id, resource_def_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessActivityApi->update_resource_type_on_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body6**](Body6.md)| A JSON object containing the options for updating the resource type. | 
 **id** | **str**| The &#x60;_id&#x60; of process the resource type is being updated on. | 
 **activity_id** | **str**| The &#x60;_id&#x60; of activity the resource type is being updated on. | 
 **resource_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; on the activity for the resource type being updated. | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

