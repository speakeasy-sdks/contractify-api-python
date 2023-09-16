# Offices

### Available Operations

* [create_office](#create_office) - Create an office
* [delete_office](#delete_office) - Delete an office
* [get_office](#get_office) - Get an office
* [list_offices](#list_offices) - List offices
* [update_office](#update_office) - Update an office

## create_office

Create an office

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction()

req = operations.CreateOfficeRequest(
    office_write=shared.OfficeWrite(
        bus='1',
        city='Sleidinge',
        contact_person='Ada Lovelace',
        country='Belgium',
        email='info@contractify.be',
        id=1,
        name='Ghent',
        number_identity='OFF-GHENT',
        phone='+32 9 234 28 97',
        street='Polenstraat 163',
        zip='9940',
    ),
    company=118274,
)

res = s.offices.create_office(req, operations.CreateOfficeSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.create_office_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateOfficeRequest](../../models/operations/createofficerequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.CreateOfficeSecurity](../../models/operations/createofficesecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.CreateOfficeResponse](../../models/operations/createofficeresponse.md)**


## delete_office

Delete an office

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.DeleteOfficeRequest(
    company=720633,
    office=639921,
)

res = s.offices.delete_office(req, operations.DeleteOfficeSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DeleteOfficeRequest](../../models/operations/deleteofficerequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.DeleteOfficeSecurity](../../models/operations/deleteofficesecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.DeleteOfficeResponse](../../models/operations/deleteofficeresponse.md)**


## get_office

Get information about an office

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.GetOfficeRequest(
    company=582020,
    office=143353,
)

res = s.offices.get_office(req, operations.GetOfficeSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.get_office_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetOfficeRequest](../../models/operations/getofficerequest.md)   | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `security`                                                                   | [operations.GetOfficeSecurity](../../models/operations/getofficesecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.GetOfficeResponse](../../models/operations/getofficeresponse.md)**


## list_offices

List all the offices within a company

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.ListOfficesRequest(
    company=537373,
)

res = s.offices.list_offices(req, operations.ListOfficesSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.office_collection is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListOfficesRequest](../../models/operations/listofficesrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.ListOfficesSecurity](../../models/operations/listofficessecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.ListOfficesResponse](../../models/operations/listofficesresponse.md)**


## update_office

Update an office

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction()

req = operations.UpdateOfficeRequest(
    office_write=shared.OfficeWrite(
        bus='1',
        city='Sleidinge',
        contact_person='Ada Lovelace',
        country='Belgium',
        email='info@contractify.be',
        id=1,
        name='Ghent',
        number_identity='OFF-GHENT',
        phone='+32 9 234 28 97',
        street='Polenstraat 163',
        zip='9940',
    ),
    company=944669,
    office=758616,
)

res = s.offices.update_office(req, operations.UpdateOfficeSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.update_office_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateOfficeRequest](../../models/operations/updateofficerequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.UpdateOfficeSecurity](../../models/operations/updateofficesecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.UpdateOfficeResponse](../../models/operations/updateofficeresponse.md)**

