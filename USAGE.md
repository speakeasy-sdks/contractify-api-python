<!-- Start SDK Example Usage -->
```python
import contractifyproduction
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.ListContractTypesRequest(
    company=548814,
)

res = s.contract_types.list_contract_types(req, operations.ListContractTypesSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.contract_type_collection is not None:
    # handle response
```
<!-- End SDK Example Usage -->