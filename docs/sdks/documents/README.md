# documents

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
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.DeleteDocumentRequest(
    company=18789,
    document=324141,
)

res = s.documents.delete_document(req, operations.DeleteDocumentSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.DeleteDocumentRequest](../../models/operations/deletedocumentrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.DeleteDocumentSecurity](../../models/operations/deletedocumentsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.DeleteDocumentResponse](../../models/operations/deletedocumentresponse.md)**


## get_document

Get information about a document

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.GetDocumentRequest(
    company=617636,
    document=149675,
)

res = s.documents.get_document(req, operations.GetDocumentSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.get_document_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetDocumentRequest](../../models/operations/getdocumentrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.GetDocumentSecurity](../../models/operations/getdocumentsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.GetDocumentResponse](../../models/operations/getdocumentresponse.md)**


## list_documents

List all the documents within a company

### Example Usage

```python
import contractifyproduction
import dateutil.parser
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.ListDocumentsRequest(
    company=612096,
    esigning_status=operations.ListDocumentsEsigningStatus.SENT_TO_LEGAL,
    esigning_updated_after=dateutil.parser.isoparse('2022-03-24T20:42:46.563Z'),
    page=943749,
    relation_id=902599,
    signed_after=dateutil.parser.isoparse('2022-02-06T12:52:33.708Z'),
)

res = s.documents.list_documents(req, operations.ListDocumentsSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.document_collection is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListDocumentsRequest](../../models/operations/listdocumentsrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.ListDocumentsSecurity](../../models/operations/listdocumentssecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.ListDocumentsResponse](../../models/operations/listdocumentsresponse.md)**


## update_document

Update a document

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations, shared

s = contractifyproduction.ContractifyProduction()

req = operations.UpdateDocumentRequest(
    document_write=shared.DocumentWrite(
        contracts=[
            1,
            1,
        ],
        custom_field_values=[
            shared.CustomFieldValueWrite(
                custom_field_id=2,
                value='iure',
            ),
            shared.CustomFieldValueWrite(
                custom_field_id=2,
                value='saepe',
            ),
            shared.CustomFieldValueWrite(
                custom_field_id=2,
                value='quidem',
            ),
        ],
        description='Lorem ipsum dolor sit amet.',
        dossiers=[
            1,
        ],
        name='filename.pdf',
        owner_id=1,
    ),
    company=60225,
    document=969810,
)

res = s.documents.update_document(req, operations.UpdateDocumentSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.update_document_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateDocumentRequest](../../models/operations/updatedocumentrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.UpdateDocumentSecurity](../../models/operations/updatedocumentsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.UpdateDocumentResponse](../../models/operations/updatedocumentresponse.md)**
