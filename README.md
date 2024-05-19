# Niyo Project


## Instructions

Prerequisites: Ensure you have docker installed in your system

1. Clone the project
2. cd into the project directory
3. run `docker compose build`
4. run `docker compose up`



## Other Info

- Make requests through the server url http://127.0.0.1:8000/
- See the API_DOCUMENTATION.md file for API endpoints documentation
- All routes (endpoints) are protected except
  - 1. http://127.0.0.1:8000/api/users/create/ - for new user
    2. http://127.0.0.1:8000/api/users/login/ - for login



### To get the Live streamed data, connect to the websocket through the ws url
websocket Url = `ws://127.0.0.1:8001/ws/tasks/`
