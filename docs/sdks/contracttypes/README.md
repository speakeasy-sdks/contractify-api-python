# ContractTypes
(*contract_types*)

### Available Operations

* [list_contract_types](#list_contract_types) - List contract types

## list_contract_types

List all the contract types within a company

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.ListContractTypesRequest(
    company=839467,
)

res = s.contract_types.list_contract_types(req)

if res.contract_type_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListContractTypesRequest](../../models/operations/listcontracttypesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.ListContractTypesResponse](../../models/operations/listcontracttypesresponse.md)**
### Errors

| Error Object                                      | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| errors.ListContractTypesResponseBody              | 401                                               | application/json                                  |
| errors.ListContractTypesContractTypesResponseBody | 403                                               | application/json                                  |
| errors.SDKError                                   | 4x-5xx                                            | */*                                               |
