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
        o_auth2="",
        personal_access_token="",
    ),
)

req = operations.CreateContractRequest(
    contract_write=shared.ContractWrite(
        contract_types=[
            940947,
        ],
        custom_field_values=[
            shared.CustomFieldValueWrite(
                custom_field_id=2,
                value='Palladium',
            ),
        ],
        departments=[
            559447,
        ],
        documents=[
            1,
        ],
        dossier_id=1,
        duration='P1Y',
        end_date=dateutil.parser.parse('2021-12-31').date(),
        is_open_ended=False,
        legal_entities=[
            657681,
        ],
        name='Partnership agreement',
        offices=[
            410255,
        ],
        owner_id=1,
        phase=shared.ContractPhase.ONGOING,
        relations=[
            867240,
        ],
        renewal=shared.ContractRenewal(
            automatic_renewal=shared.ContractAutomaticRenewal(
                number_of_renewals=1,
                renewal_period='P3Y',
            ),
            is_automatically_renewed=False,
        ),
        start_date=dateutil.parser.parse('2021-01-01').date(),
        termination=shared.ContractTermination(
            is_terminable_at_any_time=False,
            termination_date=dateutil.parser.parse('2021-11-30').date(),
            termination_duration='P1M',
        ),
    ),
    company=647814,
)

res = s.contracts.create_contract(req)

if res.create_contract_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateContractRequest](../../models/operations/createcontractrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateContractResponse](../../models/operations/createcontractresponse.md)**


## delete_contract

Delete a contract

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

req = operations.DeleteContractRequest(
    company=791005,
    contract=200974,
)

res = s.contracts.delete_contract(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteContractRequest](../../models/operations/deletecontractrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.DeleteContractResponse](../../models/operations/deletecontractresponse.md)**


## get_contract

Get information about a contract

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

req = operations.GetContractRequest(
    company=362495,
    contract=163842,
)

res = s.contracts.get_contract(req)

if res.get_contract_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetContractRequest](../../models/operations/getcontractrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetContractResponse](../../models/operations/getcontractresponse.md)**


## list_contracts

List all the contracts within a company

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

req = operations.ListContractsRequest(
    company=567515,
    page=62076,
)

res = s.contracts.list_contracts(req)

if res.contract_collection is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListContractsRequest](../../models/operations/listcontractsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.ListContractsResponse](../../models/operations/listcontractsresponse.md)**


## update_contract

Update a contract

### Example Usage

```python
import contractifyproduction
import dateutil.parser
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="",
        personal_access_token="",
    ),
)

req = operations.UpdateContractRequest(
    contract_write=shared.ContractWrite(
        contract_types=[
            60280,
        ],
        custom_field_values=[
            shared.CustomFieldValueWrite(
                custom_field_id=2,
                value='synergies',
            ),
        ],
        departments=[
            178046,
        ],
        documents=[
            1,
        ],
        dossier_id=1,
        duration='P1Y',
        end_date=dateutil.parser.parse('2021-12-31').date(),
        is_open_ended=False,
        legal_entities=[
            331597,
        ],
        name='Partnership agreement',
        offices=[
            693387,
        ],
        owner_id=1,
        phase=shared.ContractPhase.ONGOING,
        relations=[
            670029,
        ],
        renewal=shared.ContractRenewal(
            automatic_renewal=shared.ContractAutomaticRenewal(
                number_of_renewals=1,
                renewal_period='P3Y',
            ),
            is_automatically_renewed=False,
        ),
        start_date=dateutil.parser.parse('2021-01-01').date(),
        termination=shared.ContractTermination(
            is_terminable_at_any_time=False,
            termination_date=dateutil.parser.parse('2021-11-30').date(),
            termination_duration='P1M',
        ),
    ),
    company=213877,
    contract=177820,
)

res = s.contracts.update_contract(req)

if res.update_contract_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateContractRequest](../../models/operations/updatecontractrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateContractResponse](../../models/operations/updatecontractresponse.md)**

