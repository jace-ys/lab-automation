# swagger_client.ResourceApi

All URIs are relative to *https://api.riffyn.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_component_to_resource**](ResourceApi.md#add_component_to_resource) | **PUT** /resource/{id}/component | 
[**add_property_to_component**](ResourceApi.md#add_property_to_component) | **PUT** /resource/{id}/component/{componentId}/property | 
[**add_property_to_resource**](ResourceApi.md#add_property_to_resource) | **PUT** /resource/{id}/property | 
[**create_resource**](ResourceApi.md#create_resource) | **POST** /resource | 
[**delete_component_from_resource**](ResourceApi.md#delete_component_from_resource) | **DELETE** /resource/{id}/component/{componentId} | 
[**delete_property_from_resource**](ResourceApi.md#delete_property_from_resource) | **DELETE** /resource/{id}/property/{propertyId} | 
[**delete_property_of_component**](ResourceApi.md#delete_property_of_component) | **DELETE** /resource/{id}/component/{componentId}/property/{propertyId} | 
[**delete_resource**](ResourceApi.md#delete_resource) | **DELETE** /resource/{id} | 
[**get_resource**](ResourceApi.md#get_resource) | **GET** /resource/{id} | 
[**get_resource_status**](ResourceApi.md#get_resource_status) | **GET** /resource/{id}/status | 
[**get_role_for_resource**](ResourceApi.md#get_role_for_resource) | **GET** /resource/{id}/role/{userId} | 
[**list_resources**](ResourceApi.md#list_resources) | **GET** /resources | 
[**share_resource**](ResourceApi.md#share_resource) | **POST** /resource/{id}/accessible-to | 
[**unshare_resource**](ResourceApi.md#unshare_resource) | **PATCH** /resource/{id}/accessible-to/{principalId} | 
[**update_property_of_component**](ResourceApi.md#update_property_of_component) | **PATCH** /resource/{id}/component/{componentId}/property/{propertyId} | 
[**update_property_of_resource**](ResourceApi.md#update_property_of_resource) | **PATCH** /resource/{id}/property/{propertyId} | 
[**update_resource**](ResourceApi.md#update_resource) | **PATCH** /resource/{id} | 

# **add_component_to_resource**
> InlineResponse2003 add_component_to_resource(body, id)



Add a component to an existing resource. 

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddComponentToResourceBody() # AddComponentToResourceBody | A JSON object containing the necessary properties to add a property to the resource.
id = 'id_example' # str | The `_id` of the resource the component is being added to.

try:
    api_response = api_instance.add_component_to_resource(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->add_component_to_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddComponentToResourceBody**](AddComponentToResourceBody.md)| A JSON object containing the necessary properties to add a property to the resource. | 
 **id** | **str**| The &#x60;_id&#x60; of the resource the component is being added to. | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_property_to_component**
> PropertyAddedToComponent add_property_to_component(body, id, component_id)



Add a property to a component to a resource. 

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddPropertyToComponentOfResourceBody() # AddPropertyToComponentOfResourceBody | A JSON object containing the necessary properties to add a property to the resource.
id = 'id_example' # str | The `_id` of the resource to add a component to.
component_id = 'component_id_example' # str | The `_id` of the component the property will be added to.

try:
    api_response = api_instance.add_property_to_component(body, id, component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->add_property_to_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddPropertyToComponentOfResourceBody**](AddPropertyToComponentOfResourceBody.md)| A JSON object containing the necessary properties to add a property to the resource. | 
 **id** | **str**| The &#x60;_id&#x60; of the resource to add a component to. | 
 **component_id** | **str**| The &#x60;_id&#x60; of the component the property will be added to. | 

### Return type

[**PropertyAddedToComponent**](PropertyAddedToComponent.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_property_to_resource**
> PropertyAddedToResource add_property_to_resource(body, id)



Add a property to an existing resource. Only immutable properties can be added to the resource with this method. 

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddPropertyToResourceBody() # AddPropertyToResourceBody | A JSON object containing the necessary properties to add a property to the resource.
id = 'id_example' # str | The `_id` of the resource to add a property to.

try:
    api_response = api_instance.add_property_to_resource(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->add_property_to_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddPropertyToResourceBody**](AddPropertyToResourceBody.md)| A JSON object containing the necessary properties to add a property to the resource. | 
 **id** | **str**| The &#x60;_id&#x60; of the resource to add a property to. | 

### Return type

[**PropertyAddedToResource**](PropertyAddedToResource.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_resource**
> Resource create_resource(body)



Create a new resource. It creates a new resource in inventory.

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
body = swagger_client.NewResourceBody() # NewResourceBody | A JSON object containing the necessary properties to create a new resource.

try:
    api_response = api_instance.create_resource(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->create_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewResourceBody**](NewResourceBody.md)| A JSON object containing the necessary properties to create a new resource. | 

### Return type

[**Resource**](Resource.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_component_from_resource**
> SuccessfullyDelete delete_component_from_resource(body, id, component_id)



Delete a component from an existing resource.

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
body = NULL # object | A JSON object containing the necessary properties to delete a component from the resource.
id = 'id_example' # str | The `_id` of the resource related to a component.
component_id = 'component_id_example' # str | The `_id` of the component.

try:
    api_response = api_instance.delete_component_from_resource(body, id, component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->delete_component_from_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| A JSON object containing the necessary properties to delete a component from the resource. | 
 **id** | **str**| The &#x60;_id&#x60; of the resource related to a component. | 
 **component_id** | **str**| The &#x60;_id&#x60; of the component. | 

### Return type

[**SuccessfullyDelete**](SuccessfullyDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property_from_resource**
> SuccessfullyDelete delete_property_from_resource(body, id, property_id)



Removes a property from the resource.

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
body = NULL # object | A JSON object containing the necessary properties to delete a property from the resource.
id = 'id_example' # str | The `_id` of the resource related to a component.
property_id = 'property_id_example' # str | The `_id` of the property.

try:
    api_response = api_instance.delete_property_from_resource(body, id, property_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->delete_property_from_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| A JSON object containing the necessary properties to delete a property from the resource. | 
 **id** | **str**| The &#x60;_id&#x60; of the resource related to a component. | 
 **property_id** | **str**| The &#x60;_id&#x60; of the property. | 

### Return type

[**SuccessfullyDelete**](SuccessfullyDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property_of_component**
> SuccessfullyDelete delete_property_of_component(body, id, component_id, property_id)



Delete a property of a component of an existing resource.

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
body = NULL # object | A JSON object containing the necessary properties to delete a property of a component from the resource.
id = 'id_example' # str | The `_id` of the resource related to a component.
component_id = 'component_id_example' # str | The `_id` of the component.
property_id = 'property_id_example' # str | The `_id` of the property.

try:
    api_response = api_instance.delete_property_of_component(body, id, component_id, property_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->delete_property_of_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| A JSON object containing the necessary properties to delete a property of a component from the resource. | 
 **id** | **str**| The &#x60;_id&#x60; of the resource related to a component. | 
 **component_id** | **str**| The &#x60;_id&#x60; of the component. | 
 **property_id** | **str**| The &#x60;_id&#x60; of the property. | 

### Return type

[**SuccessfullyDelete**](SuccessfullyDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource**
> InlineResponse20017 delete_resource(id)



Deletes existing resource from inventory. The deleted resource will remain in experiments where it had been used. It will no longer be available for future experiments. 

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the resource to be deleted.

try:
    api_response = api_instance.delete_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->delete_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the resource to be deleted. | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource**
> Resource get_resource(id)



Returns the detail for the specified resource.

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the resource.

try:
    api_response = api_instance.get_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->get_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the resource. | 

### Return type

[**Resource**](Resource.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_status**
> ResourceStatus get_resource_status(id)



Returns the status for the specified resource. Provides a list of all experiments in which the specified resource has been used, along with the latest active step (activity), and/or the latest stopped step (activity)

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the resource.

try:
    api_response = api_instance.get_resource_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->get_resource_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the resource. | 

### Return type

[**ResourceStatus**](ResourceStatus.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_for_resource**
> Role get_role_for_resource(id, user_id)



Returns the highest role for the specified user for the specific resource.

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the resource.
user_id = 'user_id_example' # str | The `_id` of the user.

try:
    api_response = api_instance.get_role_for_resource(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->get_role_for_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the resource. | 
 **user_id** | **str**| The &#x60;_id&#x60; of the user. | 

### Return type

[**Role**](Role.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_resources**
> Resources list_resources(sort=sort, fields=fields, name=name, limit=limit, offset=offset, before=before, after=after, creator=creator, public=public, deleted=deleted, inventory=inventory, resource_type_id=resource_type_id, experiment_id=experiment_id, activity_id=activity_id, run_id=run_id, top_group_id=top_group_id, runlabel=runlabel, label=label, shareable=shareable)



List or search the user's resource inventory.

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
sort = ['sort_example'] # list[str] | The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (`-`). A comma separated list may be used to sort by more than one field (e.g. `process_name,-label`.  (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)
name = 'name_example' # str | Limits the result set to items with this exact name (case insensitive). (optional)
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)
creator = 'creator_example' # str | Limits the result set to items created by the user with this username. (optional)
public = true # bool | Toggles the result set between public and private data. Default value is `false` (optional)
deleted = true # bool | Toggles the result set between deleted and non-deleted items. Default value is `false`, to only show non-deleted items.  (optional)
inventory = true # bool | Limits the result set to items that are either inventory or run specific samples of the inventory. `inventory=1` will filter the results to include only inventory items. `inventory=0` will filter the results to include run specific samples.  (optional)
resource_type_id = 'resource_type_id_example' # str | Limits the result set to items associated with the `_id` of the specified resource type (optional)
experiment_id = 'experiment_id_example' # str | Limits the result set to items associated with the `_id` of the specified experiment. (optional)
activity_id = 'activity_id_example' # str | Limits the result set to items associated with the `_id` of the specified activity. Refers to the Process level Activity `_id`. (optional)
run_id = 'run_id_example' # str | Limits the result set to items associated with the `_id` of the specified run. (optional)
top_group_id = 'top_group_id_example' # str | Limits the result set to items associated with the `_id` of the specified process (optional)
runlabel = 'runlabel_example' # str | Limits the result set to the specified runLabel (optional)
label = 'label_example' # str | Limits the result set to the specified label (optional)
shareable = true # bool | Limits the records returned to the ones that are shareable. (optional)

try:
    api_response = api_instance.list_resources(sort=sort, fields=fields, name=name, limit=limit, offset=offset, before=before, after=after, creator=creator, public=public, deleted=deleted, inventory=inventory, resource_type_id=resource_type_id, experiment_id=experiment_id, activity_id=activity_id, run_id=run_id, top_group_id=top_group_id, runlabel=runlabel, label=label, shareable=shareable)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->list_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | [**list[str]**](str.md)| The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (&#x60;-&#x60;). A comma separated list may be used to sort by more than one field (e.g. &#x60;process_name,-label&#x60;.  | [optional] 
 **fields** | **str**| Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use &#x60;fields&#x3D;name,created&#x60;. To exclude the name and created fields from the results use &#x60;fields&#x3D;-name,-created&#x60;. Inclusion and exclusion options can not be set in the same query.  | [optional] 
 **name** | **str**| Limits the result set to items with this exact name (case insensitive). | [optional] 
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 
 **before** | **str**| Limits the result set to items created on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  | [optional] 
 **after** | **str**| Limits the result set to items created on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;).  | [optional] 
 **creator** | **str**| Limits the result set to items created by the user with this username. | [optional] 
 **public** | **bool**| Toggles the result set between public and private data. Default value is &#x60;false&#x60; | [optional] 
 **deleted** | **bool**| Toggles the result set between deleted and non-deleted items. Default value is &#x60;false&#x60;, to only show non-deleted items.  | [optional] 
 **inventory** | **bool**| Limits the result set to items that are either inventory or run specific samples of the inventory. &#x60;inventory&#x3D;1&#x60; will filter the results to include only inventory items. &#x60;inventory&#x3D;0&#x60; will filter the results to include run specific samples.  | [optional] 
 **resource_type_id** | **str**| Limits the result set to items associated with the &#x60;_id&#x60; of the specified resource type | [optional] 
 **experiment_id** | **str**| Limits the result set to items associated with the &#x60;_id&#x60; of the specified experiment. | [optional] 
 **activity_id** | **str**| Limits the result set to items associated with the &#x60;_id&#x60; of the specified activity. Refers to the Process level Activity &#x60;_id&#x60;. | [optional] 
 **run_id** | **str**| Limits the result set to items associated with the &#x60;_id&#x60; of the specified run. | [optional] 
 **top_group_id** | **str**| Limits the result set to items associated with the &#x60;_id&#x60; of the specified process | [optional] 
 **runlabel** | **str**| Limits the result set to the specified runLabel | [optional] 
 **label** | **str**| Limits the result set to the specified label | [optional] 
 **shareable** | **bool**| Limits the records returned to the ones that are shareable. | [optional] 

### Return type

[**Resources**](Resources.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_resource**
> SuccessShared share_resource(body, id)



Share an existing resource with a user, team, or organization

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
body = swagger_client.ShareResourceBody() # ShareResourceBody | A JSON object containing the necessary properties to share the resource.
id = 'id_example' # str | The `_id` of the resource

try:
    api_response = api_instance.share_resource(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->share_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShareResourceBody**](ShareResourceBody.md)| A JSON object containing the necessary properties to share the resource. | 
 **id** | **str**| The &#x60;_id&#x60; of the resource | 

### Return type

[**SuccessShared**](SuccessShared.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unshare_resource**
> SuccessfullyUnshared unshare_resource(body, id, principal_id)



Revoke access to an existing resource from a user, team, or organization

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
body = swagger_client.UnshareResourceBody() # UnshareResourceBody | A JSON object containing the necessary properties to revoke access to the resource.
id = 'id_example' # str | The `_id` of the resource.
principal_id = 'principal_id_example' # str | The `_id` of the entity being revoked access to the resource.

try:
    api_response = api_instance.unshare_resource(body, id, principal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->unshare_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnshareResourceBody**](UnshareResourceBody.md)| A JSON object containing the necessary properties to revoke access to the resource. | 
 **id** | **str**| The &#x60;_id&#x60; of the resource. | 
 **principal_id** | **str**| The &#x60;_id&#x60; of the entity being revoked access to the resource. | 

### Return type

[**SuccessfullyUnshared**](SuccessfullyUnshared.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_property_of_component**
> ComponentPropertyUpdated update_property_of_component(body, id, component_id, property_id)



Updates the property of a component of an existing resource. 

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdatePropertyOfComponentOfResourceBody() # UpdatePropertyOfComponentOfResourceBody | A JSON object containing the necessary properties to update the property of a component of a resource.
id = 'id_example' # str | The `_id` of the resource related to a component.
component_id = 'component_id_example' # str | The `_id` of the component.
property_id = 'property_id_example' # str | The `_id` of the property.

try:
    api_response = api_instance.update_property_of_component(body, id, component_id, property_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->update_property_of_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePropertyOfComponentOfResourceBody**](UpdatePropertyOfComponentOfResourceBody.md)| A JSON object containing the necessary properties to update the property of a component of a resource. | 
 **id** | **str**| The &#x60;_id&#x60; of the resource related to a component. | 
 **component_id** | **str**| The &#x60;_id&#x60; of the component. | 
 **property_id** | **str**| The &#x60;_id&#x60; of the property. | 

### Return type

[**ComponentPropertyUpdated**](ComponentPropertyUpdated.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_property_of_resource**
> PropertyUpdated update_property_of_resource(body, id, property_id)



Updates the property of an existing resource. 

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdatePropertyOfResourceBody() # UpdatePropertyOfResourceBody | A JSON object containing the necessary properties to update a property of the resource.
id = 'id_example' # str | The `_id` of the resource related to a component.
property_id = 'property_id_example' # str | The `_id` of the property.

try:
    api_response = api_instance.update_property_of_resource(body, id, property_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->update_property_of_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePropertyOfResourceBody**](UpdatePropertyOfResourceBody.md)| A JSON object containing the necessary properties to update a property of the resource. | 
 **id** | **str**| The &#x60;_id&#x60; of the resource related to a component. | 
 **property_id** | **str**| The &#x60;_id&#x60; of the property. | 

### Return type

[**PropertyUpdated**](PropertyUpdated.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource**
> Resource update_resource(body, id)



Updates an existing resource. You must provide the complete list of immutable properties and components. Old values will be deleted and replaced. Run data that's already been collected will not be deleted. 

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
api_instance = swagger_client.ResourceApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateResourceBody() # UpdateResourceBody | A JSON object containing the necessary properties to update the resource.
id = 'id_example' # str | The `_id` of the resource to update.

try:
    api_response = api_instance.update_resource(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->update_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateResourceBody**](UpdateResourceBody.md)| A JSON object containing the necessary properties to update the resource. | 
 **id** | **str**| The &#x60;_id&#x60; of the resource to update. | 

### Return type

[**Resource**](Resource.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

