# subfolders

### Available Operations

* [list_subfolders](#list_subfolders) - List subfolders

## list_subfolders

List all the subfolders within a company

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.ListSubfoldersRequest(
    company=568434,
)

res = s.subfolders.list_subfolders(req, operations.ListSubfoldersSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.dossier_collection is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListSubfoldersRequest](../../models/operations/listsubfoldersrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.ListSubfoldersSecurity](../../models/operations/listsubfolderssecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.ListSubfoldersResponse](../../models/operations/listsubfoldersresponse.md)**

