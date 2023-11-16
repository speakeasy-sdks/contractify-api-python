# Departments
(*departments*)

### Available Operations

* [create_department](#create_department) - Create a department
* [delete_department](#delete_department) - Delete a department
* [get_department](#get_department) - Get a department
* [list_departments](#list_departments) - List departments
* [update_department](#update_department) - Update a department

## create_department

Create a department

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

req = operations.CreateDepartmentRequest(
    department_write=shared.DepartmentWrite(
        name='Sales',
    ),
    company=33324,
)

res = s.departments.create_department(req)

if res.two_hundred_and_one_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateDepartmentRequest](../../models/operations/createdepartmentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateDepartmentResponse](../../models/operations/createdepartmentresponse.md)**
### Errors

| Error Object                                           | Status Code                                            | Content Type                                           |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| errors.CreateDepartmentResponseBody                    | 401                                                    | application/json                                       |
| errors.CreateDepartmentDepartmentsResponseBody         | 403                                                    | application/json                                       |
| errors.CreateDepartmentDepartmentsResponseResponseBody | 422                                                    | application/json                                       |
| errors.SDKError                                        | 400-600                                                | */*                                                    |

## delete_department

Delete a department

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

req = operations.DeleteDepartmentRequest(
    company=701942,
    department=751163,
)

res = s.departments.delete_department(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.DeleteDepartmentRequest](../../models/operations/deletedepartmentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.DeleteDepartmentResponse](../../models/operations/deletedepartmentresponse.md)**
### Errors

| Error Object                                              | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| errors.DeleteDepartmentResponseBody                       | 400                                                       | application/json                                          |
| errors.DeleteDepartmentDepartmentsResponseBody            | 401                                                       | application/json                                          |
| errors.DeleteDepartmentDepartmentsResponseResponseBody    | 403                                                       | application/json                                          |
| errors.DeleteDepartmentDepartmentsResponse404ResponseBody | 404                                                       | application/json                                          |
| errors.SDKError                                           | 400-600                                                   | */*                                                       |

## get_department

Get information about a department

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

req = operations.GetDepartmentRequest(
    company=255130,
    department=855529,
)

res = s.departments.get_department(req)

if res.two_hundred_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetDepartmentRequest](../../models/operations/getdepartmentrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetDepartmentResponse](../../models/operations/getdepartmentresponse.md)**
### Errors

| Error Object                                        | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| errors.GetDepartmentResponseBody                    | 401                                                 | application/json                                    |
| errors.GetDepartmentDepartmentsResponseBody         | 403                                                 | application/json                                    |
| errors.GetDepartmentDepartmentsResponseResponseBody | 404                                                 | application/json                                    |
| errors.SDKError                                     | 400-600                                             | */*                                                 |

## list_departments

List all the departments within a company

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

req = operations.ListDepartmentsRequest(
    company=117069,
)

res = s.departments.list_departments(req)

if res.department_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListDepartmentsRequest](../../models/operations/listdepartmentsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.ListDepartmentsResponse](../../models/operations/listdepartmentsresponse.md)**
### Errors

| Error Object                                  | Status Code                                   | Content Type                                  |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| errors.ListDepartmentsResponseBody            | 401                                           | application/json                              |
| errors.ListDepartmentsDepartmentsResponseBody | 403                                           | application/json                              |
| errors.SDKError                               | 400-600                                       | */*                                           |

## update_department

Update a department

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

req = operations.UpdateDepartmentRequest(
    department_write=shared.DepartmentWrite(
        name='Sales',
    ),
    company=431122,
    department=2342,
)

res = s.departments.update_department(req)

if res.two_hundred_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateDepartmentRequest](../../models/operations/updatedepartmentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.UpdateDepartmentResponse](../../models/operations/updatedepartmentresponse.md)**
### Errors

| Error Object                                              | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| errors.UpdateDepartmentResponseBody                       | 401                                                       | application/json                                          |
| errors.UpdateDepartmentDepartmentsResponseBody            | 403                                                       | application/json                                          |
| errors.UpdateDepartmentDepartmentsResponseResponseBody    | 404                                                       | application/json                                          |
| errors.UpdateDepartmentDepartmentsResponse422ResponseBody | 422                                                       | application/json                                          |
| errors.SDKError                                           | 400-600                                                   | */*                                                       |
