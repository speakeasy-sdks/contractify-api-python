# GetRelationResponse


## Fields

| Field                                                                                               | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                      | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `status_code`                                                                                       | *int*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `raw_response`                                                                                      | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)               | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `get_relation_200_application_json_object`                                                          | [Optional[GetRelation200ApplicationJSON]](../../models/operations/getrelation200applicationjson.md) | :heavy_minus_sign:                                                                                  | OK                                                                                                  |
| `get_relation_401_application_json_object`                                                          | [Optional[GetRelation401ApplicationJSON]](../../models/operations/getrelation401applicationjson.md) | :heavy_minus_sign:                                                                                  | Unauthenticated                                                                                     |
| `get_relation_403_application_json_object`                                                          | [Optional[GetRelation403ApplicationJSON]](../../models/operations/getrelation403applicationjson.md) | :heavy_minus_sign:                                                                                  | Forbidden                                                                                           |
| `get_relation_404_application_json_object`                                                          | [Optional[GetRelation404ApplicationJSON]](../../models/operations/getrelation404applicationjson.md) | :heavy_minus_sign:                                                                                  | Not Found                                                                                           |