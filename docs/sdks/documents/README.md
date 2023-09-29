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
    company=431806,
    document=379848,
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
    company=67810,
    document=267106,
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
    company=581480,
    esigning_status=operations.ListDocumentsEsigningStatus.LEGAL_DECLINED,
    esigning_updated_after=dateutil.parser.isoparse('2022-04-10T07:42:42.736Z'),
    page=893340,
    relation_id=873217,
    signed_after=dateutil.parser.isoparse('2021-04-10T09:49:45.540Z'),
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
                value='Product',
            ),
        ],
        description='Lorem ipsum dolor sit amet.',
        dossiers=[
            1,
        ],
        name='filename.pdf',
        owner_id=1,
    ),
    company=659951,
    document=513682,
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

