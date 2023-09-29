# Subfolders
(*subfolders*)

### Available Operations

* [list_subfolders](#list_subfolders) - List subfolders

## list_subfolders

List all the subfolders within a company

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="",
        personal_access_token="",
    ),
)

req = operations.ListSubfoldersRequest(
    company=749068,
)

res = s.subfolders.list_subfolders(req)

if res.dossier_collection is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListSubfoldersRequest](../../models/operations/listsubfoldersrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.ListSubfoldersResponse](../../models/operations/listsubfoldersresponse.md)**

