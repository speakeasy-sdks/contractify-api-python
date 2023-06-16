# TaskRead


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `contract_id`                                                                         | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | N/A                                                                                   | 1                                                                                     |
| `description`                                                                         | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | N/A                                                                                   | Lorem ipsum dolor sit amet.                                                           |
| `due_date`                                                                            | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)          | :heavy_minus_sign:                                                                    | N/A                                                                                   | 2021-12-31                                                                            |
| `due_date_depends_on`                                                                 | [Optional[TaskReadDueDateDependsOn]](../../models/shared/taskreadduedatedependson.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   | end_date                                                                              |
| `due_date_interval`                                                                   | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | N/A                                                                                   | -P10D                                                                                 |
| `escalation_date`                                                                     | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)          | :heavy_minus_sign:                                                                    | N/A                                                                                   | 2021-12-20                                                                            |
| `id`                                                                                  | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | N/A                                                                                   | 1                                                                                     |
| `owner_id`                                                                            | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | N/A                                                                                   | 1                                                                                     |
| `permalink`                                                                           | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | N/A                                                                                   | https://app.contractify.io/client/company/company-slug/tasks/1                        |
| `reminder_date`                                                                       | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)          | :heavy_minus_sign:                                                                    | N/A                                                                                   | 2021-11-30                                                                            |
| `reminder_duration`                                                                   | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | N/A                                                                                   | P1M                                                                                   |
| `repetition_interval`                                                                 | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | N/A                                                                                   | P1Y                                                                                   |
| `status`                                                                              | [Optional[TaskReadStatus]](../../models/shared/taskreadstatus.md)                     | :heavy_minus_sign:                                                                    | N/A                                                                                   | accomplished                                                                          |
| `title`                                                                               | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | N/A                                                                                   | My task                                                                               |