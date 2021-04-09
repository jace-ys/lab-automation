# riffyn_nexus_sdk_v1.UnitApi

All URIs are relative to *deployment_url/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_unit**](UnitApi.md#create_unit) | **POST** /unit | createUnit
[**get_role_for_unit**](UnitApi.md#get_role_for_unit) | **GET** /unit/{id}/role/{userId} | getRoleForUnit
[**get_unit**](UnitApi.md#get_unit) | **GET** /unit/{id} | getUnit
[**list_units**](UnitApi.md#list_units) | **GET** /units | listUnits
[**share_unit**](UnitApi.md#share_unit) | **POST** /unit/{id}/accessible-to | shareUnit
[**unshare_unit**](UnitApi.md#unshare_unit) | **PATCH** /unit/{id}/accessible-to/{principalId} | unshareUnit
[**update_unit**](UnitApi.md#update_unit) | **PATCH** /unit/{id} | updateUnit

# **create_unit**
> Unit create_unit(body)

createUnit

Create a new unit.

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
api_instance = riffyn_nexus_sdk_v1.UnitApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.NewUnitBody() # NewUnitBody | A JSON object containing the necessary properties to create a new unit.

try:
    # createUnit
    api_response = api_instance.create_unit(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitApi->create_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewUnitBody**](NewUnitBody.md)| A JSON object containing the necessary properties to create a new unit. | 

### Return type

[**Unit**](Unit.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_for_unit**
> Role get_role_for_unit(id, user_id)

getRoleForUnit

Returns the highest role for the specified user for the specific unit.

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
api_instance = riffyn_nexus_sdk_v1.UnitApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the unit.
user_id = 'user_id_example' # str | The `_id` of the user.

try:
    # getRoleForUnit
    api_response = api_instance.get_role_for_unit(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitApi->get_role_for_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the unit. | 
 **user_id** | **str**| The &#x60;_id&#x60; of the user. | 

### Return type

[**Role**](Role.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unit**
> Unit get_unit(id)

getUnit

Returns the detail for the specified unit.

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
api_instance = riffyn_nexus_sdk_v1.UnitApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the unit.

try:
    # getUnit
    api_response = api_instance.get_unit(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitApi->get_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the unit. | 

### Return type

[**Unit**](Unit.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_units**
> Units list_units(sort=sort, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator, deleted=deleted, public=public)

listUnits

List or search the user's units. 

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
api_instance = riffyn_nexus_sdk_v1.UnitApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
sort = ['sort_example'] # list[str] | The sort order to use for the result set. To sort in descending order, prefix the field name with a dash(`-`). A comma separated list may be used to sort by more than one field (e.g. `name,-creator`).  (optional)
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)
name = 'name_example' # str | Limits the result set to items with this exact name (case insensitive). (optional)
creator = 'creator_example' # str | Limits the result set to items created by the user with this username. (optional)
deleted = true # bool | Toggles the result set between deleted and non-deleted items. Default value is `false`, to only show non-deleted items.  (optional)
public = true # bool | Toggles the result set between public and private data. Default value is `false` (optional)

try:
    # listUnits
    api_response = api_instance.list_units(sort=sort, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator, deleted=deleted, public=public)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitApi->list_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | [**list[str]**](str.md)| The sort order to use for the result set. To sort in descending order, prefix the field name with a dash(&#x60;-&#x60;). A comma separated list may be used to sort by more than one field (e.g. &#x60;name,-creator&#x60;).  | [optional] 
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 
 **before** | **str**| Limits the result set to items created on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  | [optional] 
 **after** | **str**| Limits the result set to items created on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;).  | [optional] 
 **fields** | **str**| Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use &#x60;fields&#x3D;name,created&#x60;. To exclude the name and created fields from the results use &#x60;fields&#x3D;-name,-created&#x60;. Inclusion and exclusion options can not be set in the same query.  | [optional] 
 **name** | **str**| Limits the result set to items with this exact name (case insensitive). | [optional] 
 **creator** | **str**| Limits the result set to items created by the user with this username. | [optional] 
 **deleted** | **bool**| Toggles the result set between deleted and non-deleted items. Default value is &#x60;false&#x60;, to only show non-deleted items.  | [optional] 
 **public** | **bool**| Toggles the result set between public and private data. Default value is &#x60;false&#x60; | [optional] 

### Return type

[**Units**](Units.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_unit**
> SuccessfullyShare share_unit(body, id)

shareUnit

Share an existing unit with a user, team, or organization.

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
api_instance = riffyn_nexus_sdk_v1.UnitApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.ShareUnitBody() # ShareUnitBody | A JSON object containing the necessary properties to share the unit.
id = 'id_example' # str | The `_id` of the unit to share.

try:
    # shareUnit
    api_response = api_instance.share_unit(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitApi->share_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShareUnitBody**](ShareUnitBody.md)| A JSON object containing the necessary properties to share the unit. | 
 **id** | **str**| The &#x60;_id&#x60; of the unit to share. | 

### Return type

[**SuccessfullyShare**](SuccessfullyShare.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unshare_unit**
> SuccessfullyUnshared unshare_unit(body, id, principal_id)

unshareUnit

Revoke access to an existing unit from a user, team, or organization.

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
api_instance = riffyn_nexus_sdk_v1.UnitApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.UnshareUnitBody() # UnshareUnitBody | A JSON object containing the necessary properties to revoke access to the unit.
id = 'id_example' # str | The `_id` of the unit to be revoked access to.
principal_id = 'principal_id_example' # str | The `_id` of the entity being revoked access to the unit.

try:
    # unshareUnit
    api_response = api_instance.unshare_unit(body, id, principal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitApi->unshare_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnshareUnitBody**](UnshareUnitBody.md)| A JSON object containing the necessary properties to revoke access to the unit. | 
 **id** | **str**| The &#x60;_id&#x60; of the unit to be revoked access to. | 
 **principal_id** | **str**| The &#x60;_id&#x60; of the entity being revoked access to the unit. | 

### Return type

[**SuccessfullyUnshared**](SuccessfullyUnshared.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_unit**
> Unit update_unit(body, id)

updateUnit

Update an existing unit.

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
api_instance = riffyn_nexus_sdk_v1.UnitApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.UpdateUnitBody() # UpdateUnitBody | A JSON object containing the necessary properties to update the unit.
id = 'id_example' # str | The `_id` of the unit to update.

try:
    # updateUnit
    api_response = api_instance.update_unit(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitApi->update_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUnitBody**](UpdateUnitBody.md)| A JSON object containing the necessary properties to update the unit. | 
 **id** | **str**| The &#x60;_id&#x60; of the unit to update. | 

### Return type

[**Unit**](Unit.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

