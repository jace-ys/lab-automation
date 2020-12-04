# NewPropertyTypeBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new property type. | 
**immutable** | **bool** | Indicates if values for this property type should be editable, once they&#x27;ve been set, in an experiment. | 
**data_type** | **str** | must be one of these values: float, integer, character, datetime, image. | 
**has_units** | **bool** |  | 
**parents** | [**list[NewPropertyTypeBodyParents]**](NewPropertyTypeBodyParents.md) |  | [optional] 
**synonyms** | **str** | An array of synonyms for the property type. | [optional] 
**units** | **str** | An array of _ids of the units for the property type. HasUnits must be set to true. | [optional] 
**definition** | **str** | A definition of the new property type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

