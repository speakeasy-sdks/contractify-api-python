# contractify

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/contractify-api-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="",
        personal_access_token="",
    ),
)

req = operations.ListContractTypesRequest(
    company=592845,
)

res = s.contract_types.list_contract_types(req)

if res.contract_type_collection is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [ContractTypes](docs/sdks/contracttypes/README.md)

* [list_contract_types](docs/sdks/contracttypes/README.md#list_contract_types) - List contract types

### [Contracts](docs/sdks/contracts/README.md)

* [create_contract](docs/sdks/contracts/README.md#create_contract) - Create a contract
* [delete_contract](docs/sdks/contracts/README.md#delete_contract) - Delete a contract
* [get_contract](docs/sdks/contracts/README.md#get_contract) - Get a contract
* [list_contracts](docs/sdks/contracts/README.md#list_contracts) - List contracts
* [update_contract](docs/sdks/contracts/README.md#update_contract) - Update a contract

### [CustomFields](docs/sdks/customfields/README.md)

* [list_custom_fields](docs/sdks/customfields/README.md#list_custom_fields) - List custom fields

### [Departments](docs/sdks/departments/README.md)

* [create_department](docs/sdks/departments/README.md#create_department) - Create a department
* [delete_department](docs/sdks/departments/README.md#delete_department) - Delete a department
* [get_department](docs/sdks/departments/README.md#get_department) - Get a department
* [list_departments](docs/sdks/departments/README.md#list_departments) - List departments
* [update_department](docs/sdks/departments/README.md#update_department) - Update a department

### [Documents](docs/sdks/documents/README.md)

* [delete_document](docs/sdks/documents/README.md#delete_document) - Delete a document
* [get_document](docs/sdks/documents/README.md#get_document) - Get a document
* [list_documents](docs/sdks/documents/README.md#list_documents) - List documents
* [update_document](docs/sdks/documents/README.md#update_document) - Update a document

### [LegalEntities](docs/sdks/legalentities/README.md)

* [list_legal_entities](docs/sdks/legalentities/README.md#list_legal_entities) - List legal entities

### [Offices](docs/sdks/offices/README.md)

* [create_office](docs/sdks/offices/README.md#create_office) - Create an office
* [delete_office](docs/sdks/offices/README.md#delete_office) - Delete an office
* [get_office](docs/sdks/offices/README.md#get_office) - Get an office
* [list_offices](docs/sdks/offices/README.md#list_offices) - List offices
* [update_office](docs/sdks/offices/README.md#update_office) - Update an office

### [Relations](docs/sdks/relations/README.md)

* [create_relation](docs/sdks/relations/README.md#create_relation) - Create a relation
* [delete_relation](docs/sdks/relations/README.md#delete_relation) - Delete a relation
* [get_relation](docs/sdks/relations/README.md#get_relation) - Get a relation
* [list_relations](docs/sdks/relations/README.md#list_relations) - List relations
* [update_relation](docs/sdks/relations/README.md#update_relation) - Update a relation

### [Subfolders](docs/sdks/subfolders/README.md)

* [list_subfolders](docs/sdks/subfolders/README.md#list_subfolders) - List subfolders

### [Tasks](docs/sdks/tasks/README.md)

* [create_task](docs/sdks/tasks/README.md#create_task) - Create a task
* [delete_task](docs/sdks/tasks/README.md#delete_task) - Delete a task
* [get_task](docs/sdks/tasks/README.md#get_task) - Get a task
* [list_tasks](docs/sdks/tasks/README.md#list_tasks) - List tasks
* [update_task](docs/sdks/tasks/README.md#update_task) - Update a task

### [Users](docs/sdks/users/README.md)

* [current_user](docs/sdks/users/README.md#current_user) - Current User
* [list_users](docs/sdks/users/README.md#list_users) - List users
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
