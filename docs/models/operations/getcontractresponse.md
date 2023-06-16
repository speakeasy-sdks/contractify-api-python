# GetContractResponse


## Fields

| Field                                                                                               | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                      | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `status_code`                                                                                       | *int*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `raw_response`                                                                                      | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)               | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `get_contract_200_application_json_object`                                                          | [Optional[GetContract200ApplicationJSON]](../../models/operations/getcontract200applicationjson.md) | :heavy_minus_sign:                                                                                  | OK                                                                                                  |
| `get_contract_401_application_json_object`                                                          | [Optional[GetContract401ApplicationJSON]](../../models/operations/getcontract401applicationjson.md) | :heavy_minus_sign:                                                                                  | Unauthenticated                                                                                     |
| `get_contract_403_application_json_object`                                                          | [Optional[GetContract403ApplicationJSON]](../../models/operations/getcontract403applicationjson.md) | :heavy_minus_sign:                                                                                  | Forbidden                                                                                           |
| `get_contract_404_application_json_object`                                                          | [Optional[GetContract404ApplicationJSON]](../../models/operations/getcontract404applicationjson.md) | :heavy_minus_sign:                                                                                  | Not Found                                                                                           |