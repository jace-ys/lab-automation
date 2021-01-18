# PropertySpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Allowed values are &#x60;none&#x60;, &#x60;required&#x60;, &#x60;valid-options&#x60;, &#x60;spec-limit&#x60;, &#x60;control-limit&#x60; | [optional] 
**value** | **object** | This property can have three different formats, depending on the &#x60;type&#x60; of the property spec. For &#x60;control-limit&#x60; this is an object with three properties, &#x60;ucl&#x60; - upper control limit, &#x60;lcl&#x60; - lower control limit, and &#x60;target&#x60; - the target value. For &#x60;spec-limit&#x60; this is an object with three properties, &#x60;usl&#x60; - upper spec limit, &#x60;lsl&#x60; - lower spec limit, and &#x60;target&#x60; - the target value. For &#x60;valid-options&#x60; this is an array of allowed values.  example:  {   lsl: 1,   usl: 1,   target: 1 }  | [optional] 
**enforcement** | **str** | Allowed values are &#x60;strict&#x60;, &#x60;warn&#x60;, &#x60;none&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

