# ContractTypes

### Available Operations

* [list_contract_types](#list_contract_types) - List contract types

## list_contract_types

List all the contract types within a company

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.ListContractTypesRequest(
    company=592845,
)

res = s.contract_types.list_contract_types(req, operations.ListContractTypesSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.contract_type_collection is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListContractTypesRequest](../../models/operations/listcontracttypesrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.ListContractTypesSecurity](../../models/operations/listcontracttypessecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.ListContractTypesResponse](../../models/operations/listcontracttypesresponse.md)**

