# riffyn_nexus_sdk_v1.TeamApi

All URIs are relative to *deployment_url/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member_to_team**](TeamApi.md#add_member_to_team) | **POST** /team/{id}/member | addMemberToTeam
[**create_team**](TeamApi.md#create_team) | **POST** /team | createTeam
[**delete_team**](TeamApi.md#delete_team) | **DELETE** /team/{id} | deleteTeam
[**get_role_for_team**](TeamApi.md#get_role_for_team) | **GET** /team/{id}/role/{userId} | getRoleForTeam
[**get_team**](TeamApi.md#get_team) | **GET** /team/{id} | getTeam
[**list_teams**](TeamApi.md#list_teams) | **GET** /teams | listTeams
[**remove_member_from_team**](TeamApi.md#remove_member_from_team) | **DELETE** /team/{id}/member/{memberId} | removeMemberFromTeam
[**share_team**](TeamApi.md#share_team) | **POST** /team/{id}/accessible-to | shareTeam
[**unshare_team**](TeamApi.md#unshare_team) | **PATCH** /team/{id}/accessible-to/{principalId} | unshareTeam
[**update_team**](TeamApi.md#update_team) | **PATCH** /team/{id} | updateTeam

# **add_member_to_team**
> SuccessAddedMember add_member_to_team(body, id)

addMemberToTeam

Add a member to an existing team.

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
api_instance = riffyn_nexus_sdk_v1.TeamApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.AddMemberToTeamBody() # AddMemberToTeamBody | A JSON object containing the necessary properties to add a new member to a team.
id = 'id_example' # str | The `_id` of the team that the member is being added to.

try:
    # addMemberToTeam
    api_response = api_instance.add_member_to_team(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->add_member_to_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddMemberToTeamBody**](AddMemberToTeamBody.md)| A JSON object containing the necessary properties to add a new member to a team. | 
 **id** | **str**| The &#x60;_id&#x60; of the team that the member is being added to. | 

### Return type

[**SuccessAddedMember**](SuccessAddedMember.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_team**
> Team create_team(body)

createTeam

Create a new team. Will add the team creator as a member by default unless a `excludeCreator` parameter is passed.

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
api_instance = riffyn_nexus_sdk_v1.TeamApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.NewTeamBody() # NewTeamBody | A JSON object containing the necessary properties to create a new team.

try:
    # createTeam
    api_response = api_instance.create_team(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->create_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewTeamBody**](NewTeamBody.md)| A JSON object containing the necessary properties to create a new team. | 

### Return type

[**Team**](Team.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team**
> TeamRemove delete_team(id)

deleteTeam

Delete an existing team from the database.

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
api_instance = riffyn_nexus_sdk_v1.TeamApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the team.

try:
    # deleteTeam
    api_response = api_instance.delete_team(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->delete_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the team. | 

### Return type

[**TeamRemove**](TeamRemove.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_for_team**
> Role get_role_for_team(id, user_id)

getRoleForTeam

Returns the highest role for the specified user for the specific team.

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
api_instance = riffyn_nexus_sdk_v1.TeamApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the team.
user_id = 'user_id_example' # str | The `_id` of the user.

try:
    # getRoleForTeam
    api_response = api_instance.get_role_for_team(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_role_for_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the team. | 
 **user_id** | **str**| The &#x60;_id&#x60; of the user. | 

### Return type

[**Role**](Role.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team**
> TeamWithMembers get_team(id)

getTeam

Returns the details for the specified team.

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
api_instance = riffyn_nexus_sdk_v1.TeamApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the team.

try:
    # getTeam
    api_response = api_instance.get_team(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the team. | 

### Return type

[**TeamWithMembers**](TeamWithMembers.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_teams**
> Teams list_teams(sort=sort, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator)

listTeams

List or search the user's teams.

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
api_instance = riffyn_nexus_sdk_v1.TeamApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
sort = ['sort_example'] # list[str] | The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (`-`). A comma separated list may be used to sort by more than one field (e.g. `process_name,-label`.  (optional)
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)
name = 'name_example' # str | Limits the result set to items with this exact name (case insensitive). (optional)
creator = 'creator_example' # str | Limits the result set to items created by the user with this username. (optional)

try:
    # listTeams
    api_response = api_instance.list_teams(sort=sort, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->list_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | [**list[str]**](str.md)| The sort order to use for the result set. To sort in descending order, prefix the field name with a dash (&#x60;-&#x60;). A comma separated list may be used to sort by more than one field (e.g. &#x60;process_name,-label&#x60;.  | [optional] 
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 
 **before** | **str**| Limits the result set to items created on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  | [optional] 
 **after** | **str**| Limits the result set to items created on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;).  | [optional] 
 **fields** | **str**| Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use &#x60;fields&#x3D;name,created&#x60;. To exclude the name and created fields from the results use &#x60;fields&#x3D;-name,-created&#x60;. Inclusion and exclusion options can not be set in the same query.  | [optional] 
 **name** | **str**| Limits the result set to items with this exact name (case insensitive). | [optional] 
 **creator** | **str**| Limits the result set to items created by the user with this username. | [optional] 

### Return type

[**Teams**](Teams.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_member_from_team**
> SuccessfullyDelete remove_member_from_team(body, id, member_id)

removeMemberFromTeam

Remove a member from an existing team.

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
api_instance = riffyn_nexus_sdk_v1.TeamApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = NULL # object | The member type from the team.
id = 'id_example' # str | The `_id` of the team.
member_id = 'member_id_example' # str | The `_id` of the team.

try:
    # removeMemberFromTeam
    api_response = api_instance.remove_member_from_team(body, id, member_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->remove_member_from_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| The member type from the team. | 
 **id** | **str**| The &#x60;_id&#x60; of the team. | 
 **member_id** | **str**| The &#x60;_id&#x60; of the team. | 

### Return type

[**SuccessfullyDelete**](SuccessfullyDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_team**
> SuccessfullyShare share_team(body, id)

shareTeam

Share an existing team with a user, team, or organization.

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
api_instance = riffyn_nexus_sdk_v1.TeamApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.ShareTeamBody() # ShareTeamBody | A JSON object containing the necessary properties to share the team.
id = 'id_example' # str | The `_id` of the team being shared.

try:
    # shareTeam
    api_response = api_instance.share_team(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->share_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShareTeamBody**](ShareTeamBody.md)| A JSON object containing the necessary properties to share the team. | 
 **id** | **str**| The &#x60;_id&#x60; of the team being shared. | 

### Return type

[**SuccessfullyShare**](SuccessfullyShare.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unshare_team**
> SuccessfullyUnshared unshare_team(body, id, principal_id)

unshareTeam

Revoke access to an existing team from a user, team, or organization.

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
api_instance = riffyn_nexus_sdk_v1.TeamApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.UnshareTeamBody() # UnshareTeamBody | A JSON object containing the necessary properties to revoke access to the team.
id = 'id_example' # str | The `_id` of the team.
principal_id = 'principal_id_example' # str | The `_id` of the entity being revoked access to the team.

try:
    # unshareTeam
    api_response = api_instance.unshare_team(body, id, principal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->unshare_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnshareTeamBody**](UnshareTeamBody.md)| A JSON object containing the necessary properties to revoke access to the team. | 
 **id** | **str**| The &#x60;_id&#x60; of the team. | 
 **principal_id** | **str**| The &#x60;_id&#x60; of the entity being revoked access to the team. | 

### Return type

[**SuccessfullyUnshared**](SuccessfullyUnshared.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> Team update_team(body, id)

updateTeam

Update the name or the description of an existing team.

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
api_instance = riffyn_nexus_sdk_v1.TeamApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.UpdateTeamBody() # UpdateTeamBody | A JSON object containing the necessary properties to update the team.
id = 'id_example' # str | The `_id` of the team.

try:
    # updateTeam
    api_response = api_instance.update_team(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->update_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTeamBody**](UpdateTeamBody.md)| A JSON object containing the necessary properties to update the team. | 
 **id** | **str**| The &#x60;_id&#x60; of the team. | 

### Return type

[**Team**](Team.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

