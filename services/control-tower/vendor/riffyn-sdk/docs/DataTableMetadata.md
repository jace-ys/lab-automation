# DataTableMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_key** | **str** | A unique key that is assigned to this column. This key can be used to locate data for this column in the &#x60;datatables&#x60; array. | [optional] 
**display_name** | **str** |  | [optional] 
**header** | **str** | The &#x60;header&#x60; field can be used to access a column in the &#x60;datatable&#x60; row. | [optional] 
**level** | **str** |  | [optional] 
**direction** | **str** | If referring to a resource, indicates if it&#x27;s an &#x60;input&#x60; or &#x60;output&#x60; resource | [optional] 
**activity_id** | **str** | The &#x60;_id&#x60; of the activity (step) the data belongs to. Refers to the Process level Activity &#x60;_id&#x60;. | [optional] 
**activity_name** | **str** | The &#x60;name&#x60; of the activity (step) the data belongs to. | [optional] 
**activity_version** | **str** | The &#x60;version.label&#x60; of the activity (step) the data belongs to. | [optional] 
**resource_name** | **str** | The &#x60;name&#x60; of the resource the data belongs to. | [optional] 
**resource_def_id** | **str** | The &#x60;_id&#x60; of an &#x60;input&#x60; or &#x60;output&#x60; of the activity (step), linking the resource to the activity. | [optional] 
**spec_type** | **str** |  | [optional] 
**spec_attribute** | **str** |  | [optional] 
**exported_data_type** | **str** | The dataType of the column in the parquet/datatable. | [optional] 
**short_header** | **str** | The shortened name of the column data table. This is a unique name based on the &#x60;header&#x60; attribute. | [optional] 
**sql_name** | **str** | The name of the column when accessed via the SQL database. This name is the same as the &#x60;uniqueName&#x60; with pipe characters (\&quot;|\&quot;) replaced with two underscores (\&quot;__\&quot;) and spaces (\&quot; \&quot;) replaced with one underscore (\&quot;_\&quot;). | [optional] 
**unique_name** | **str** | The unique name of the column. This is the same as the &#x60;displayName&#x60; with a numeric index added to columns with conflicting names. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

