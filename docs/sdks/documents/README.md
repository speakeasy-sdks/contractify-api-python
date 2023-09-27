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
        o_auth2="",
        personal_access_token="",
    ),
)

req = operations.DeleteDocumentRequest(
    company=368241,
    document=832620,
)

res = s.documents.delete_document(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteDocumentRequest](../../models/operations/deletedocumentrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.DeleteDocumentResponse](../../models/operations/deletedocumentresponse.md)**


## get_document

Get information about a document

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

req = operations.GetDocumentRequest(
    company=957156,
    document=778157,
)

res = s.documents.get_document(req)

if res.get_document_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetDocumentRequest](../../models/operations/getdocumentrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetDocumentResponse](../../models/operations/getdocumentresponse.md)**


## list_documents

List all the documents within a company

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

req = operations.ListDocumentsRequest(
    company=140350,
    esigning_status=operations.ListDocumentsEsigningStatus.FINISHED_BUT_PARTIALLY_SIGNED,
    esigning_updated_after=dateutil.parser.isoparse('2020-01-25T09:54:35.794Z'),
    page=473608,
    relation_id=799159,
    signed_after=dateutil.parser.isoparse('2021-08-13T16:19:19.906Z'),
)

res = s.documents.list_documents(req)

if res.document_collection is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListDocumentsRequest](../../models/operations/listdocumentsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.ListDocumentsResponse](../../models/operations/listdocumentsresponse.md)**


## update_document

Update a document

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

req = operations.UpdateDocumentRequest(
    document_write=shared.DocumentWrite(
        contracts=[
            1,
        ],
        custom_field_values=[
            shared.CustomFieldValueWrite(
                custom_field_id=2,
                value='totam',
            ),
        ],
        description='Lorem ipsum dolor sit amet.',
        dossiers=[
            1,
        ],
        name='filename.pdf',
        owner_id=1,
    ),
    company=780529,
    document=678880,
)

res = s.documents.update_document(req)

if res.update_document_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateDocumentRequest](../../models/operations/updatedocumentrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateDocumentResponse](../../models/operations/updatedocumentresponse.md)**

