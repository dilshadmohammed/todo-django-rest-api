
# Todo App API Documentation

## Authentication

### User Sign Up
- **URL:** `POST https://dilshadvlnnssce.pythonanywhere.com/users/signup/`
- **Request Body (Form Data):**
  - `username`: testuser
  - `password`: 123456
  - **Response Body:**
    ```json
    {
      "user": {
        "id": 1,
        "username": "testuser"
      },
      "refresh": "<refresh_token>",
      "access": "<access_token>"
    }
    ```

### User Login
- **URL:** `POST https://dilshadvlnnssce.pythonanywhere.com/users/login/`
- **Request Body (Form Data):**
  - `username`: testuser
  - `password`: 123456
  - **Response Body:**
    ```json
    {
      "user": {
        "id": 1,
        "username": "testuser"
      },
      "refresh": "<refresh_token>",
      "access": "<access_token>"
    }
    ```

## Todo Operations

### Create Todo
- **URL:** `POST https://dilshadvlnnssce.pythonanywhere.com/todos/`
- **Authorization Header:** Bearer `<access_token>`
- **Request Body:**
  ```json
  {
    "task": "Sample task",
    "expiry": "{{$isoTimestamp}}"
  }
  ```
 - **Response Body:**
   ```json
   {  "id":  3, 
    "task":  "Sample task",  
    "completed":  false,  
    "expiry":  "2024-05-07T06:02:04.859000Z" 
    }
   ```
    
    ### Get all Todos
- **URL:** `GET https://dilshadvlnnssce.pythonanywhere.com/todos/`
- **Description:** 
 -- Get all todos by default or use params `filter=` `completed` or `expired` to get filtered view. 
-- if you want a todo with an id use `GET https://dilshadvlnnssce.pythonanywhere.com/todos/{id}`
- **Authorization Header:** Bearer `<access_token>`
 - **Response Body:**
   ```json
   [  {  "id":  1,  
	   "task":  "first task",
	    "completed":  true,
	    "expiry":  "2024-05-07T06:00:08.818000Z"
	   },
	   {  "id":  3,  
		   "task":  "Sample task",
		   "completed":  true,
		   "expiry":  "2024-05-07T06:02:04.859000Z"  
		}  ]
    ```


### Delete Todo
- **URL:** `DELETE https://dilshadvlnnssce.pythonanywhere.com/todos/{id}/`
- **Authorization Header:** Bearer `<access_token>`
 - **Response Body:**
   ```json
   { 
    "message" : "Todo deleted successfully." 
    }
   ```

### Toggle Todo
- **URL:** `POST dilshadvlnnssce.pythonanywhere.com/todos/{id}/complete/`
- **Authorization Header:** Bearer `<access_token>`
 - **Response Body:**
   ```json
   {  "id":  3,  
	   "task":  
		"Sample task",  
		"completed":  true,  
		"expiry":  "2024-05-07T06:02:04.859000Z"
	}
   ```



