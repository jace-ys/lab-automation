# swagger_client.AuthenticationApi

All URIs are relative to *https://api.riffyn.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AuthenticationApi.md#authenticate) | **POST** /auth | 
[**check_access_token**](AuthenticationApi.md#check_access_token) | **GET** /auth/access-token | 
[**create_access_token**](AuthenticationApi.md#create_access_token) | **POST** /auth/access-token | 
[**create_api_key**](AuthenticationApi.md#create_api_key) | **POST** /auth/api-key | 
[**list_api_keys**](AuthenticationApi.md#list_api_keys) | **GET** /auth/api-keys | 
[**update_api_key**](AuthenticationApi.md#update_api_key) | **PATCH** /auth/api-key/{id} | 
[**verify**](AuthenticationApi.md#verify) | **POST** /auth/factor/{factorId}/verify | 

# **authenticate**
> AuthResponse authenticate()



Validates the user from a `username` and `password` with `Basic Authentication`. Returns a JSON object with a `status`, `API Key`, `accessToken`, `accessTokenExpiresAt`. If MultiFactor Authentication is required, the JSON object will only have a `stateToken` and the `factorId` required in the `verify` endpoint along with the `status` and an `expiresAt` field.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.authenticate()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authenticate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_access_token**
> AccessTokenInfo check_access_token(access_token=access_token)



Checks the validity of the `access-token` used in the headers of the request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
access_token = 'access_token_example' # str | The `access-token` to be checked. (optional)

try:
    api_response = api_instance.check_access_token(access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->check_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| The &#x60;access-token&#x60; to be checked. | [optional] 

### Return type

[**AccessTokenInfo**](AccessTokenInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_access_token**
> AccessToken create_access_token(body=body)



Generates an `access-token` to be used to access the same endpoints that support apiKey authentication. Default lifetime for the access token in 30 minutes. A `time` parameter can be sent to set the lifetime up to 6 hours. 

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
api_instance = swagger_client.AuthenticationApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccessTokenBody() # AccessTokenBody | A JSON object containing the `time` describing the amount of time, in seconds, the generated access token should last. Maximum lifetime is 6 hours and the default is 30 minutes. ) (optional)

try:
    api_response = api_instance.create_access_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->create_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessTokenBody**](AccessTokenBody.md)| A JSON object containing the &#x60;time&#x60; describing the amount of time, in seconds, the generated access token should last. Maximum lifetime is 6 hours and the default is 30 minutes. ) | [optional] 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_key**
> NewApiKey create_api_key(body)



Generate a new `api-key` to be used to access any of the endpoints that support apiKey authentication. This API key will not be displayed again, please store it securely. The key must be named by passing a `name` in the `body`.

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
api_instance = swagger_client.AuthenticationApi(swagger_client.ApiClient(configuration))
body = swagger_client.NewApiKeyBody() # NewApiKeyBody | A JSON object containing the `name` for the new api key.

try:
    api_response = api_instance.create_api_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->create_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewApiKeyBody**](NewApiKeyBody.md)| A JSON object containing the &#x60;name&#x60; for the new api key. | 

### Return type

[**NewApiKey**](NewApiKey.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys**
> ApiKeys list_api_keys()



Returns the information associated with the api keys for the user. Will not include the api key itself. 

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
api_instance = swagger_client.AuthenticationApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.list_api_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->list_api_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiKeys**](ApiKeys.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key**
> UpdateApiKeyResponse update_api_key(body, id)



Rename an api key. A new `name` must be passed in the `body`. The `name` must be unique.

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
api_instance = swagger_client.AuthenticationApi(swagger_client.ApiClient(configuration))
body = swagger_client.NewApiKeyBody() # NewApiKeyBody | A JSON object containing the new name for the api key.
id = 'id_example' # str | The `_id` of the api-key.

try:
    api_response = api_instance.update_api_key(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->update_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewApiKeyBody**](NewApiKeyBody.md)| A JSON object containing the new name for the api key. | 
 **id** | **str**| The &#x60;_id&#x60; of the api-key. | 

### Return type

[**UpdateApiKeyResponse**](UpdateApiKeyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify**
> VerifyResponse verify(body, factor_id)



For MultiFactor Authentication only. Validates the `passCode` from Google Authenticator and returns a JSON object with the access token, the final status of the multi-factor authentication request, and the API key. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi(swagger_client.ApiClient(configuration))
body = swagger_client.VerifyBody() # VerifyBody | A JSON object containing the stateToken, factorId, and passCode to authenticate. When using the SDK pass in the values only (i.e. swagger_client.VerifyBody(passCode, state_token) ).
factor_id = 'factor_id_example' # str | The id of the factor type being checked. Generated by the [authenticate](/#api-Authentication-authenticate) endpoint.

try:
    api_response = api_instance.verify(body, factor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyBody**](VerifyBody.md)| A JSON object containing the stateToken, factorId, and passCode to authenticate. When using the SDK pass in the values only (i.e. swagger_client.VerifyBody(passCode, state_token) ). | 
 **factor_id** | **str**| The id of the factor type being checked. Generated by the [authenticate](/#api-Authentication-authenticate) endpoint. | 

### Return type

[**VerifyResponse**](VerifyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

