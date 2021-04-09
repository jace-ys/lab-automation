# riffyn_nexus_sdk_v1.UserApi

All URIs are relative to *deployment_url/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_users**](UserApi.md#list_users) | **GET** /users | listUsers

# **list_users**
> Users list_users(fields=fields, sort=sort, limit=limit, offset=offset)

listUsers

List the members of the user's organization.

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
api_instance = riffyn_nexus_sdk_v1.UserApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the username and email fields use `fields=username,emails`. To exclude the username and emails fields from the results use `fields=-username,-emails.`. Inclusion and exclusion options can not be set in the same query.  (optional)
sort = ['sort_example'] # list[str] | The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (`-`). A comma separated list may be used to sort by more than one field (e.g. `username,-org`).  (optional)
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)

try:
    # listUsers
    api_response = api_instance.list_users(fields=fields, sort=sort, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Modifies the result set to exclude or include the specified fields. E.g: To return only the the username and email fields use &#x60;fields&#x3D;username,emails&#x60;. To exclude the username and emails fields from the results use &#x60;fields&#x3D;-username,-emails.&#x60;. Inclusion and exclusion options can not be set in the same query.  | [optional] 
 **sort** | [**list[str]**](str.md)| The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (&#x60;-&#x60;). A comma separated list may be used to sort by more than one field (e.g. &#x60;username,-org&#x60;).  | [optional] 
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 

### Return type

[**Users**](Users.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

