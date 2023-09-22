# CustomFields

### Available Operations

* [list_custom_fields](#list_custom_fields) - List custom fields

## list_custom_fields

List all the custom fields within a company

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

req = operations.ListCustomFieldsRequest(
    company=568045,
)

res = s.custom_fields.list_custom_fields(req)

if res.custom_field_collection is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListCustomFieldsRequest](../../models/operations/listcustomfieldsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListCustomFieldsResponse](../../models/operations/listcustomfieldsresponse.md)**

