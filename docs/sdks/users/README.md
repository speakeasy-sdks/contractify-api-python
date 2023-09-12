# users

### Available Operations

* [current_user](#current_user) - Current User
* [list_users](#list_users) - List users

## current_user

Get the current user details

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()


res = s.users.current_user(operations.CurrentUserSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.current_user_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `security`                                                                       | [operations.CurrentUserSecurity](../../models/operations/currentusersecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.CurrentUserResponse](../../models/operations/currentuserresponse.md)**


## list_users

List all the users within a company

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import operations

s = contractifyproduction.ContractifyProduction()

req = operations.ListUsersRequest(
    company=943749,
    page=902599,
)

res = s.users.list_users(req, operations.ListUsersSecurity(
    o_auth2="",
    personal_access_token="",
))

if res.user_collection is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.ListUsersRequest](../../models/operations/listusersrequest.md)   | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `security`                                                                   | [operations.ListUsersSecurity](../../models/operations/listuserssecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.ListUsersResponse](../../models/operations/listusersresponse.md)**

