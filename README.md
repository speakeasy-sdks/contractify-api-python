# contractify

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/speakeasy-sdks/contractify-api-python.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/contractify-api-python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README
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
    company=839467,
)

res = s.contract_types.list_contract_types(req)

if res.contract_type_collection is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [contract_types](docs/sdks/contracttypes/README.md)

* [list_contract_types](docs/sdks/contracttypes/README.md#list_contract_types) - List contract types

### [contracts](docs/sdks/contracts/README.md)

* [create_contract](docs/sdks/contracts/README.md#create_contract) - Create a contract
* [delete_contract](docs/sdks/contracts/README.md#delete_contract) - Delete a contract
* [get_contract](docs/sdks/contracts/README.md#get_contract) - Get a contract
* [list_contracts](docs/sdks/contracts/README.md#list_contracts) - List contracts
* [update_contract](docs/sdks/contracts/README.md#update_contract) - Update a contract

### [custom_fields](docs/sdks/customfields/README.md)

* [list_custom_fields](docs/sdks/customfields/README.md#list_custom_fields) - List custom fields

### [departments](docs/sdks/departments/README.md)

* [create_department](docs/sdks/departments/README.md#create_department) - Create a department
* [delete_department](docs/sdks/departments/README.md#delete_department) - Delete a department
* [get_department](docs/sdks/departments/README.md#get_department) - Get a department
* [list_departments](docs/sdks/departments/README.md#list_departments) - List departments
* [update_department](docs/sdks/departments/README.md#update_department) - Update a department

### [documents](docs/sdks/documents/README.md)

* [delete_document](docs/sdks/documents/README.md#delete_document) - Delete a document
* [get_document](docs/sdks/documents/README.md#get_document) - Get a document
* [list_documents](docs/sdks/documents/README.md#list_documents) - List documents
* [update_document](docs/sdks/documents/README.md#update_document) - Update a document

### [subfolders](docs/sdks/subfolders/README.md)

* [list_subfolders](docs/sdks/subfolders/README.md#list_subfolders) - List subfolders

### [legal_entities](docs/sdks/legalentities/README.md)

* [list_legal_entities](docs/sdks/legalentities/README.md#list_legal_entities) - List legal entities

### [offices](docs/sdks/offices/README.md)

* [create_office](docs/sdks/offices/README.md#create_office) - Create an office
* [delete_office](docs/sdks/offices/README.md#delete_office) - Delete an office
* [get_office](docs/sdks/offices/README.md#get_office) - Get an office
* [list_offices](docs/sdks/offices/README.md#list_offices) - List offices
* [update_office](docs/sdks/offices/README.md#update_office) - Update an office

### [relations](docs/sdks/relations/README.md)

* [create_relation](docs/sdks/relations/README.md#create_relation) - Create a relation
* [delete_relation](docs/sdks/relations/README.md#delete_relation) - Delete a relation
* [get_relation](docs/sdks/relations/README.md#get_relation) - Get a relation
* [list_relations](docs/sdks/relations/README.md#list_relations) - List relations
* [update_relation](docs/sdks/relations/README.md#update_relation) - Update a relation

### [tasks](docs/sdks/tasks/README.md)

* [create_task](docs/sdks/tasks/README.md#create_task) - Create a task
* [delete_task](docs/sdks/tasks/README.md#delete_task) - Delete a task
* [get_task](docs/sdks/tasks/README.md#get_task) - Get a task
* [list_tasks](docs/sdks/tasks/README.md#list_tasks) - List tasks
* [update_task](docs/sdks/tasks/README.md#update_task) - Update a task

### [users](docs/sdks/users/README.md)

* [current_user](docs/sdks/users/README.md#current_user) - Current User
* [list_users](docs/sdks/users/README.md#list_users) - List users
<!-- End SDK Available Operations -->

<!-- Start Dev Containers -->

<!-- End Dev Containers -->

<!-- Start Error Handling -->
# Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                                      | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| errors.ListContractTypesResponseBody              | 401                                               | application/json                                  |
| errors.ListContractTypesContractTypesResponseBody | 403                                               | application/json                                  |
| errors.SDKError                                   | 400-600                                           | */*                                               |


## Example

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
    company=839467,
)

res = None
try:
    res = s.contract_types.list_contract_types(req)
except (errors.ListContractTypesResponseBody) as e:
    print(e) # handle exception
except (errors.ListContractTypesContractTypesResponseBody) as e:
    print(e) # handle exception

except (errors.SDKError) as e:
    print(e) # handle exception


if res.contract_type_collection is not None:
    # handle response
    pass
```
<!-- End Error Handling -->

<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://app.contractify.be` | None |

For example:

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    server_idx=0,
    security=shared.Security(
        o_auth2="",
        personal_access_token="",
    ),
)

req = operations.ListContractTypesRequest(
    company=839467,
)

res = s.contract_types.list_contract_types(req)

if res.contract_type_collection is not None:
    # handle response
    pass
```


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    server_url="https://app.contractify.be",
    security=shared.Security(
        o_auth2="",
        personal_access_token="",
    ),
)

req = operations.ListContractTypesRequest(
    company=839467,
)

res = s.contract_types.list_contract_types(req)

if res.contract_type_collection is not None:
    # handle response
    pass
```
<!-- End Server Selection -->

<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that this sdk makes as follows:

```python
import contractifyproduction
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = contractifyproduction.ContractifyProduction(client: http_client)
```
<!-- End Custom HTTP Client -->



<!-- Start Authentication -->
# Authentication

## Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name                    | Type                    | Scheme                  |
| ----------------------- | ----------------------- | ----------------------- |
| `o_auth2`               | oauth2                  | OAuth2 token            |
| `personal_access_token` | http                    | HTTP Bearer             |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:

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
    company=839467,
)

res = s.contract_types.list_contract_types(req)

if res.contract_type_collection is not None:
    # handle response
    pass
```
<!-- End Authentication -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
