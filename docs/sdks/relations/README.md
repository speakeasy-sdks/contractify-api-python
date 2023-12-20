# Relations
(*relations*)

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

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

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
    company=528070,
)

res = s.relations.create_relation(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateRelationRequest](../../models/operations/createrelationrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateRelationResponse](../../models/operations/createrelationresponse.md)**
### Errors

| Error Object                                       | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| errors.CreateRelationResponseBody                  | 401                                                | application/json                                   |
| errors.CreateRelationRelationsResponseBody         | 403                                                | application/json                                   |
| errors.CreateRelationRelationsResponseResponseBody | 422                                                | application/json                                   |
| errors.SDKError                                    | 4x-5xx                                             | */*                                                |

## delete_relation

Delete a relation

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.DeleteRelationRequest(
    company=773418,
    relation=890630,
)

res = s.relations.delete_relation(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteRelationRequest](../../models/operations/deleterelationrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.DeleteRelationResponse](../../models/operations/deleterelationresponse.md)**
### Errors

| Error Object                                          | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| errors.DeleteRelationResponseBody                     | 400                                                   | application/json                                      |
| errors.DeleteRelationRelationsResponseBody            | 401                                                   | application/json                                      |
| errors.DeleteRelationRelationsResponseResponseBody    | 403                                                   | application/json                                      |
| errors.DeleteRelationRelationsResponse404ResponseBody | 404                                                   | application/json                                      |
| errors.SDKError                                       | 4x-5xx                                                | */*                                                   |

## get_relation

Get information about a relation

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.GetRelationRequest(
    company=734058,
    relation=979643,
)

res = s.relations.get_relation(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetRelationRequest](../../models/operations/getrelationrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetRelationResponse](../../models/operations/getrelationresponse.md)**
### Errors

| Error Object                                    | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| errors.GetRelationResponseBody                  | 401                                             | application/json                                |
| errors.GetRelationRelationsResponseBody         | 403                                             | application/json                                |
| errors.GetRelationRelationsResponseResponseBody | 404                                             | application/json                                |
| errors.SDKError                                 | 4x-5xx                                          | */*                                             |

## list_relations

List all the relations within a company

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.ListRelationsRequest(
    company=454135,
)

res = s.relations.list_relations(req)

if res.relation_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListRelationsRequest](../../models/operations/listrelationsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.ListRelationsResponse](../../models/operations/listrelationsresponse.md)**
### Errors

| Error Object                              | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.ListRelationsResponseBody          | 401                                       | application/json                          |
| errors.ListRelationsRelationsResponseBody | 403                                       | application/json                          |
| errors.SDKError                           | 4x-5xx                                    | */*                                       |

## update_relation

Update a relation

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

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
    company=573397,
    relation=281147,
)

res = s.relations.update_relation(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateRelationRequest](../../models/operations/updaterelationrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateRelationResponse](../../models/operations/updaterelationresponse.md)**
### Errors

| Error Object                                          | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| errors.UpdateRelationResponseBody                     | 401                                                   | application/json                                      |
| errors.UpdateRelationRelationsResponseBody            | 403                                                   | application/json                                      |
| errors.UpdateRelationRelationsResponseResponseBody    | 404                                                   | application/json                                      |
| errors.UpdateRelationRelationsResponse422ResponseBody | 422                                                   | application/json                                      |
| errors.SDKError                                       | 4x-5xx                                                | */*                                                   |
