# Documents
(*documents*)

### Available Operations

* [delete_document](#delete_document) - Delete a document
* [get_document](#get_document) - Get a document
* [list_documents](#list_documents) - List documents
* [update_document](#update_document) - Update a document

## delete_document

Delete a document

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.DeleteDocumentRequest(
    company=431806,
    document=379848,
)

res = s.documents.delete_document(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteDocumentRequest](../../models/operations/deletedocumentrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.DeleteDocumentResponse](../../models/operations/deletedocumentresponse.md)**
### Errors

| Error Object                                          | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| errors.DeleteDocumentResponseBody                     | 401                                                   | application/json                                      |
| errors.DeleteDocumentDocumentsResponseBody            | 403                                                   | application/json                                      |
| errors.DeleteDocumentDocumentsResponseResponseBody    | 404                                                   | application/json                                      |
| errors.DeleteDocumentDocumentsResponse422ResponseBody | 422                                                   | application/json                                      |
| errors.SDKError                                       | 4x-5xx                                                | */*                                                   |

## get_document

Get information about a document

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.GetDocumentRequest(
    company=67810,
    document=267106,
)

res = s.documents.get_document(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetDocumentRequest](../../models/operations/getdocumentrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetDocumentResponse](../../models/operations/getdocumentresponse.md)**
### Errors

| Error Object                                    | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| errors.GetDocumentResponseBody                  | 401                                             | application/json                                |
| errors.GetDocumentDocumentsResponseBody         | 403                                             | application/json                                |
| errors.GetDocumentDocumentsResponseResponseBody | 404                                             | application/json                                |
| errors.SDKError                                 | 4x-5xx                                          | */*                                             |

## list_documents

List all the documents within a company

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

req = operations.ListDocumentsRequest(
    company=581480,
)

res = s.documents.list_documents(req)

if res.document_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListDocumentsRequest](../../models/operations/listdocumentsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.ListDocumentsResponse](../../models/operations/listdocumentsresponse.md)**
### Errors

| Error Object                              | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.ListDocumentsResponseBody          | 401                                       | application/json                          |
| errors.ListDocumentsDocumentsResponseBody | 403                                       | application/json                          |
| errors.SDKError                           | 4x-5xx                                    | */*                                       |

## update_document

Update a document

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.UpdateDocumentRequest(
    document_write=shared.DocumentWrite(
        contracts=[
            1,
        ],
        custom_field_values=[
            shared.CustomFieldValueWrite(
                custom_field_id=2,
                value='software',
            ),
        ],
        description='Lorem ipsum dolor sit amet.',
        dossiers=[
            1,
        ],
        name='filename.pdf',
        owner_id=1,
    ),
    company=653381,
    document=312704,
)

res = s.documents.update_document(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateDocumentRequest](../../models/operations/updatedocumentrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateDocumentResponse](../../models/operations/updatedocumentresponse.md)**
### Errors

| Error Object                                       | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| errors.UpdateDocumentResponseBody                  | 401                                                | application/json                                   |
| errors.UpdateDocumentDocumentsResponseBody         | 403                                                | application/json                                   |
| errors.UpdateDocumentDocumentsResponseResponseBody | 404                                                | application/json                                   |
| errors.SDKError                                    | 4x-5xx                                             | */*                                                |
