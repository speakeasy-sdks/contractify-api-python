# Offices
(*offices*)

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

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="",
        personal_access_token="",
    ),
)

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
    company=244393,
)

res = s.offices.create_office(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreateOfficeRequest](../../models/operations/createofficerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateOfficeResponse](../../models/operations/createofficeresponse.md)**
### Errors

| Error Object                                   | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| errors.CreateOfficeResponseBody                | 401                                            | application/json                               |
| errors.CreateOfficeOfficesResponseBody         | 403                                            | application/json                               |
| errors.CreateOfficeOfficesResponseResponseBody | 422                                            | application/json                               |
| errors.SDKError                                | 400-600                                        | */*                                            |

## delete_office

Delete an office

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

req = operations.DeleteOfficeRequest(
    company=327183,
    office=668605,
)

res = s.offices.delete_office(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteOfficeRequest](../../models/operations/deleteofficerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteOfficeResponse](../../models/operations/deleteofficeresponse.md)**
### Errors

| Error Object                                      | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| errors.DeleteOfficeResponseBody                   | 400                                               | application/json                                  |
| errors.DeleteOfficeOfficesResponseBody            | 401                                               | application/json                                  |
| errors.DeleteOfficeOfficesResponseResponseBody    | 403                                               | application/json                                  |
| errors.DeleteOfficeOfficesResponse404ResponseBody | 404                                               | application/json                                  |
| errors.SDKError                                   | 400-600                                           | */*                                               |

## get_office

Get information about an office

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

req = operations.GetOfficeRequest(
    company=616050,
    office=134885,
)

res = s.offices.get_office(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetOfficeRequest](../../models/operations/getofficerequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetOfficeResponse](../../models/operations/getofficeresponse.md)**
### Errors

| Error Object                                | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| errors.GetOfficeResponseBody                | 401                                         | application/json                            |
| errors.GetOfficeOfficesResponseBody         | 403                                         | application/json                            |
| errors.GetOfficeOfficesResponseResponseBody | 404                                         | application/json                            |
| errors.SDKError                             | 400-600                                     | */*                                         |

## list_offices

List all the offices within a company

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

req = operations.ListOfficesRequest(
    company=303557,
)

res = s.offices.list_offices(req)

if res.office_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListOfficesRequest](../../models/operations/listofficesrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListOfficesResponse](../../models/operations/listofficesresponse.md)**
### Errors

| Error Object                          | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.ListOfficesResponseBody        | 401                                   | application/json                      |
| errors.ListOfficesOfficesResponseBody | 403                                   | application/json                      |
| errors.SDKError                       | 400-600                               | */*                                   |

## update_office

Update an office

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
    company=989026,
    office=647378,
)

res = s.offices.update_office(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateOfficeRequest](../../models/operations/updateofficerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateOfficeResponse](../../models/operations/updateofficeresponse.md)**
### Errors

| Error Object                                      | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| errors.UpdateOfficeResponseBody                   | 401                                               | application/json                                  |
| errors.UpdateOfficeOfficesResponseBody            | 403                                               | application/json                                  |
| errors.UpdateOfficeOfficesResponseResponseBody    | 404                                               | application/json                                  |
| errors.UpdateOfficeOfficesResponse422ResponseBody | 422                                               | application/json                                  |
| errors.SDKError                                   | 400-600                                           | */*                                               |
