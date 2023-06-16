# DeleteTaskResponse


## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                    | *str*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `status_code`                                                                                     | *int*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `raw_response`                                                                                    | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)             | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `delete_task_401_application_json_object`                                                         | [Optional[DeleteTask401ApplicationJSON]](../../models/operations/deletetask401applicationjson.md) | :heavy_minus_sign:                                                                                | Unauthenticated                                                                                   |
| `delete_task_403_application_json_object`                                                         | [Optional[DeleteTask403ApplicationJSON]](../../models/operations/deletetask403applicationjson.md) | :heavy_minus_sign:                                                                                | Forbidden                                                                                         |
| `delete_task_404_application_json_object`                                                         | [Optional[DeleteTask404ApplicationJSON]](../../models/operations/deletetask404applicationjson.md) | :heavy_minus_sign:                                                                                | Not Found                                                                                         |