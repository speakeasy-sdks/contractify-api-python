# departments

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

s = contractifyproduction.ContractifyProduction()

req = operations.CreateDepartmentRequest(
    department_write=shared.DepartmentWrite(
        name='Sales',
    ),
    company=568045,
)

res = s.departments.create_department(req, operations.CreateDepartmentSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.create_department_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateDepartmentRequest](../../models/operations/createdepartmentrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.CreateDepartmentSecurity](../../models/operations/createdepartmentsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.CreateDepartmentResponse](../../models/operations/createdepartmentresponse.md)**


## delete_department

Delete a department

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.DeleteDepartmentRequest(
    company=392785,
    department=925597,
)

res = s.departments.delete_department(req, operations.DeleteDepartmentSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteDepartmentRequest](../../models/operations/deletedepartmentrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.DeleteDepartmentSecurity](../../models/operations/deletedepartmentsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.DeleteDepartmentResponse](../../models/operations/deletedepartmentresponse.md)**


## get_department

Get information about a department

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.GetDepartmentRequest(
    company=836079,
    department=71036,
)

res = s.departments.get_department(req, operations.GetDepartmentSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.get_department_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetDepartmentRequest](../../models/operations/getdepartmentrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.GetDepartmentSecurity](../../models/operations/getdepartmentsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.GetDepartmentResponse](../../models/operations/getdepartmentresponse.md)**


## list_departments

List all the departments within a company

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.ListDepartmentsRequest(
    company=337396,
)

res = s.departments.list_departments(req, operations.ListDepartmentsSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.department_collection is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListDepartmentsRequest](../../models/operations/listdepartmentsrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.ListDepartmentsSecurity](../../models/operations/listdepartmentssecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.ListDepartmentsResponse](../../models/operations/listdepartmentsresponse.md)**


## update_department

Update a department

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction()

req = operations.UpdateDepartmentRequest(
    department_write=shared.DepartmentWrite(
        name='Sales',
    ),
    company=87129,
    department=648172,
)

res = s.departments.update_department(req, operations.UpdateDepartmentSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.update_department_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateDepartmentRequest](../../models/operations/updatedepartmentrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.UpdateDepartmentSecurity](../../models/operations/updatedepartmentsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.UpdateDepartmentResponse](../../models/operations/updatedepartmentresponse.md)**

