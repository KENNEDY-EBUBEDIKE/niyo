
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




### User Auth Endpoints
##### 1. Create a new user
**Endpoint:** `POST /api/users/create/`

**Description:** This endpoint allows to create a new user.

**Request Body:**
- `email` (required): email
- `username` (required): Username
- `password` (required): Password

**Request:**
```bash
curl  -X POST \
  'http://127.0.0.1:8000/api/users/create/` \
  --header 'Content-Type: application/json'\
  --data-raw '{
    - "email": johndoe@mail.com
    - "username": John-DOE
    - "password": pass123
}'

```

**Response:**
```json
{
    "success": true,
    "message": "OK"
}
```


##### 2. Login
**Endpoint:** `POST /api/users/login/`

**Description:** This endpoint allows to create a user to login.

**Request Body:**
- `email` (required): email
- `password` (required): Password

**Request:**
```bash
curl  -X POST \
  'http://127.0.0.1:8000/api/users/login/` \
  --header 'Content-Type: application/json'\
  --data-raw '{
    - "email": johndoe@mail.com
    - "password": pass123
}'

```

**Response:**
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNjIyMTM2NCwiaWF0IjoxNzE2MTM0OTY0LCJqdGkiOiJlZTMwZWNjOTIwN2I0YmVhYjU2NmYxNDhhYmZmMjg3OSIsInVzZXJfaWQiOjF9.rgdICeQasw_DS1gIXcmPdxXIXWfF0cK9YhylUmMaHVQ",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MTUyOTY0LCJpYXQiOjE3MTYxMzQ5NjQsImp0aSI6ImY3YzBiZmVhOGQ3NDRkMTc5ZjVjMzE0NDA3NDE4YTliIiwidXNlcl9pZCI6MX0.cotBaVaxR5JY_wPrgPJTrIv5wwu6SYVEcjZI0nJNnk8"
}
```



##### 3. Get all Users
**Endpoint:** `GET /api/users/user/`

**Description:** This endpoint allows the user to get all Users.

**Request:**
```bash
curl  -X GET \
  'http://127.0.0.1:8000/api/users/user/` \
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
            "email": "ken@mailinator.com",
            "username": "EBUBEDIKE2"
        },
        {
            "id": 1,
            "email": "keny@gmail.com",
            "username": "OKOSISI"
        }
    ]
}
```


##### 3. Get the auth user's profile
**Endpoint:** `GET /api/users/me/`

**Description:** This endpoint allows the user to get his user profile.

**Request:**
```bash
curl  -X GET \
  'http://127.0.0.1:8000/api/users/me/` \
  --header 'Content-Type: application/json'\

```

**Response:**
```json
{
    "id": 1,
    "email": "keny@gmail.com",
    "username": "OKOSISI"
}
```

##### 4. Update the User details
**Endpoint:** `PATCH /api/users/edit/`

**Description:** This endpoint allows the auth user to Update a his details.


**Request:**
```bash
curl  -X PATCH \
  'http://127.0.0.1:8000/api/users/edit/` \
  --header 'Content-Type: application/json'\
    --data-raw '{
    - "username": Abobby
}'

```

**Response:**
```json
{
    "success": true,
    "message": "User Data updated successfully"
}
```
