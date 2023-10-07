# Tasks
(*tasks*)

### Available Operations

* [create_task](#create_task) - Create a task
* [delete_task](#delete_task) - Delete a task
* [get_task](#get_task) - Get a task
* [list_tasks](#list_tasks) - List tasks
* [update_task](#update_task) - Update a task

## create_task

Create a task

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

req = operations.CreateTaskRequest(
    task_write=shared.TaskWrite(
        contract_id=1,
        description='Lorem ipsum dolor sit amet.',
        due_date=dateutil.parser.parse('2021-12-31').date(),
        due_date_depends_on=shared.TaskWriteDueDateDependsOn.END_DATE,
        due_date_interval='-P10D',
        owner_id=1,
        reminder_duration='P1M',
        repetition_interval='P1Y',
        status=shared.TaskWriteStatus.ACCOMPLISHED,
        title='My task',
    ),
    company=296904,
)

res = s.tasks.create_task(req)

if res.create_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.CreateTaskRequest](../../models/operations/createtaskrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.CreateTaskResponse](../../models/operations/createtaskresponse.md)**


## delete_task

Delete a task

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

req = operations.DeleteTaskRequest(
    company=357574,
    task=394977,
)

res = s.tasks.delete_task(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.DeleteTaskRequest](../../models/operations/deletetaskrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.DeleteTaskResponse](../../models/operations/deletetaskresponse.md)**


## get_task

Get a task

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

req = operations.GetTaskRequest(
    company=717011,
    task=649018,
)

res = s.tasks.get_task(req)

if res.get_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetTaskRequest](../../models/operations/gettaskrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetTaskResponse](../../models/operations/gettaskresponse.md)**


## list_tasks

List all tasks within a company

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

req = operations.ListTasksRequest(
    company=715197,
)

res = s.tasks.list_tasks(req)

if res.task_collection is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListTasksRequest](../../models/operations/listtasksrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.ListTasksResponse](../../models/operations/listtasksresponse.md)**


## update_task

Update a task

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

req = operations.UpdateTaskRequest(
    task_update=shared.TaskUpdate(
        description='Lorem ipsum dolor sit amet.',
        due_date=dateutil.parser.parse('2021-12-31').date(),
        due_date_depends_on=shared.TaskUpdateDueDateDependsOn.END_DATE,
        due_date_interval='-P10D',
        owner_id=1,
        reminder_duration='P1M',
        repetition_interval='P1Y',
        status=shared.TaskUpdateStatus.ACCOMPLISHED,
        title='My task',
    ),
    company=449699,
    task=675064,
)

res = s.tasks.update_task(req)

if res.update_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.UpdateTaskRequest](../../models/operations/updatetaskrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.UpdateTaskResponse](../../models/operations/updatetaskresponse.md)**

