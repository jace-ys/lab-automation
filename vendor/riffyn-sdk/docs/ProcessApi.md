# riffyn_nexus_sdk_v1.ProcessApi

All URIs are relative to *deployment_url/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_connection**](ProcessApi.md#add_connection) | **POST** /process/{id}/connection | addConnection
[**add_process_comment**](ProcessApi.md#add_process_comment) | **POST** /process/{id}/comment | addProcessComment
[**add_tag_to_process**](ProcessApi.md#add_tag_to_process) | **POST** /process/{id}/tag | addTagToProcess
[**create_group**](ProcessApi.md#create_group) | **POST** /process/{id}/group | createGroup
[**create_process**](ProcessApi.md#create_process) | **POST** /process | createProcess
[**delete_connection**](ProcessApi.md#delete_connection) | **DELETE** /process/{id}/connection/{fromResDefId} | deleteConnection
[**delete_group**](ProcessApi.md#delete_group) | **DELETE** /process/{id}/group/{groupId} | deleteGroup
[**delete_process**](ProcessApi.md#delete_process) | **DELETE** /process/{id} | deleteProcess
[**delete_process_comment**](ProcessApi.md#delete_process_comment) | **DELETE** /process/{id}/comment/{commentId} | deleteProcessComment
[**delete_tag_from_process**](ProcessApi.md#delete_tag_from_process) | **DELETE** /process/{id}/tag/{tagId} | deleteTagFromProcess
[**duplicate_process**](ProcessApi.md#duplicate_process) | **POST** /process/{id} | duplicateProcess
[**export_to_enclosing_group**](ProcessApi.md#export_to_enclosing_group) | **POST** /process/{id}/connection/{resourceDefId}/export | exportToEnclosingGroup
[**get_group**](ProcessApi.md#get_group) | **GET** /process/{id}/group/{groupId} | getGroup
[**get_process**](ProcessApi.md#get_process) | **GET** /process/{id} | getProcess
[**get_process_comment**](ProcessApi.md#get_process_comment) | **GET** /process/{id}/comment/{commentId} | getProcessComment
[**get_process_version**](ProcessApi.md#get_process_version) | **GET** /process/{id}/version/{versionLabel} | getProcessVersion
[**get_role_for_process**](ProcessApi.md#get_role_for_process) | **GET** /process/{id}/role/{userId} | getRoleForProcess
[**get_upload_config**](ProcessApi.md#get_upload_config) | **GET** /process/{id}/upload-config/{uploadConfigId} | getUploadConfig
[**get_upload_config_collection**](ProcessApi.md#get_upload_config_collection) | **GET** /process/{id}/upload-config-collection/{collectionId} | getUploadConfigCollection
[**list_groups**](ProcessApi.md#list_groups) | **GET** /process/{id}/groups | listGroups
[**list_process_comments**](ProcessApi.md#list_process_comments) | **GET** /process/{id}/comments | listProcessComments
[**list_process_tags**](ProcessApi.md#list_process_tags) | **GET** /process/{id}/tags | listProcessTags
[**list_process_versions**](ProcessApi.md#list_process_versions) | **GET** /process/{id}/versions | listProcessVersions
[**list_processes**](ProcessApi.md#list_processes) | **GET** /processes | listProcesses
[**list_replies_to_process_comment**](ProcessApi.md#list_replies_to_process_comment) | **GET** /process/{id}/comment/{commentId}/replies | listRepliesToProcessComment
[**list_upload_config_collections**](ProcessApi.md#list_upload_config_collections) | **GET** /process/{id}/upload-config-collections | listUploadConfigCollections
[**list_upload_configs**](ProcessApi.md#list_upload_configs) | **GET** /process/{id}/upload-configs | listUploadConfigs
[**reply_to_process_comment**](ProcessApi.md#reply_to_process_comment) | **POST** /process/{id}/comment/{commentId}/reply | replyToProcessComment
[**share_process**](ProcessApi.md#share_process) | **POST** /process/{id}/accessible-to | shareProcess
[**unshare_process**](ProcessApi.md#unshare_process) | **PATCH** /process/{id}/accessible-to/{principalId} | unshareProcess
[**update_group**](ProcessApi.md#update_group) | **PATCH** /process/{id}/group/{groupId} | updateGroup
[**update_process**](ProcessApi.md#update_process) | **PATCH** /process/{id} | updateProcess
[**update_process_comment**](ProcessApi.md#update_process_comment) | **PATCH** /process/{id}/comment/{commentId} | updateProcessComment

# **add_connection**
> SuccessfullyConnection add_connection(body, id)

addConnection

Makes a connection between activities and/or groups for a resource type (indicated by its `resourceDefId`). ResourceDefs are the inputs and outputs of the process activity (step) which correspond to the resource type being connected. The resourceDefId for a group is the resourceDefId of the activity inside the group where the resource type exists. To connect a group, the resourceDefId must first be exported/imported from the activity inside the group where the resourceDef exists (Use `exportToEnclosingGroup` endpoint). Both activities and/or groups being connected must be at the same level. The connection will be reflected in the connections object of the enclosing group or the process. 

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.Connection() # Connection | A JSON object containing the necessary properties to add a connection.
id = 'id_example' # str | The `_id` of the process.

try:
    # addConnection
    api_response = api_instance.add_connection(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->add_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Connection**](Connection.md)| A JSON object containing the necessary properties to add a connection. | 
 **id** | **str**| The &#x60;_id&#x60; of the process. | 

### Return type

[**SuccessfullyConnection**](SuccessfullyConnection.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_process_comment**
> CommentResponse add_process_comment(body, id)

addProcessComment

Adds a comment (or design notes) to a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.CommentBody() # CommentBody | A JSON object containing the necessary properties to create a new comment (or observation).
id = 'id_example' # str | The `_id` of process.

try:
    # addProcessComment
    api_response = api_instance.add_process_comment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->add_process_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentBody**](CommentBody.md)| A JSON object containing the necessary properties to create a new comment (or observation). | 
 **id** | **str**| The &#x60;_id&#x60; of process. | 

### Return type

[**CommentResponse**](CommentResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tag_to_process**
> Tag add_tag_to_process(body, id)

addTagToProcess

Adds a tag to an process. If the tag doesn't exist, it will create it and add it to the process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.Body8() # Body8 | A JSON object containing the options for creating the tag.
id = 'id_example' # str | The `_id` of the process you would like to add the tag to.

try:
    # addTagToProcess
    api_response = api_instance.add_tag_to_process(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->add_tag_to_process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body8**](Body8.md)| A JSON object containing the options for creating the tag. | 
 **id** | **str**| The &#x60;_id&#x60; of the process you would like to add the tag to. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> InlineResponse20014 create_group(body, id)

createGroup

Create a group within a process. Existing activities and groups can be added to the group being created. These entities must be siblings of the group being created.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.GroupBody() # GroupBody | A JSON object containing the necessary properties to create a new group.
id = 'id_example' # str | The `_id` of process.

try:
    # createGroup
    api_response = api_instance.create_group(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupBody**](GroupBody.md)| A JSON object containing the necessary properties to create a new group. | 
 **id** | **str**| The &#x60;_id&#x60; of process. | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_process**
> SuccessfullyCreation create_process(body)

createProcess

Create a new process. A process is a top level group that contains activities and other groups.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.Process() # Process | A JSON object containing the necessary properties to create a new topGroup.

try:
    # createProcess
    api_response = api_instance.create_process(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->create_process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Process**](Process.md)| A JSON object containing the necessary properties to create a new topGroup. | 

### Return type

[**SuccessfullyCreation**](SuccessfullyCreation.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection**
> SuccessfullyDelete delete_connection(id, from_res_def_id, to_res_def_id, parent_id=parent_id)

deleteConnection

Deletes a connection between two entities (group or activity) for a resource type (indicated by its `resourceDefId`). ResourceDefs are the `inputs` and `outputs` of the process activity (step) which correspond to the resource type being disconnected. The `resourceDefId` for a group is the exported `resourceDefId` of the activity where the resource type exists. Both entities being disconnected must be at the same level unless removing an exported connection between an inner entity and its parent. When removing an exported connection the `resourceDefId` will be the same for both `toResDefId` and `fromResDefId`. If the entities are not at the top level for the process, the `parentId` of the entities must be defined. The connection will be deleted from the connections object of the enclosing group or the process. 

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the process.
from_res_def_id = 'from_res_def_id_example' # str | The `_id` of the `output` on the activity for the resource type the connection will be removed from. This activity may be within the group being disconnected. The `fromResDefId` must always be on the output of the connection being removed.
to_res_def_id = 'to_res_def_id_example' # str | The `_id` of the `input` on the activity for the resource type the connection will be removed from.  This activity may be within the group being disconnected. The `toResDefId` must always be on the input of the connection being removed.
parent_id = 'parent_id_example' # str | The id of the parent group of both entities. If both entities are not at the toplevel for the process, the `parentId` for the entities must be included. When removing an exported connection the parent is the group enclosing the entity with the exported `resourceDefId`. (optional)

try:
    # deleteConnection
    api_response = api_instance.delete_connection(id, from_res_def_id, to_res_def_id, parent_id=parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->delete_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the process. | 
 **from_res_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;output&#x60; on the activity for the resource type the connection will be removed from. This activity may be within the group being disconnected. The &#x60;fromResDefId&#x60; must always be on the output of the connection being removed. | 
 **to_res_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; on the activity for the resource type the connection will be removed from.  This activity may be within the group being disconnected. The &#x60;toResDefId&#x60; must always be on the input of the connection being removed. | 
 **parent_id** | **str**| The id of the parent group of both entities. If both entities are not at the toplevel for the process, the &#x60;parentId&#x60; for the entities must be included. When removing an exported connection the parent is the group enclosing the entity with the exported &#x60;resourceDefId&#x60;. | [optional] 

### Return type

[**SuccessfullyDelete**](SuccessfullyDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> InlineResponse20015 delete_group(id, group_id)

deleteGroup

Deletes the specific group from the process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
group_id = 'group_id_example' # str | The `_id` of the group.

try:
    # deleteGroup
    api_response = api_instance.delete_group(id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **group_id** | **str**| The &#x60;_id&#x60; of the group. | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_process**
> SuccessfullyDelete delete_process(id, purge_experiments=purge_experiments)

deleteProcess

Performs a 'soft delete' on an existing process. Deleted processes will be marked as purged and remain in the database for 7 days, after which they will then be permanently deleted. During those 7 days the process will still be accessible through the api by searching for `_id` on `getProcess` endpoint or with the query parameter `deleted` on`listProcesses` endpoint. Associated experiments will also be 'soft deleted' for 7 days before being removed. To preserve associated experiments beyond the permanent deletion of the process, use the `purgeExperiments` query parameter. Remaining experiments may not work as expected once the process is purged. 

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the process.
purge_experiments = true # bool | Defaults to `true`. Set to `false` to prevent the experiments associated with the process from being deleted. (optional)

try:
    # deleteProcess
    api_response = api_instance.delete_process(id, purge_experiments=purge_experiments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->delete_process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the process. | 
 **purge_experiments** | **bool**| Defaults to &#x60;true&#x60;. Set to &#x60;false&#x60; to prevent the experiments associated with the process from being deleted. | [optional] 

### Return type

[**SuccessfullyDelete**](SuccessfullyDelete.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_process_comment**
> SuccessMessage delete_process_comment(id, comment_id)

deleteProcessComment

Deletes the specific comment (or design notes) associated with a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
comment_id = 'comment_id_example' # str | The `_id` of the comment.

try:
    # deleteProcessComment
    api_response = api_instance.delete_process_comment(id, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->delete_process_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **comment_id** | **str**| The &#x60;_id&#x60; of the comment. | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag_from_process**
> SuccessMessage delete_tag_from_process(id, tag_id)

deleteTagFromProcess

Removes a tag from an process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
tag_id = 'tag_id_example' # str | The `_id` of the tag to be removed from the process.

try:
    # deleteTagFromProcess
    api_response = api_instance.delete_tag_from_process(id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->delete_tag_from_process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **tag_id** | **str**| The &#x60;_id&#x60; of the tag to be removed from the process. | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_process**
> SuccessfullyCreation duplicate_process(id, body=body)

duplicateProcess

Duplicates the specified process. A version can be passed in to duplicate a chosen version of the process. If no version is passed in, the latest saved version will be duplicated.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the process.
body = riffyn_nexus_sdk_v1.DuplicateProcess() # DuplicateProcess | A JSON object containing the necessary properties to duplicate a process. (optional)

try:
    # duplicateProcess
    api_response = api_instance.duplicate_process(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->duplicate_process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the process. | 
 **body** | [**DuplicateProcess**](DuplicateProcess.md)| A JSON object containing the necessary properties to duplicate a process. | [optional] 

### Return type

[**SuccessfullyCreation**](SuccessfullyCreation.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_to_enclosing_group**
> SuccessfullyExported export_to_enclosing_group(id, resource_def_id, body=body)

exportToEnclosingGroup

Exports a resourceType (indicated by its `resourceDefId`) from an activity or a group to the connections object of the enclosing group or process. This connects the inner entities to the enclosing group or process. The enclosing group can then be connected to other entities. Inner entities must be exported first starting with the activity with the `resourceDefId` being exported.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the process.
resource_def_id = 'resource_def_id_example' # str | The `_id` of the `input` or `output` on the activity for the resource type the property type will be updated on.
body = riffyn_nexus_sdk_v1.EnclosingConnection() # EnclosingConnection | A JSON object containing the necessary properties to export to enclosing group. (optional)

try:
    # exportToEnclosingGroup
    api_response = api_instance.export_to_enclosing_group(id, resource_def_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->export_to_enclosing_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the process. | 
 **resource_def_id** | **str**| The &#x60;_id&#x60; of the &#x60;input&#x60; or &#x60;output&#x60; on the activity for the resource type the property type will be updated on. | 
 **body** | [**EnclosingConnection**](EnclosingConnection.md)| A JSON object containing the necessary properties to export to enclosing group. | [optional] 

### Return type

[**SuccessfullyExported**](SuccessfullyExported.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(id, group_id)

getGroup

Returns the specific group associated with a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
group_id = 'group_id_example' # str | The `_id` of the group.

try:
    # getGroup
    api_response = api_instance.get_group(id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **group_id** | **str**| The &#x60;_id&#x60; of the group. | 

### Return type

[**Group**](Group.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process**
> Group get_process(id)

getProcess

Returns the detail for the specified process

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of the process.

try:
    # getProcess
    api_response = api_instance.get_process(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->get_process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of the process. | 

### Return type

[**Group**](Group.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_comment**
> Comment get_process_comment(id, comment_id)

getProcessComment

Returns the specific comment (or design notes) associated with a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
comment_id = 'comment_id_example' # str | The `_id` of the comment.

try:
    # getProcessComment
    api_response = api_instance.get_process_comment(id, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->get_process_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **comment_id** | **str**| The &#x60;_id&#x60; of the comment. | 

### Return type

[**Comment**](Comment.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_version**
> Group get_process_version(id, version_label)

getProcessVersion

Returns design details on the specified process and version.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
version_label = 'version_label_example' # str | The `version.label` of the process. Should be in the format of `0.01` or `1.00`.

try:
    # getProcessVersion
    api_response = api_instance.get_process_version(id, version_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->get_process_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **version_label** | **str**| The &#x60;version.label&#x60; of the process. Should be in the format of &#x60;0.01&#x60; or &#x60;1.00&#x60;. | 

### Return type

[**Group**](Group.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_for_process**
> Role get_role_for_process(id, user_id)

getRoleForProcess

Returns the highest role for the specified user for the specific process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
user_id = 'user_id_example' # str | The `_id` of the user.

try:
    # getRoleForProcess
    api_response = api_instance.get_role_for_process(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->get_role_for_process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **user_id** | **str**| The &#x60;_id&#x60; of the user. | 

### Return type

[**Role**](Role.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload_config**
> UploadConfig get_upload_config(id, upload_config_id)

getUploadConfig

Returns the details for the selected upload configuration (or parseConfig).

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
upload_config_id = 'upload_config_id_example' # str | The `_id` of the upload configuration.

try:
    # getUploadConfig
    api_response = api_instance.get_upload_config(id, upload_config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->get_upload_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **upload_config_id** | **str**| The &#x60;_id&#x60; of the upload configuration. | 

### Return type

[**UploadConfig**](UploadConfig.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload_config_collection**
> UploadConfigCollection get_upload_config_collection(id, collection_id)

getUploadConfigCollection

Returns the details for the selected upload configuration collection (or collection of parseConfigs).

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
collection_id = 'collection_id_example' # str | The `_id` of the upload configuration collection.

try:
    # getUploadConfigCollection
    api_response = api_instance.get_upload_config_collection(id, collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->get_upload_config_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **collection_id** | **str**| The &#x60;_id&#x60; of the upload configuration collection. | 

### Return type

[**UploadConfigCollection**](UploadConfigCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> Groups list_groups(id, sort=sort, version=version, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator, public=public)

listGroups

List or search the groups associated with a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
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
    # listGroups
    api_response = api_instance.list_groups(id, sort=sort, version=version, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator, public=public)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->list_groups: %s\n" % e)
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

[**Groups**](Groups.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_process_comments**
> Comments list_process_comments(id, activity_id=activity_id, group_id=group_id, experiment_id=experiment_id, limit=limit, offset=offset, before=before, after=after, modified_before=modified_before, modified_after=modified_after, fields=fields, creator=creator)

listProcessComments

Lists the comments (or design notes) associated with a process. Includes experiment, activity, and group comments.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
activity_id = 'activity_id_example' # str | Limits the result set to items associated with the `_id` of the specified activity. Refers to the Process level Activity `_id`. (optional)
group_id = 'group_id_example' # str | Limits the result set to items associated with the `_id` of the specified group. The process `_id` is the `topGroupId`. (optional)
experiment_id = 'experiment_id_example' # str | Limits the result set to items associated with the `_id` of the specified experiment. (optional)
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)
modified_before = 'modified_before_example' # str | Limits the result set to items modified on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch, `1507650828`).  (optional)
modified_after = 'modified_after_example' # str | Limits the result set to items modified on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z` or epoch, `1507650828`).  (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)
creator = 'creator_example' # str | Limits the result set to items created by the user with this username. (optional)

try:
    # listProcessComments
    api_response = api_instance.list_process_comments(id, activity_id=activity_id, group_id=group_id, experiment_id=experiment_id, limit=limit, offset=offset, before=before, after=after, modified_before=modified_before, modified_after=modified_after, fields=fields, creator=creator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->list_process_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **activity_id** | **str**| Limits the result set to items associated with the &#x60;_id&#x60; of the specified activity. Refers to the Process level Activity &#x60;_id&#x60;. | [optional] 
 **group_id** | **str**| Limits the result set to items associated with the &#x60;_id&#x60; of the specified group. The process &#x60;_id&#x60; is the &#x60;topGroupId&#x60;. | [optional] 
 **experiment_id** | **str**| Limits the result set to items associated with the &#x60;_id&#x60; of the specified experiment. | [optional] 
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

# **list_process_tags**
> Tags list_process_tags(id, name=name, limit=limit, offset=offset, before=before, after=after, modified_before=modified_before, modified_after=modified_after, fields=fields, creator=creator)

listProcessTags

Returns the tags for the specified process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
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
    # listProcessTags
    api_response = api_instance.list_process_tags(id, name=name, limit=limit, offset=offset, before=before, after=after, modified_before=modified_before, modified_after=modified_after, fields=fields, creator=creator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->list_process_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
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

# **list_process_versions**
> Group list_process_versions(id)

listProcessVersions

Returns design details for all the versions of the process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.

try:
    # listProcessVersions
    api_response = api_instance.list_process_versions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->list_process_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 

### Return type

[**Group**](Group.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_processes**
> Processes list_processes(sort=sort, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator, public=public, deleted=deleted)

listProcesses

List or search the user's processes.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
sort = ['sort_example'] # list[str] | The sort order to use for the result set. To sort in descending order, prefix the field name with a dash(`-`). A comma separated list may be used to sort by more than one field (e.g. `name,-label`).  (optional)
limit = 56 # int | Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100`  (optional)
offset = 56 # int | The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  (optional)
before = 'before_example' # str | Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  (optional)
after = 'after_example' # str | Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`).  (optional)
fields = 'fields_example' # str | Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query.  (optional)
name = 'name_example' # str | Limits the result set to items with this exact name (case insensitive). (optional)
creator = 'creator_example' # str | Limits the result set to items created by the user with this username. (optional)
public = true # bool | Toggles the result set between public and private data. Default value is `false` (optional)
deleted = true # bool | Limits the results to deleted items, excludes them, or returns both deleted and non-deleted items if set to `all `. Default value       is `false`, to only show non-deleted items.  (optional)

try:
    # listProcesses
    api_response = api_instance.list_processes(sort=sort, limit=limit, offset=offset, before=before, after=after, fields=fields, name=name, creator=creator, public=public, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->list_processes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | [**list[str]**](str.md)| The sort order to use for the result set. To sort in descending order, prefix the field name with a dash(&#x60;-&#x60;). A comma separated list may be used to sort by more than one field (e.g. &#x60;name,-label&#x60;).  | [optional] 
 **limit** | **int**| Limits the number of records returned to the given value. Maximum value is &#x60;1000&#x60;. Default value is &#x60;100&#x60;  | [optional] 
 **offset** | **int**| The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned.  | [optional] 
 **before** | **str**| Limits the result set to items created on, or before, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded.  | [optional] 
 **after** | **str**| Limits the result set to items created on, or after, the specified timestamp (for example ISO, &#x60;2017-10-10T15:53:48.998Z&#x60;).  | [optional] 
 **fields** | **str**| Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use &#x60;fields&#x3D;name,created&#x60;. To exclude the name and created fields from the results use &#x60;fields&#x3D;-name,-created&#x60;. Inclusion and exclusion options can not be set in the same query.  | [optional] 
 **name** | **str**| Limits the result set to items with this exact name (case insensitive). | [optional] 
 **creator** | **str**| Limits the result set to items created by the user with this username. | [optional] 
 **public** | **bool**| Toggles the result set between public and private data. Default value is &#x60;false&#x60; | [optional] 
 **deleted** | **bool**| Limits the results to deleted items, excludes them, or returns both deleted and non-deleted items if set to &#x60;all &#x60;. Default value       is &#x60;false&#x60;, to only show non-deleted items.  | [optional] 

### Return type

[**Processes**](Processes.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replies_to_process_comment**
> Comments list_replies_to_process_comment(id, comment_id, limit=limit, offset=offset, before=before, after=after, modified_before=modified_before, modified_after=modified_after, fields=fields, creator=creator)

listRepliesToProcessComment

Lists replies to a specific comment (or design notes) associated with a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.
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
    # listRepliesToProcessComment
    api_response = api_instance.list_replies_to_process_comment(id, comment_id, limit=limit, offset=offset, before=before, after=after, modified_before=modified_before, modified_after=modified_after, fields=fields, creator=creator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->list_replies_to_process_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 
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

# **list_upload_config_collections**
> UploadConfigCollections list_upload_config_collections(id)

listUploadConfigCollections

Lists all collections of upload configurations (or parseConfigs) on the process. The upload configs of a collection may not all apply to the same activityId.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.

try:
    # listUploadConfigCollections
    api_response = api_instance.list_upload_config_collections(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->list_upload_config_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 

### Return type

[**UploadConfigCollections**](UploadConfigCollections.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_upload_configs**
> UploadConfigs list_upload_configs(id)

listUploadConfigs

Lists the upload configurations (or parseConfigs) on the process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
id = 'id_example' # str | The `_id` of process.

try:
    # listUploadConfigs
    api_response = api_instance.list_upload_configs(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->list_upload_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;_id&#x60; of process. | 

### Return type

[**UploadConfigs**](UploadConfigs.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reply_to_process_comment**
> CommentResponse reply_to_process_comment(body, id, comment_id)

replyToProcessComment

Replies to a specific comment (or design notes) associated with a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.CommentMessageBody() # CommentMessageBody | A JSON object containing the necessary properties to reply to a comment.
id = 'id_example' # str | The `_id` of process.
comment_id = 'comment_id_example' # str | The `_id` of the comment.

try:
    # replyToProcessComment
    api_response = api_instance.reply_to_process_comment(body, id, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->reply_to_process_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentMessageBody**](CommentMessageBody.md)| A JSON object containing the necessary properties to reply to a comment. | 
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **comment_id** | **str**| The &#x60;_id&#x60; of the comment. | 

### Return type

[**CommentResponse**](CommentResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_process**
> SuccessShared share_process(body, id)

shareProcess

Share an existing process with a user, team, or organization.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.ShareProcessBody() # ShareProcessBody | A JSON object containing the necessary properties to share the process.
id = 'id_example' # str | The `_id` of process.

try:
    # shareProcess
    api_response = api_instance.share_process(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->share_process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShareProcessBody**](ShareProcessBody.md)| A JSON object containing the necessary properties to share the process. | 
 **id** | **str**| The &#x60;_id&#x60; of process. | 

### Return type

[**SuccessShared**](SuccessShared.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unshare_process**
> SuccessfullyUnshared unshare_process(body, id, principal_id)

unshareProcess

Revoke access to an existing proces from a user, team, or organization.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.UnshareProcessBody() # UnshareProcessBody | A JSON object containing the necessary properties to revoke access to the process.
id = 'id_example' # str | The `_id` of the process to be revoked access to
principal_id = 'principal_id_example' # str | The `_id` of the entity being revoked access to the process.

try:
    # unshareProcess
    api_response = api_instance.unshare_process(body, id, principal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->unshare_process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnshareProcessBody**](UnshareProcessBody.md)| A JSON object containing the necessary properties to revoke access to the process. | 
 **id** | **str**| The &#x60;_id&#x60; of the process to be revoked access to | 
 **principal_id** | **str**| The &#x60;_id&#x60; of the entity being revoked access to the process. | 

### Return type

[**SuccessfullyUnshared**](SuccessfullyUnshared.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> InlineResponse20016 update_group(body, id, group_id)

updateGroup

Updates the specific group associated with a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.UpdateGroupBody() # UpdateGroupBody | A JSON object containing the necessary properties to update a group.
id = 'id_example' # str | The `_id` of process.
group_id = 'group_id_example' # str | The `_id` of the group.

try:
    # updateGroup
    api_response = api_instance.update_group(body, id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateGroupBody**](UpdateGroupBody.md)| A JSON object containing the necessary properties to update a group. | 
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **group_id** | **str**| The &#x60;_id&#x60; of the group. | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_process**
> Group update_process(body, id)

updateProcess

Updates the specific process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.UpdateProcess() # UpdateProcess | A JSON object containing the necessary properties to update a process.
id = 'id_example' # str | The `_id` of the process.

try:
    # updateProcess
    api_response = api_instance.update_process(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->update_process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateProcess**](UpdateProcess.md)| A JSON object containing the necessary properties to update a process. | 
 **id** | **str**| The &#x60;_id&#x60; of the process. | 

### Return type

[**Group**](Group.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_process_comment**
> SuccessMessage update_process_comment(body, id, comment_id)

updateProcessComment

Updates the specific comment (or design notes) associated with a process.

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
api_instance = riffyn_nexus_sdk_v1.ProcessApi(riffyn_nexus_sdk_v1.ApiClient(configuration))
body = riffyn_nexus_sdk_v1.CommentMessageBody() # CommentMessageBody | A JSON object containing the necessary properties to create a new comment (or observation).
id = 'id_example' # str | The `_id` of process.
comment_id = 'comment_id_example' # str | The `_id` of the comment.

try:
    # updateProcessComment
    api_response = api_instance.update_process_comment(body, id, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->update_process_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentMessageBody**](CommentMessageBody.md)| A JSON object containing the necessary properties to create a new comment (or observation). | 
 **id** | **str**| The &#x60;_id&#x60; of process. | 
 **comment_id** | **str**| The &#x60;_id&#x60; of the comment. | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

