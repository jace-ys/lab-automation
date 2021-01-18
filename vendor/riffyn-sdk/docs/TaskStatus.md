# TaskStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of task at the time of the query. Will be one of: &#x60;new&#x60;, &#x60;initializing&#x60;, &#x60;initialized&#x60;, &#x60;wip&#x60;, &#x60;success&#x60;, &#x60;failed&#x60;, &#x60;aborted&#x60;. | [optional] 
**status_code** | **str** | | Code | Cause                                                                  | |------|------------------------------------------------------------------------| | 0    | initializing                                                           | | 1    | work in progress.                                                      | | 2    | success.                                                               | | 3    | task aborted due to new data.                                          | | 100  | unknown error.                                                         | | 101  | data is corrupted, fields are missing.                                 | | 301  | expected document too large.                                           | | 302  | database document too large.                                           | | 303  | memoryError                                                            | | 304  | exported file too large.                                               | | 305  | time out - data too large to process in maximum time.                  | | 901  | The export configuration has entity from older version of the process. |  | [optional] 
**status_message** | **str** | Message regarding the status of the task. For example: \&quot;task completed successfully\&quot; | [optional] 
**comment_message** | **str** | The comment message displayed to the user. | [optional] 
**stale** | **bool** | The￼&#x60;stale&#x60; field will only exist if relevant. A &#x60;stale&#x3D;true&#x60; flag means the experiment was modified since this task was created. The &#x60;stale&#x60; state is with respect to the requested &#x60;fileType&#x60; (defaults to &#x60;text/csv&#x60;). If you request &#x60;fileType&#x3D;binary/parquet&#x60;, the stale flag shows the status of the &#x60;binary/parquet&#x60; datatable. If you request &#x60;fileType&#x3D;text/csv&#x60; (the default) it shows the status of &#x60;text/csv&#x60; datatable. If stale is true, the results may not exist. The &#x60;stale&#x60; field will only exist if relevant.  | [optional] 
**modified** | **datetime** | The last modified date of the task | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

