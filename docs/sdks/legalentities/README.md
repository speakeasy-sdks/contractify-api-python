# LegalEntities
(*legal_entities*)

### Available Operations

* [list_legal_entities](#list_legal_entities) - List legal entities

## list_legal_entities

List all the legal entities within a company

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.ListLegalEntitiesRequest(
    company=730248,
)

res = s.legal_entities.list_legal_entities(req)

if res.legal_entity_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListLegalEntitiesRequest](../../models/operations/listlegalentitiesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.ListLegalEntitiesResponse](../../models/operations/listlegalentitiesresponse.md)**
### Errors

| Error Object                                      | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| errors.ListLegalEntitiesResponseBody              | 401                                               | application/json                                  |
| errors.ListLegalEntitiesLegalEntitiesResponseBody | 403                                               | application/json                                  |
| errors.SDKError                                   | 4x-5xx                                            | */*                                               |
