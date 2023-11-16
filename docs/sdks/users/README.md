# Users
(*users*)

### Available Operations

* [current_user](#current_user) - Current User
* [list_users](#list_users) - List users

## current_user

Get the current user details

### Example Usage

```python
import contractifyproduction
from contractifyproduction.models import shared

s = contractifyproduction.ContractifyProduction(
    security=shared.Security(
        o_auth2="",
        personal_access_token="",
    ),
)


res = s.users.current_user()

if res.two_hundred_application_json_object is not None:
    # handle response
    pass
```


### Response

**[operations.CurrentUserResponse](../../models/operations/currentuserresponse.md)**
### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.CurrentUserResponseBody      | 401                                 | application/json                    |
| errors.CurrentUserUsersResponseBody | 403                                 | application/json                    |
| errors.SDKError                     | 400-600                             | */*                                 |

## list_users

List all the users within a company

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

req = operations.ListUsersRequest(
    company=606239,
)

res = s.users.list_users(req)

if res.user_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListUsersRequest](../../models/operations/listusersrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.ListUsersResponse](../../models/operations/listusersresponse.md)**
### Errors

| Error Object                      | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ListUsersResponseBody      | 401                               | application/json                  |
| errors.ListUsersUsersResponseBody | 403                               | application/json                  |
| errors.SDKError                   | 400-600                           | */*                               |
