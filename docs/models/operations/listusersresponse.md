# ListUsersResponse


## Fields

| Field                                                                                           | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `content_type`                                                                                  | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `status_code`                                                                                   | *int*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `raw_response`                                                                                  | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)           | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `user_collection`                                                                               | [Optional[shared.UserCollection]](../../models/shared/usercollection.md)                        | :heavy_minus_sign:                                                                              | OK                                                                                              |
| `list_users_401_application_json_object`                                                        | [Optional[ListUsers401ApplicationJSON]](../../models/operations/listusers401applicationjson.md) | :heavy_minus_sign:                                                                              | Unauthenticated                                                                                 |
| `list_users_403_application_json_object`                                                        | [Optional[ListUsers403ApplicationJSON]](../../models/operations/listusers403applicationjson.md) | :heavy_minus_sign:                                                                              | Forbidden                                                                                       |