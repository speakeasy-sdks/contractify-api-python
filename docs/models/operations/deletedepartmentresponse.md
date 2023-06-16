# DeleteDepartmentResponse


## Fields

| Field                                                                                                         | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                                | *str*                                                                                                         | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `status_code`                                                                                                 | *int*                                                                                                         | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `raw_response`                                                                                                | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                         | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `delete_department_400_application_json_object`                                                               | [Optional[DeleteDepartment400ApplicationJSON]](../../models/operations/deletedepartment400applicationjson.md) | :heavy_minus_sign:                                                                                            | Precondition failed                                                                                           |
| `delete_department_401_application_json_object`                                                               | [Optional[DeleteDepartment401ApplicationJSON]](../../models/operations/deletedepartment401applicationjson.md) | :heavy_minus_sign:                                                                                            | Unauthenticated                                                                                               |
| `delete_department_403_application_json_object`                                                               | [Optional[DeleteDepartment403ApplicationJSON]](../../models/operations/deletedepartment403applicationjson.md) | :heavy_minus_sign:                                                                                            | Forbidden                                                                                                     |
| `delete_department_404_application_json_object`                                                               | [Optional[DeleteDepartment404ApplicationJSON]](../../models/operations/deletedepartment404applicationjson.md) | :heavy_minus_sign:                                                                                            | Not Found                                                                                                     |