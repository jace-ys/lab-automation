# UnitsForProperty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the unit of measurement. | [optional] 
**basic_unit** | **bool** |  | [optional] 
**definition** | **str** | Can be a mathematical formula for calculating this unit of measurment from other units of measurement, or a simple definition. | [optional] 
**definition_base** | **str** | The mathematical expression used to calculate this unit of measurement, in terms of base units. | [optional] 
**description** | **str** | A brief description of this unit of measurement. | [optional] 
**name** | **str** | The name of the item. | [optional] 
**notes** | **str** |  | [optional] 
**si_unit** | **bool** | Indicated if the unit of measurement is a part of the International System of Units. | [optional] 
**symbol** | **str** | The symbol that represents the unit of measurement. E.g. &#x60;in&#x60; for \&quot;inches\&quot;, or &#x60;mg&#x60; for \&quot;milligrams\&quot;. | [optional] 
**synonyms** | **list[str]** | An array of synonyms for the unit. In many instances units have multiple abbreviations or spellings. | [optional] 
**source** | **str** | Indicates if the unit is user defined or a system unit. Possible values are &#x60;SYSTEM&#x60; or &#x60;USER_DEFINED&#x60;. | [optional] 
**sharable** | **bool** | Indicates if the unit can be shared with other users. | [optional] 
**public** | **bool** | Indicates if the unit is visible to all users. | [optional] 
**creator** | **str** | The &#x60;username&#x60; of the user that created this unit. | [optional] 
**created** | [**Created**](Created.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

