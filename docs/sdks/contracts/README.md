# Contracts
(*contracts*)

### Available Operations

* [create_contract](#create_contract) - Create a contract
* [delete_contract](#delete_contract) - Delete a contract
* [get_contract](#get_contract) - Get a contract
* [list_contracts](#list_contracts) - List contracts
* [update_contract](#update_contract) - Update a contract

## create_contract

Create a contract

### Example Usage

```python
import contractifyproduction
import dateutil.parser
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.CreateContractRequest(
    contract_write=shared.ContractWrite(
        contract_types=[
            1,
            2,
        ],
        custom_field_values=[
            shared.CustomFieldValueWrite(
                custom_field_id=2,
                value='software',
            ),
        ],
        departments=[
            1,
            2,
        ],
        documents=[
            1,
        ],
        dossier_id=1,
        duration='P1Y',
        end_date=dateutil.parser.parse('2021-12-31').date(),
        legal_entities=[
            1,
            2,
        ],
        name='Partnership agreement',
        offices=[
            1,
            2,
        ],
        owner_id=1,
        phase=shared.ContractPhase.ONGOING,
        relations=[
            1,
            2,
        ],
        renewal=shared.ContractRenewal(
            automatic_renewal=shared.ContractAutomaticRenewal(
                number_of_renewals=1,
                renewal_period='P3Y',
            ),
        ),
        start_date=dateutil.parser.parse('2021-01-01').date(),
        termination=shared.ContractTermination(
            termination_date=dateutil.parser.parse('2021-11-30').date(),
            termination_duration='P1M',
        ),
    ),
    company=940947,
)

res = s.contracts.create_contract(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateContractRequest](../../models/operations/createcontractrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateContractResponse](../../models/operations/createcontractresponse.md)**
### Errors

| Error Object                                       | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| errors.CreateContractResponseBody                  | 401                                                | application/json                                   |
| errors.CreateContractContractsResponseBody         | 403                                                | application/json                                   |
| errors.CreateContractContractsResponseResponseBody | 422                                                | application/json                                   |
| errors.SDKError                                    | 400-600                                            | */*                                                |

## delete_contract

Delete a contract

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.DeleteContractRequest(
    company=791005,
    contract=200974,
)

res = s.contracts.delete_contract(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteContractRequest](../../models/operations/deletecontractrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.DeleteContractResponse](../../models/operations/deletecontractresponse.md)**
### Errors

| Error Object                                          | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| errors.DeleteContractResponseBody                     | 400                                                   | application/json                                      |
| errors.DeleteContractContractsResponseBody            | 401                                                   | application/json                                      |
| errors.DeleteContractContractsResponseResponseBody    | 403                                                   | application/json                                      |
| errors.DeleteContractContractsResponse404ResponseBody | 404                                                   | application/json                                      |
| errors.SDKError                                       | 400-600                                               | */*                                                   |

## get_contract

Get information about a contract

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.GetContractRequest(
    company=362495,
    contract=163842,
)

res = s.contracts.get_contract(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetContractRequest](../../models/operations/getcontractrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetContractResponse](../../models/operations/getcontractresponse.md)**
### Errors

| Error Object                                    | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| errors.GetContractResponseBody                  | 401                                             | application/json                                |
| errors.GetContractContractsResponseBody         | 403                                             | application/json                                |
| errors.GetContractContractsResponseResponseBody | 404                                             | application/json                                |
| errors.SDKError                                 | 400-600                                         | */*                                             |

## list_contracts

List all the contracts within a company

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.ListContractsRequest(
    company=567515,
)

res = s.contracts.list_contracts(req)

if res.contract_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListContractsRequest](../../models/operations/listcontractsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.ListContractsResponse](../../models/operations/listcontractsresponse.md)**
### Errors

| Error Object                              | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.ListContractsResponseBody          | 401                                       | application/json                          |
| errors.ListContractsContractsResponseBody | 403                                       | application/json                          |
| errors.SDKError                           | 400-600                                   | */*                                       |

## update_contract

Update a contract

### Example Usage

```python
import contractifyproduction
import dateutil.parser
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.UpdateContractRequest(
    contract_write=shared.ContractWrite(
        contract_types=[
            1,
            2,
        ],
        custom_field_values=[
            shared.CustomFieldValueWrite(
                custom_field_id=2,
                value='software',
            ),
        ],
        departments=[
            1,
            2,
        ],
        documents=[
            1,
        ],
        dossier_id=1,
        duration='P1Y',
        end_date=dateutil.parser.parse('2021-12-31').date(),
        legal_entities=[
            1,
            2,
        ],
        name='Partnership agreement',
        offices=[
            1,
            2,
        ],
        owner_id=1,
        phase=shared.ContractPhase.ONGOING,
        relations=[
            1,
            2,
        ],
        renewal=shared.ContractRenewal(
            automatic_renewal=shared.ContractAutomaticRenewal(
                number_of_renewals=1,
                renewal_period='P3Y',
            ),
        ),
        start_date=dateutil.parser.parse('2021-01-01').date(),
        termination=shared.ContractTermination(
            termination_date=dateutil.parser.parse('2021-11-30').date(),
            termination_duration='P1M',
        ),
    ),
    company=60280,
    contract=331790,
)

res = s.contracts.update_contract(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateContractRequest](../../models/operations/updatecontractrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateContractResponse](../../models/operations/updatecontractresponse.md)**
### Errors

| Error Object                                          | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| errors.UpdateContractResponseBody                     | 401                                                   | application/json                                      |
| errors.UpdateContractContractsResponseBody            | 403                                                   | application/json                                      |
| errors.UpdateContractContractsResponseResponseBody    | 404                                                   | application/json                                      |
| errors.UpdateContractContractsResponse422ResponseBody | 422                                                   | application/json                                      |
| errors.SDKError                                       | 400-600                                               | */*                                                   |
