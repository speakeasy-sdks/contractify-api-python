# legal_entities

### Available Operations

* [list_legal_entities](#list_legal_entities) - List legal entities

## list_legal_entities

List all the legal entities within a company

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.ListLegalEntitiesRequest(
    company=666767,
)

res = s.legal_entities.list_legal_entities(req, operations.ListLegalEntitiesSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.legal_entity_collection is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListLegalEntitiesRequest](../../models/operations/listlegalentitiesrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.ListLegalEntitiesSecurity](../../models/operations/listlegalentitiessecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.ListLegalEntitiesResponse](../../models/operations/listlegalentitiesresponse.md)**

