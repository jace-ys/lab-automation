# swagger_client.ResourceTypeApi

All URIs are relative to *https://api.riffyn.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_type**](ResourceTypeApi.md#create_resource_type) | **POST** /resource-type | 
[**get_resource_type**](ResourceTypeApi.md#get_resource_type) | **GET** /resource-type/{id} | 
[**get_role_for_resource_type**](ResourceTypeApi.md#get_role_for_resource_type) | **GET** /resource-type/{id}/role/{userId} | 
[**list_resource_types**](ResourceTypeApi.md#list_resource_types) | **GET** /resource-types | 
[**share_resource_type**](ResourceTypeApi.md#share_resource_type) | **POST** /resource-type/{id}/accessible-to | 
[**unshare_resource_type**](ResourceTypeApi.md#unshare_resource_type) | **PATCH** /resource-type/{id}/accessible-to/{principalId} | 
[**update_resource_type**](ResourceTypeApi.md#update_resource_type) | **PATCH** /resource-type/{id} | 

# **create_resource_type**
> ResourceType create_resource_type(body)



Create a new resource type.

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
api_instance = swagger_client.ResourceTypeApi(swagger_client.ApiClient(configuration))
body = swagger_client.NewResourceTypeBody() # NewResourceTypeBody | A JSON object containing the necessary properties to create a new resource type.

try:
    api_response = api_instance.create_resource_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceTypeApi->create_resource_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewResourceTypeBody**](NewResourceTypeBody.md)| A JSON object containing the necessary properties to create a new resource type. | 

### Return type

[**ResourceType**](ResourceType.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_type**
> ResourceType get_resource_type(id)



Returns the detail for the specified resource type.

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
api_instance = swagger_client.ResourceTypeApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the resource type.

try:
    api_response = api_instance.get_resource_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceTypeApi->get_resource_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the resource type. | 

### Return type

[**ResourceType**](ResourceType.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_for_resource_type**
> Role get_role_for_resource_type(id, user_id)



Returns the highest role for the specified user for the specific resource-type.

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
api_instance = swagger_client.ResourceTypeApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the resource type.
user_id = 'user_id_example' # str | The `_id` of the user.

try:
    api_response = api_instance.get_role_for_resource_type(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceTypeApi->get_role_for_resource_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the resource type. | 
 **user_id** | **str**| The &#x60;_id&#x60; of the user. | 

### Return type

[**Role**](Role.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_resource_types**
> ResourceTypes list_resource_types(sort=sort, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator, public=public, deleted=deleted)



List or search the user's resource types.

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
api_instance = swagger_client.ResourceTypeApi(swagger_client.ApiClient(configuration))
sort = ['sort_example'] # list[str] | The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (`-`). A comma separated list may be used to sort by more than one field (e.g. `process_name,-label`).  (optional)
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)
name = 'name_example' # str | Limits the result set to items with this exact name (case insensitive). (optional)
creator = 'creator_example' # str | Limits the result set to items created by the user with this username. (optional)
public = true # bool | Toggles the result set between public and private data. Default value is `false` (optional)
deleted = true # bool | Toggles the result set between deleted and non-deleted items. Default value is `false`, to only show non-deleted items.  (optional)

try:
    api_response = api_instance.list_resource_types(sort=sort, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator, public=public, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceTypeApi->list_resource_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | [**list[str]**](str.md)| The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (&#x60;-&#x60;). A comma separated list may be used to sort by more than one field (e.g. &#x60;process_name,-label&#x60;).  | [optional] 
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 
 **before** | **str**| Limits the result set to items created on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  | [optional] 
 **after** | **str**| Limits the result set to items created on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;).  | [optional] 
 **fields** | **str**| Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use &#x60;fields&#x3D;name,created&#x60;. To exclude the name and created fields from the results use &#x60;fields&#x3D;-name,-created&#x60;. Inclusion and exclusion options can not be set in the same query.  | [optional] 
 **name** | **str**| Limits the result set to items with this exact name (case insensitive). | [optional] 
 **creator** | **str**| Limits the result set to items created by the user with this username. | [optional] 
 **public** | **bool**| Toggles the result set between public and private data. Default value is &#x60;false&#x60; | [optional] 
 **deleted** | **bool**| Toggles the result set between deleted and non-deleted items. Default value is &#x60;false&#x60;, to only show non-deleted items.  | [optional] 

### Return type

[**ResourceTypes**](ResourceTypes.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_resource_type**
> SuccessShared share_resource_type(body, id)



Share an existing resource type with a user, team, or organization.

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
api_instance = swagger_client.ResourceTypeApi(swagger_client.ApiClient(configuration))
body = swagger_client.ShareResourceTypeBody() # ShareResourceTypeBody | A JSON object containing the necessary properties to share the property.
id = 'id_example' # str | The `_id` of the resource type.

try:
    api_response = api_instance.share_resource_type(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceTypeApi->share_resource_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShareResourceTypeBody**](ShareResourceTypeBody.md)| A JSON object containing the necessary properties to share the property. | 
 **id** | **str**| The &#x60;_id&#x60; of the resource type. | 

### Return type

[**SuccessShared**](SuccessShared.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unshare_resource_type**
> SuccessfullyUnshared unshare_resource_type(body, id, principal_id)



Revoke access to an existing resource type from a user, team, or organization.

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
api_instance = swagger_client.ResourceTypeApi(swagger_client.ApiClient(configuration))
body = swagger_client.UnshareResourceTypeBody() # UnshareResourceTypeBody | A JSON object containing the necessary properties to revoke access to the reource type.
id = 'id_example' # str | The `_id` of the resource type.
principal_id = 'principal_id_example' # str | The `_id` of the entity being revoked access to the resource type.

try:
    api_response = api_instance.unshare_resource_type(body, id, principal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceTypeApi->unshare_resource_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnshareResourceTypeBody**](UnshareResourceTypeBody.md)| A JSON object containing the necessary properties to revoke access to the reource type. | 
 **id** | **str**| The &#x60;_id&#x60; of the resource type. | 
 **principal_id** | **str**| The &#x60;_id&#x60; of the entity being revoked access to the resource type. | 

### Return type

[**SuccessfullyUnshared**](SuccessfullyUnshared.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource_type**
> ResourceType update_resource_type(body, id)



Updates an existing resource type. You must provide the complete list of immutable properties and components. Old values will be deleted and replaced. Run data that's already been collected will not be deleted. 

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
api_instance = swagger_client.ResourceTypeApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateResourceTypeBody() # UpdateResourceTypeBody | A JSON object containing the necessary properties to update the resource.
id = 'id_example' # str | The `_id` of the resource type to update.

try:
    api_response = api_instance.update_resource_type(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceTypeApi->update_resource_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateResourceTypeBody**](UpdateResourceTypeBody.md)| A JSON object containing the necessary properties to update the resource. | 
 **id** | **str**| The &#x60;_id&#x60; of the resource type to update. | 

### Return type

[**ResourceType**](ResourceType.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

