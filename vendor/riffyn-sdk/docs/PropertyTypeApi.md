# swagger_client.PropertyTypeApi

All URIs are relative to *https://api.riffyn.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_unit_to_property_type**](PropertyTypeApi.md#add_unit_to_property_type) | **PUT** /property-type/{id}/unit | 
[**create_property_type**](PropertyTypeApi.md#create_property_type) | **POST** /property-type | 
[**get_property_type**](PropertyTypeApi.md#get_property_type) | **GET** /property-type/{id} | 
[**get_role_for_property_type**](PropertyTypeApi.md#get_role_for_property_type) | **GET** /property-type/{id}/role/{userId} | 
[**list_property_type_units**](PropertyTypeApi.md#list_property_type_units) | **GET** /property-type/{id}/units | 
[**list_property_types**](PropertyTypeApi.md#list_property_types) | **GET** /property-types | 
[**remove_unit_from_property_type**](PropertyTypeApi.md#remove_unit_from_property_type) | **DELETE** /property-type/{id}/unit/{unitId} | 
[**share_property_type**](PropertyTypeApi.md#share_property_type) | **POST** /property-type/{id}/accessible-to | 
[**unshare_property_type**](PropertyTypeApi.md#unshare_property_type) | **PATCH** /property-type/{id}/accessible-to/{principalId} | 
[**update_property_type**](PropertyTypeApi.md#update_property_type) | **PATCH** /property-type/{id} | 

# **add_unit_to_property_type**
> SuccessMessage add_unit_to_property_type(id, body=body)



Add a unit to a property type.

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
api_instance = swagger_client.PropertyTypeApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the property type.
body = swagger_client.NewPropertyUnitBody() # NewPropertyUnitBody | A JSON object containing the `_id` of the unit to be added to the property type. (optional)

try:
    api_response = api_instance.add_unit_to_property_type(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyTypeApi->add_unit_to_property_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the property type. | 
 **body** | [**NewPropertyUnitBody**](NewPropertyUnitBody.md)| A JSON object containing the &#x60;_id&#x60; of the unit to be added to the property type. | [optional] 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_property_type**
> PropertyType create_property_type(body)



Create a new property type.

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
api_instance = swagger_client.PropertyTypeApi(swagger_client.ApiClient(configuration))
body = swagger_client.NewPropertyTypeBody() # NewPropertyTypeBody | A JSON object containing the necessary properties to create a new property type.

try:
    api_response = api_instance.create_property_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyTypeApi->create_property_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewPropertyTypeBody**](NewPropertyTypeBody.md)| A JSON object containing the necessary properties to create a new property type. | 

### Return type

[**PropertyType**](PropertyType.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property_type**
> PropertyType get_property_type(id)



Returns the detail for the specified property type.

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
api_instance = swagger_client.PropertyTypeApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the property type.

try:
    api_response = api_instance.get_property_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyTypeApi->get_property_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the property type. | 

### Return type

[**PropertyType**](PropertyType.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_for_property_type**
> Role get_role_for_property_type(id, user_id)



Returns the highest role for the specified user for the specific property type.

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
api_instance = swagger_client.PropertyTypeApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the property type.
user_id = 'user_id_example' # str | The `_id` of the user.

try:
    api_response = api_instance.get_role_for_property_type(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyTypeApi->get_role_for_property_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the property type. | 
 **user_id** | **str**| The &#x60;_id&#x60; of the user. | 

### Return type

[**Role**](Role.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_property_type_units**
> UnitsForProperty list_property_type_units(id, limit=limit, offset=offset, sort=sort, fields=fields)



List or search the units associated with a property type.

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
api_instance = swagger_client.PropertyTypeApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the property type.
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
sort = ['sort_example'] # list[str] | The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (`-`). A comma separated list may be used to sort by more than one field (e.g. `process_name,-label`).  (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)

try:
    api_response = api_instance.list_property_type_units(id, limit=limit, offset=offset, sort=sort, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyTypeApi->list_property_type_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the property type. | 
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 
 **sort** | [**list[str]**](str.md)| The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (&#x60;-&#x60;). A comma separated list may be used to sort by more than one field (e.g. &#x60;process_name,-label&#x60;).  | [optional] 
 **fields** | **str**| Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use &#x60;fields&#x3D;name,created&#x60;. To exclude the name and created fields from the results use &#x60;fields&#x3D;-name,-created&#x60;. Inclusion and exclusion options can not be set in the same query.  | [optional] 

### Return type

[**UnitsForProperty**](UnitsForProperty.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_property_types**
> PropertyTypes list_property_types(limit=limit, offset=offset, sort=sort, before=before, after=after, fields=fields, name=name, creator=creator, deleted=deleted, public=public)



List or search the user's property types.

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
api_instance = swagger_client.PropertyTypeApi(swagger_client.ApiClient(configuration))
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
sort = ['sort_example'] # list[str] | The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (`-`). A comma separated list may be used to sort by more than one field (e.g. `process_name,-label`).  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)
name = 'name_example' # str | Limits the result set to items with this exact name (case insensitive). (optional)
creator = 'creator_example' # str | Limits the result set to items created by the user with this username. (optional)
deleted = true # bool | Toggles the result set between deleted and non-deleted items. Default value is `false`, to only show non-deleted items.  (optional)
public = true # bool | Toggles the result set between public and private data. Default value is `false` (optional)

try:
    api_response = api_instance.list_property_types(limit=limit, offset=offset, sort=sort, before=before, after=after, fields=fields, name=name, creator=creator, deleted=deleted, public=public)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyTypeApi->list_property_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 
 **sort** | [**list[str]**](str.md)| The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (&#x60;-&#x60;). A comma separated list may be used to sort by more than one field (e.g. &#x60;process_name,-label&#x60;).  | [optional] 
 **before** | **str**| Limits the result set to items created on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  | [optional] 
 **after** | **str**| Limits the result set to items created on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;).  | [optional] 
 **fields** | **str**| Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use &#x60;fields&#x3D;name,created&#x60;. To exclude the name and created fields from the results use &#x60;fields&#x3D;-name,-created&#x60;. Inclusion and exclusion options can not be set in the same query.  | [optional] 
 **name** | **str**| Limits the result set to items with this exact name (case insensitive). | [optional] 
 **creator** | **str**| Limits the result set to items created by the user with this username. | [optional] 
 **deleted** | **bool**| Toggles the result set between deleted and non-deleted items. Default value is &#x60;false&#x60;, to only show non-deleted items.  | [optional] 
 **public** | **bool**| Toggles the result set between public and private data. Default value is &#x60;false&#x60; | [optional] 

### Return type

[**PropertyTypes**](PropertyTypes.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_unit_from_property_type**
> UnitRemoved remove_unit_from_property_type(id, unit_id)



Remove the unit associated with a property type.

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
api_instance = swagger_client.PropertyTypeApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the property type.
unit_id = 'unit_id_example' # str | The `_id` of the unit to be removed.

try:
    api_response = api_instance.remove_unit_from_property_type(id, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyTypeApi->remove_unit_from_property_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the property type. | 
 **unit_id** | **str**| The &#x60;_id&#x60; of the unit to be removed. | 

### Return type

[**UnitRemoved**](UnitRemoved.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_property_type**
> SuccessfullyShare share_property_type(body, id)



Share an existing property type with a user, team, or organization

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
api_instance = swagger_client.PropertyTypeApi(swagger_client.ApiClient(configuration))
body = swagger_client.SharePropertyTypeBody() # SharePropertyTypeBody | A JSON object containing the necessary properties to share the property type.
id = 'id_example' # str | The `_id` of the property type.

try:
    api_response = api_instance.share_property_type(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyTypeApi->share_property_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SharePropertyTypeBody**](SharePropertyTypeBody.md)| A JSON object containing the necessary properties to share the property type. | 
 **id** | **str**| The &#x60;_id&#x60; of the property type. | 

### Return type

[**SuccessfullyShare**](SuccessfullyShare.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unshare_property_type**
> SuccessfullyUnshared unshare_property_type(body, id, principal_id)



Revoke access to an existing property type from a user, team, or organization

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
api_instance = swagger_client.PropertyTypeApi(swagger_client.ApiClient(configuration))
body = swagger_client.UnsharePropertyTypeBody() # UnsharePropertyTypeBody | A JSON object containing the necessary properties to revoke access to the property type.
id = 'id_example' # str | The `_id` of the property type to be revoked
principal_id = 'principal_id_example' # str | The `_id` of the entity being revoked access to the property type.

try:
    api_response = api_instance.unshare_property_type(body, id, principal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyTypeApi->unshare_property_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnsharePropertyTypeBody**](UnsharePropertyTypeBody.md)| A JSON object containing the necessary properties to revoke access to the property type. | 
 **id** | **str**| The &#x60;_id&#x60; of the property type to be revoked | 
 **principal_id** | **str**| The &#x60;_id&#x60; of the entity being revoked access to the property type. | 

### Return type

[**SuccessfullyUnshared**](SuccessfullyUnshared.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_property_type**
> PropertyType update_property_type(body, id)



Update an existing property type

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
api_instance = swagger_client.PropertyTypeApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdatePropertyTypeBody() # UpdatePropertyTypeBody | A JSON object containing the necessary properties to update the property.
id = 'id_example' # str | The `_id` of the property type.

try:
    api_response = api_instance.update_property_type(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyTypeApi->update_property_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePropertyTypeBody**](UpdatePropertyTypeBody.md)| A JSON object containing the necessary properties to update the property. | 
 **id** | **str**| The &#x60;_id&#x60; of the property type. | 

### Return type

[**PropertyType**](PropertyType.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

