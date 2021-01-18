# SpecInner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type will be one of: &#x60;spec-limit&#x60;, &#x60;target&#x60;, &#x60;valid-options&#x60;, or &#x60;required&#x60;. Defines one object of each type of spec to be included in the array. See table above for usage. | [optional] 
**config** | **object** | The value for the spec type. This property can have different formats, depending on the &#x60;type&#x60; of the property spec. Only use either &#x60;upper&#x60; and &#x60;lower&#x60; or &#x60;value&#x60; in the config object not both. See table above for description of each format.  | [optional] 
**enforcement** | **str** | Currently only allows value of &#x60;none&#x60;. All objects will have the same &#x60;enforcement&#x60; format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

