
### Tasks Endpoints
##### 1. Create a new task
**Endpoint:** `POST /api/tasks/`

**Description:** This endpoint allows the user to create a new task.

**Request Body:**
- `title` (required): Title of the task
- `description` (required): Task Description

**Request:**
```bash
curl  -X POST \
  'http://127.0.0.1:8000/api/tasks/` \
  --header 'Content-Type: application/json'\
  --data-raw '{
    - "title": Task Title 1
    - "description": This is a task decription
}'

```

**Response:**
```json
{
    "success": true,
    "message": "OK"
}
```

##### 2. Get all tasks
**Endpoint:** `GET /api/tasks/`

**Description:** This endpoint allows the user to get all tasks.

**Request:**
```bash
curl  -X GET \
  'http://127.0.0.1:8000/api/tasks/` \
  --header 'Content-Type: application/json'\

```

**Response:**
```json
{
    "success": true,
    "message": "OK",
    "data": [
        {
            "id": 2,
            "title": "Task 2",
            "description": "This is task 2",
            "completed": false,
            "created_at": "2024-05-19T13:01:44.367685+01:00",
            "updated_at": "2024-05-19T13:01:44.367756+01:00"
        },
        {
            "id": 3,
            "title": "Task 3",
            "description": "This is task 3",
            "completed": false,
            "created_at": "2024-05-19T13:24:29.795735+01:00",
            "updated_at": "2024-05-19T13:24:29.795801+01:00"
        },
        {
            "id": 4,
            "title": "Task 4",
            "description": "This is task 4",
            "completed": false,
            "created_at": "2024-05-19T14:03:59.082429+01:00",
            "updated_at": "2024-05-19T14:03:59.082496+01:00"
        }
    ]
}
```

##### 3. Get a single task
**Endpoint:** `GET /api/tasks/<task_id>/`

**Description:** This endpoint allows the user to get a single task.


**Request:**
```bash
curl  -X GET \
  'http://127.0.0.1:8000/api/tasks/2/` \
  --header 'Content-Type: application/json'\

```

**Response:**
```json
{
    "success": true,
    "message": "OK",
    "data": {
        "id": 2,
        "title": "Task 2",
        "description": "This is task 2",
        "completed": false,
        "created_at": "2024-05-19T13:01:44.367685+01:00",
        "updated_at": "2024-05-19T13:01:44"
    }
}
```

##### 4. Update a single task
**Endpoint:** `PATCH /api/tasks/<task_id>/`

**Description:** This endpoint allows the user to Update a single task.


**Request:**
```bash
curl  -X PATCH \
  'http://127.0.0.1:8000/api/tasks/2/` \
  --header 'Content-Type: application/json'\
    --data-raw '{
    - "description": This is a task has been updated
}'

```

**Response:**
```json
{
    "success": true,
    "message": "OK",
    "data": {
        "id": 2,
        "title": "Task 2",
        "description": "This is a task has been updated",
        "completed": false,
        "created_at": "2024-05-19T11:01:09.598767+01:00",
        "updated_at": "2024-05-19T13:41:52.000123+01:00"
    }
}
```


##### 4. Delete a task
**Endpoint:** `DELETE /api/tasks/<task_id>/`

**Description:** This endpoint allows the user to delete a task.

**Request:**
```bash
curl  -X DELETE \
  'http://127.0.0.1:8000/api/tasks/2/` \
  --header 'Content-Type: application/json'\

```

**Response:**

```json
{
    "success": true,
    "message": "Task Deleted"
}
```
