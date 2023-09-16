# Relations

### Available Operations

* [create_relation](#create_relation) - Create a relation
* [delete_relation](#delete_relation) - Delete a relation
* [get_relation](#get_relation) - Get a relation
* [list_relations](#list_relations) - List relations
* [update_relation](#update_relation) - Update a relation

## create_relation

Create a relation

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction()

req = operations.CreateRelationRequest(
    relation_write=shared.RelationWrite(
        address=shared.Address(
            address_line_1='221B Baker Street',
            address_line_2='Marylebone',
            city='London',
            country='United Kingdom',
            postal_code='NW1 6XE',
        ),
        email='sherlock@example.org',
        fax='+3211324354',
        mobile_phone='+23477123456',
        name='Sherlock Holmes Detective Services',
        phone='+23477123456',
        reference='REF123',
        vat='BE12345678',
        website='https://www.example.org',
    ),
    company=521848,
)

res = s.relations.create_relation(req, operations.CreateRelationSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.create_relation_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateRelationRequest](../../models/operations/createrelationrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.CreateRelationSecurity](../../models/operations/createrelationsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.CreateRelationResponse](../../models/operations/createrelationresponse.md)**


## delete_relation

Delete a relation

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.DeleteRelationRequest(
    company=105907,
    relation=414662,
)

res = s.relations.delete_relation(req, operations.DeleteRelationSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.DeleteRelationRequest](../../models/operations/deleterelationrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.DeleteRelationSecurity](../../models/operations/deleterelationsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.DeleteRelationResponse](../../models/operations/deleterelationresponse.md)**


## get_relation

Get information about a relation

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.GetRelationRequest(
    company=473600,
    relation=264555,
)

res = s.relations.get_relation(req, operations.GetRelationSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.get_relation_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetRelationRequest](../../models/operations/getrelationrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.GetRelationSecurity](../../models/operations/getrelationsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.GetRelationResponse](../../models/operations/getrelationresponse.md)**


## list_relations

List all the relations within a company

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.ListRelationsRequest(
    company=186332,
    page=774234,
    reference='cum',
)

res = s.relations.list_relations(req, operations.ListRelationsSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.relation_collection is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListRelationsRequest](../../models/operations/listrelationsrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.ListRelationsSecurity](../../models/operations/listrelationssecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.ListRelationsResponse](../../models/operations/listrelationsresponse.md)**


## update_relation

Update a relation

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction()

req = operations.UpdateRelationRequest(
    relation_write=shared.RelationWrite(
        address=shared.Address(
            address_line_1='221B Baker Street',
            address_line_2='Marylebone',
            city='London',
            country='United Kingdom',
            postal_code='NW1 6XE',
        ),
        email='sherlock@example.org',
        fax='+3211324354',
        mobile_phone='+23477123456',
        name='Sherlock Holmes Detective Services',
        phone='+23477123456',
        reference='REF123',
        vat='BE12345678',
        website='https://www.example.org',
    ),
    company=456150,
    relation=216550,
)

res = s.relations.update_relation(req, operations.UpdateRelationSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.update_relation_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateRelationRequest](../../models/operations/updaterelationrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.UpdateRelationSecurity](../../models/operations/updaterelationsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.UpdateRelationResponse](../../models/operations/updaterelationresponse.md)**

