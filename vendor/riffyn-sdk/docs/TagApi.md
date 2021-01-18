# swagger_client.TagApi

All URIs are relative to *https://api.riffyn.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag**](TagApi.md#create_tag) | **POST** /tag | 
[**delete_tag**](TagApi.md#delete_tag) | **DELETE** /tag/{id} | 
[**get_tag**](TagApi.md#get_tag) | **GET** /tag/{id} | 
[**list_entities_for_tag**](TagApi.md#list_entities_for_tag) | **GET** /tag/{id}/entities | 
[**list_tags**](TagApi.md#list_tags) | **GET** /tags | 
[**update_tag**](TagApi.md#update_tag) | **PATCH** /tag/{id} | 

# **create_tag**
> Tag create_tag(body)



Create a tag for the user.

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
body = swagger_client.TagBody() # TagBody | A JSON object containing the necessary properties to create a new tag.

try:
    api_response = api_instance.create_tag(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->create_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TagBody**](TagBody.md)| A JSON object containing the necessary properties to create a new tag. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> InlineResponse20018 delete_tag(id)



Delete an existing tag.

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the tag.

try:
    api_response = api_instance.delete_tag(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->delete_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the tag. | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> Tag get_tag(id)



Returns the detail for the specified tag.

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the tag.

try:
    api_response = api_instance.get_tag(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->get_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the tag. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entities_for_tag**
> EntitiesForTag list_entities_for_tag(id)



Returns all the entities with the specified tag.

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the tag.

try:
    api_response = api_instance.list_entities_for_tag(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->list_entities_for_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the tag. | 

### Return type

[**EntitiesForTag**](EntitiesForTag.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags**
> Tags list_tags(name=name, fields=fields, creator=creator, sort=sort, limit=limit, offset=offset, before=before, after=after, modified_before=modified_before, modified_after=modified_after, public=public)



Returns all tags for the user.

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Limits the result set to items with this exact name (case insensitive). (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)
creator = 'creator_example' # str | Limits the result set to items created by the user with this username. (optional)
sort = ['sort_example'] # list[str] | The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (`-`). A comma separated list may be used to sort by more than one field (e.g. `process_name,-label`).  (optional)
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)
modified_before = 'modified_before_example' # str | Limits the result set to items modified on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch, `1507650828`).  (optional)
modified_after = 'modified_after_example' # str | Limits the result set to items modified on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch, `1507650828`).  (optional)
public = true # bool | Toggles the result set between public and private data. Default value is `false` (optional)

try:
    api_response = api_instance.list_tags(name=name, fields=fields, creator=creator, sort=sort, limit=limit, offset=offset, before=before, after=after, modified_before=modified_before, modified_after=modified_after, public=public)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->list_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Limits the result set to items with this exact name (case insensitive). | [optional] 
 **fields** | **str**| Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use &#x60;fields&#x3D;name,created&#x60;. To exclude the name and created fields from the results use &#x60;fields&#x3D;-name,-created&#x60;. Inclusion and exclusion options can not be set in the same query.  | [optional] 
 **creator** | **str**| Limits the result set to items created by the user with this username. | [optional] 
 **sort** | [**list[str]**](str.md)| The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (&#x60;-&#x60;). A comma separated list may be used to sort by more than one field (e.g. &#x60;process_name,-label&#x60;).  | [optional] 
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 
 **before** | **str**| Limits the result set to items created on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  | [optional] 
 **after** | **str**| Limits the result set to items created on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;).  | [optional] 
 **modified_before** | **str**| Limits the result set to items modified on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60; or epoch, &#x60;1507650828&#x60;).  | [optional] 
 **modified_after** | **str**| Limits the result set to items modified on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60; or epoch, &#x60;1507650828&#x60;).  | [optional] 
 **public** | **bool**| Toggles the result set between public and private data. Default value is &#x60;false&#x60; | [optional] 

### Return type

[**Tags**](Tags.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> Tag update_tag(body, id)



Update an existing tag.

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
body = swagger_client.TagBody() # TagBody | A JSON object containing the necessary properties to update a tag.
id = 'id_example' # str | The `_id` of the tag.

try:
    api_response = api_instance.update_tag(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->update_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TagBody**](TagBody.md)| A JSON object containing the necessary properties to update a tag. | 
 **id** | **str**| The &#x60;_id&#x60; of the tag. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

