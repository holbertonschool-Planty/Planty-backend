# Planty-backend
This Django backend service provides a RESTful API to manage various data models including plants, devices, users among others and an notification system. The API serves as a central platform to handle operations related to these entities, offering endpoints for creation, retrieval, modification, and deletion of model instances.
## Index

- [Installation](#installation)
- [API](#api)
- [Creators](#creators)

## Installation

### Docker and Docker Compose:

Ensure you have Docker and Docker Compose installed on your machine. If not, you can download and follow the installation instructions from the [Official Docker page](https://docs.docker.com/get-docker/).

### Port Configuration:

By default, the application inside the container listens on port **8000**. However, to access it from your host machine, you'll use port **8080**. The **docker-compose.yml** configuration maps port **8080** on your host machine to port **8000** inside the container.

### Starting the Service:

To build and start the service, simply run(**Ubuntu**):

    bash run start

To build and start the service, simply run(**Windows**):

    docker-compose build
    docker-compose -f docker-compose.yml up

Once the service is up, you can access the API at **http://localhost:8080**.



## API

<details>
<summary><b>Plants Information Endpoints</b></summary>


**Endpoint:** `/plants_info`

**Method:** `GET`

**Description:**
Retrieves a list of all plant information records.

**Parameters:** 
- `None` 

**Possible status codes:**

    200 OK: Successfully retrieved the list of plant information.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    200 OK:
```json
[
    {
        "id": "b4155bcf-db9e-445e-bb9c-86bbb03ec2cd",
        "scientific_name": "Plantago major",
        "station": "Indoor",
        "temperature": 22,
        "light": 80,
        "watering": 3,
        "water_frequency": 3
    },
    {
        "id": "2da4e546-bc3d-4db9-84a8-1ae5ef79f4eb",
        "scientific_name": "Ficus lyrata",
        "station": "Outdoor",
        "temperature": 25,
        "light": 90,
        "watering": 2,
        "water_frequency": 3
    },
    ...
]
```

**Endpoint:** `/plants_info/{plants_info_id}`

**Method:** `GET`

**Description:**
Fetches details of a plant using its plants_info_id.

**Parameters:** 
- `plants_info_id` (UUID): Unique identifier for a plant information record. 

**Possible status codes:**

    200 OK: Successfully retrieved the details of the specified plant.
    404 Not Found: No plant information found for the provided plants_info_id.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    200 OK:
```json
{
    "id": "b4155bcf-db9e-445e-bb9c-86bbb03ec2cd",
    "scientific_name": "Plantago major",
    "station": "Indoor",
    "temperature": 22,
    "light": 80,
    "watering": 3,
    "water_frequency": 3
}
```

    404: Not Found:
```json
{
    "detail": "Not Found: No Plants_info matches the given query."
}
```

**Endpoint:** `/plants_info`

**Method:** `POST`

**Description:**
Adds new plant details.

**Parameters:** 
- `None`

**Payload:**
```json
{
    "scientific_name": "string",
    "station": "string",
    "temperature": 0,
    "light": 0,
    "watering": 0,
    "water_frequency": 0
}
```

**Possible status codes:**

    201 Created: Successfully added the new plant information.
    400 Bad Request: Invalid input data.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    201 Created:
```json
{
    "id": "b4155bcf-db9e-445e-bb9c-86bbb03ec2cd",
    "scientific_name": "Plantago major",
    "station": "Indoor",
    "temperature": 22,
    "light": 80,
    "watering": 3,
    "water_frequency": 3
}
```

**Endpoint:** `/plants_info/list/`

**Method:** `POST`

**Description:**
Adds a list of new plant details.

**Parameters:** 
- `None`

**Payload:**
```json
[
  {
    "scientific_name": "string",
    "station": "string",
    "temperature": 0,
    "light": 0,
    "watering": 0,
    "water_frequency": 0
  }
]
```

**Possible status codes:**

    201 Created: Successfully added the list with new plants information.
    400 Bad Request: Invalid input data.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    201 Created:
```json
[
    {
        "id": "b4155bcf-db9e-445e-bb9c-86bbb03ec2cd",
        "scientific_name": "Plantago major",
        "station": "Indoor",
        "temperature": 22,
        "light": 80,
        "watering": 3,
        "water_frequency": 3
    },
    {
        "id": "2da4e546-bc3d-4db9-84a8-1ae5ef79f4eb",
        "scientific_name": "Ficus lyrata",
        "station": "Outdoor",
        "temperature": 25,
        "light": 90,
        "watering": 2,
        "water_frequency": 3
    },
    ...
]
```


**Endpoint:** `/plants_info/{plants_info_id}`

**Method:** `PUT`

**Description:**
Updates details of a plant using its plants_info_id.

**Parameters:** 
- `plants_info_id` (UUID): Unique identifier for a plant information.

**Payload:**
```json
{
    "scientific_name": "string",
    "station": "string",
    "temperature": 0,
    "light": 0,
    "watering": 0,
    "water_frequency": 0
}
```

**Possible status codes:**

    200 OK: Successfully updated the plant information.
    400 Bad Request: Invalid input data.
    404 Not Found: No plant information found for the provided plants_info_id.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    200 OK:
```json
{
    "id": "b4155bcf-db9e-445e-bb9c-86bbb03ec2cd",
    "scientific_name": "Plantago major",
    "station": "Indoor",
    "temperature": 20,
    "light": 75,
    "watering": 3,
    "water_frequency": 4
}
```

    404: Not Found:
```json
{
    "detail": "Not Found: No Plants_info matches the given query."
}
```

**Endpoint:** `/plants_info/{plants_info_id}`

**Method:** `DELETE`

**Description:**
Deletes a plant's details using its plants_info_id.

**Parameters:** 
- `plants_info_id` (UUID): Unique identifier for a plant information.

**Possible status codes:**

    200 OK: Successfully updated the plant information.
    404 Not Found: No plant information found for the provided plants_info_id.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    200 OK:
```json
{
    "message": "Plant information deleted successfully."
}
```

    404: Not Found:
```json
{
    "detail": "Not Found: No Plants_info matches the given query."
}
```

</details>


<details>
<summary><b>Planty Endpoints</b></summary>


**Endpoint:** `/planty/{planty_id}`

**Method:** `GET`

**Description:**
Fetches details of a planty using its planty_id.

**Parameters:** 
- `planty_id` (UUID): Unique identifier for a planty device.

**Possible status codes:**

    200 OK: Successfully retrieved the details of the specified planty.
    404 Not Found: No planty found for the provided planty_id.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    200 OK:
```json
{
    "id": "f60e53b4-a776-4d24-96c5-6e2164b5c9e3",
    "serie": "123abc",
    "timezone": 0,
    "actual_temperature": [
        0
    ],
    "actual_light": [
        0
    ],
    "actual_watering": [
        0
    ],
    "plants_info": {
        "id": "b4155bcf-db9e-445e-bb9c-86bbb03ec2cd",
        "scientific_name": "Plantago major",
        "station": "Indoor",
        "temperature": 22,
        "light": 80,
        "watering": 3,
        "water_frequency": 3
        }
}
```

    404: Not Found:
```json
{
    "detail": "Not Found: No Planty matches the given query."
}
```

**Endpoint:** `/planty`

**Method:** `POST`

**Description:**
Creates a new planty device.

**Parameters:** 
- `None`

**Possible status codes:**

    201 Created: Successfully created the new planty device.
    400 Bad Request: Invalid input data.
    409 Conflict: A conflict arises when attempting to create a device with a series that already exists in the database.
    500 Internal Server Error: Server error during the operation.

**Payload:**
```json
{
    "serie": "string",
    "timezone": 0,
    "actual_temperature": 0,
    "actual_light": 0,
    "actual_watering": 0,
    "plants_info_id": "string"
}
```

**Responses:**

    201 Created:
```json
{
    "id": "f60e53b4-a776-4d24-96c5-6e2164b5c9e3",
    "serie": "123abc",
    "timezone": 0,
    "actual_temperature": [
        0
    ],
    "actual_light": [
        0
    ],
    "actual_watering": [
        0
    ],
    "plants_info": {
        "id": "b4155bcf-db9e-445e-bb9c-86bbb03ec2cd",
        "scientific_name": "Plantago major",
        "station": "Indoor",
        "temperature": 22,
        "light": 80,
        "watering": 3,
        "water_frequency": 3
        }
}
```

**Endpoint:** `/planty/{planty_id}`

**Method:** `PUT`

**Description:**
Updates the environmental data of a planty using its planty_id.

**Parameters:** 
- `planty_id` (UUID): Unique identifier for a planty device.

**Possible status codes:**

    200 OK: Successfully updated the data of the specified planty.
    400 Bad Request: Invalid input data.
    404 Not Found: No planty found for the provided planty_id.
    500 Internal Server Error: Server error during the operation.

**Payload:**
```json
{
    "actual_temperature": 12,
    "actual_light": 75,
    "actual_watering": 3
}
```

**Responses:**

    200 OK:
```json
{
    "id": "f60e53b4-a776-4d24-96c5-6e2164b5c9e3",
    "serie": "123abc",
    "timezone": 0,
    "actual_temperature": [
        0,
        12
    ],
    "actual_light": [
        0,
        75
    ],
    "actual_watering": [
        0,
        3
    ],
    "plants_info": {
        "id": "b4155bcf-db9e-445e-bb9c-86bbb03ec2cd",
        "scientific_name": "Plantago major",
        "station": "Indoor",
        "temperature": 22,
        "light": 80,
        "watering": 3,
        "water_frequency": 3
        }
}
```

    404: Not Found:
```json
{
    "detail": "Not Found: No Planty matches the given query."
}
```

**Endpoint:** `/planty/{planty_id}`

**Method:** `DELETE`

**Description:**
Deletes a planty specified by its planty_id.

**Parameters:** 
- `planty_id` (UUID): Unique identifier for a planty device.

**Possible status codes:**

    200 OK: Successfully deleted the specified planty.
    404 Not Found: No planty found for the provided planty_id.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    200 OK:
```json
{
    "message": "Planty deleted successfully."
}
```

    404: Not Found:
```json
{
    "detail": "Not Found: No Planty matches the given query."
}
```

</details>

<details>
<summary><b>Users Endpoints</b></summary>


**Endpoint:** `/users/{users_id}`

**Method:** `GET`

**Description:**
Fetches details of a user using its users_id.

**Parameters:** 
- `users_id` (UUID): Unique identifier for a user. 

**Possible status codes:**

    200 OK: Successfully retrieved the user's details.
    404 Not Found: No user found for the provided users_id.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    200 OK:
```json
{
    "id": "a0c1eecf-b417-4b3c-a7e0-eced4ab5e73d",
    "name": "John",
    "email": "johndoe@email.com",
    "token": null
}
```

    404 Not Found:
```json
{
    "detail": "Not Found: No Users matches the given query."
}
```

**Endpoint:** `/users`

**Method:** `POST`

**Description:**
Adds a new user.

**Parameters:** 
- `None`

**Possible status codes:**

    201 Created: Successfully added the new user.
    400 Bad Request: Invalid input data.
    500 Internal Server Error: Server error during the operation.

**Payload:**
```json
{
    "name": "string",
    "email": "string",
    "password": "string"
}
```

**Responses:**

    201 Created:
```json
{
    "id": "a0c1eecf-b417-4b3c-a7e0-eced4ab5e73d",
    "name": "John",
    "email": "johndoe@email.com",
    "token": null
}
```

**Endpoint:** `/users/login`

**Method:** `POST`

**Description:**
Allows a user to log in by validating their email and password.

**Parameters:** 
- `None`

**Possible status codes:**

    200 OK: Successfully logged in.
    400 Bad Request: Missing or invalid input data or invalid credentials.
    500 Internal Server Error: Server error during the operation.

**Payload:**
```json
{
    "name": "string",
    "email": "string",
    "password": "string"
}
```

**Responses:**

    200 OK:
```json
{
    "id": "a0c1eecf-b417-4b3c-a7e0-eced4ab5e73d",
    "name": "John",
    "email": "johndoe@email.com",
    "token": "aa68fe20-234c-432a-8c5c-522f24b741ac"
}
```

**Endpoint:** `/users/{users_id}`

**Method:** `PUT`

**Description:**
Updates a user's details using its users_id.

**Parameters:** 
- `users_id` (UUID): Unique identifier for a user. 

**Possible status codes:**

    200 OK: Successfully updated the user's information.
    400 Bad Request: Invalid input data.
    401 Unauthorized: The request is missing the necessary login-generated authentication token for this operation.
    404 Not Found: No user found for the provided users_id.
    500 Internal Server Error: Server error during the operation.

**Payload:**
```json
{
    "name": "string",
    "email": "string",
    "password": "string"
}
```

**Responses:**

    200 OK:
```json
{
    "id": "a0c1eecf-b417-4b3c-a7e0-eced4ab5e73d",
    "name": "Jane",
    "email": "johndoe@email.com",
    "token": null
}
```

    404 Not Found:
```json
{
    "detail": "Not Found: No Users matches the given query."
}
```

**Endpoint:** `/users/{users_id}`

**Method:** `DELETE`

**Description:**
Deletes a user using its users_id.

**Parameters:** 
- `users_id` (UUID): Unique identifier for a user. 

**Possible status codes:**

    200 OK: Successfully deleted the user.
    404 Not Found: No user found for the provided users_id.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    200 OK:
```json
{
    "message": "User deleted succesfully"
}
```

    404 Not Found:
```json
{
    "detail": "Not Found: No Users matches the given query."
}
```

</details>

<details>
<summary><b>Users Phone Token Endpoints</b></summary>


**Endpoint:** `/users/{users_id}/token`

**Method:** `GET`

**Description:**
Fetches all the authentication tokens for the specified user.

**Parameters:** 
- `users_id` (UUID): Unique identifier for a user.

**Possible status codes:**

    200 OK: Successfully retrieved all the tokens.
    404 Not Found: No tokens found for the provided users_id.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    200 OK:
```json
[
    {
        "id": "9a39d69a-2d7e-4b82-9f9c-b1bd2600020a",
        "user": {
            "id": "a0c1eecf-b417-4b3c-a7e0-eced4ab5e73d",
            "name": "John",
            "email": "johndoe@email.com",
            "token": null
        },
        "token": "phone_token"
    },
    ...
]
```

    404: Not Found:
```json
{
    "detail": "Not Found: No UserPhone matches the given query."
}
```

**Endpoint:** `/users/{users_id}/token/{user_phone_token}`

**Method:** `GET`

**Description:**
Retrieves the designated user's specific authentication token.

**Parameters:** 
- `users_id` (UUID): Unique identifier for a user.
- `user_phone_token` (string): Unique identifier for a userphone token.

**Possible status codes:**

    200 OK: Successfully retrieved the token.
    404 Not Found: No token found for the provided users_id.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    200 OK:
```json
{
    "id": "9a39d69a-2d7e-4b82-9f9c-b1bd2600020a",
    "user": {
        "id": "a0c1eecf-b417-4b3c-a7e0-eced4ab5e73d",
        "name": "John",
        "email": "johndoe@email.com",
        "token": null
    },
    "token": "phone_token"
}
```

    404: Not Found:
```json
{
    "detail": "Not Found: No UserPhone matches the given query."
}
```

**Endpoint:** `/users/{users_id}/token/{user_phone_token}/notifications`

**Method:** `GET`

**Description:**
Retrieves a list of all events associated with a specific user's phone token.

**Parameters:** 
- `users_id` (UUID): Unique identifier for a user.
- `user_phone_token` (string): Unique identifier for a userphone token.

**Possible status codes:**

    200 OK: Successfully retrieved the list of events.
    404 Not Found: No events found for the provided `users_id` and `user_phone_token`.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    200 OK:
```json
[
    {
        "id": "d7167893-f5aa-4ffc-84e0-adb14518734f",
        "user_phone": {
            "id": "9a39d69a-2d7e-4b82-9f9c-b1bd2600020a",
            "user": {
                "id": "a0c1eecf-b417-4b3c-a7e0-eced4ab5e73d",
                "name": "John",
                "email": "johndoe@email.com",
                "token": null
            },
            "token": "phone_token"
        },
        "last_event_date": "2023-10-12",
        "frequency": 2,
        "event_type": "TYPE_1",
        "message": "Watering plants"
    }
]
```

    404: Not Found:
```json
{
    "detail": "Not Found: No UserPhone matches the given query."
}
```

**Endpoint:** `/users/{users_id}/token/{user_phone_token}`

**Method:** `POST`

**Description:**
Generates and assigns a new authentication token for the specified user.

**Parameters:** 
- `users_id` (UUID): Unique identifier for a user.
- `user_phone_token` (string): Unique identifier for a userphone token.

**Possible status codes:**

    201 Created: Successfully generated and assigned the token.
    400 Bad Request: Unable to generate the token.
    404 Not Found: No user found for the provided `users_id` or no token found associated with the `users_id`.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    201 Created:
```json
{
    "id": "9a39d69a-2d7e-4b82-9f9c-b1bd2600020a",
    "user": {
        "id": "a0c1eecf-b417-4b3c-a7e0-eced4ab5e73d",
        "name": "John",
        "email": "johndoe@email.com",
        "token": null
    },
    "token": "phone_token"
}
```

    404: Not Found:
```json
{
    "detail": "Not Found: No UserPhone matches the given query."
}
```

**Endpoint:** `/users/{users_id}/token/{user_phone_token}/notifications`

**Method:** `POST`

**Description:**
Creates notification events based on a user and their phone token.

**Parameters:** 
- `users_id` (UUID): Unique identifier for a user.
- `user_phone_token` (string): Unique identifier for a userphone token.

**Possible status codes:**

    201 Created: Successfully generates and assigns the notification event.
    400 Bad Request: Unable to generate the notification event.
    404 Not Found: No user found for the provided `users_id` or no token found associated with the `users_id`.
    500 Internal Server Error: Server error during the operation.

**Payload:**
```json
{
    "frequency": 0,
    "event_type": "string",
    "message": "string"
}
```

**Responses:**

    201 Created:
```json
[
    {
        "id": "d7167893-f5aa-4ffc-84e0-adb14518734f",
        "user_phone": {
            "id": "9a39d69a-2d7e-4b82-9f9c-b1bd2600020a",
            "user": {
                "id": "a0c1eecf-b417-4b3c-a7e0-eced4ab5e73d",
                "name": "John",
                "email": "johndoe@email.com",
                "token": null
            },
            "token": "phone_token"
        },
        "last_event_date": "2023-10-12",
        "frequency": 2,
        "event_type": "TYPE_1",
        "message": "Watering plants"
    }
]
```

    404: Not Found:
```json
{
    "detail": "Not Found: No UserPhone matches the given query."
}
```

**Endpoint:** `/users/{users_id}/token/{user_phone_token}`

**Method:** `DELETE`

**Description:**
Revokes the authentication token for the specified user.

**Parameters:** 
- `users_id` (UUID): Unique identifier for a user.
- `user_phone_token` (string): Unique identifier for a userphone token.

**Possible status codes:**

    200 OK: Successfully revoked the token.
    404 Not Found: No user found for the provided `users_id` or no token found associated with the `users_id`.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    200 OK:
```json
{
    "message": "Token revoked successfully."
}
```

    404: Not Found:
```json
{
    "detail": "Not Found: No UserPhone matches the given query."
}
```

**Endpoint:** `/users/{users_id}/token/{user_phone_token}/notifications`

**Method:** `DELETE`

**Description:**
Deletes the events for the specified user.

**Parameters:** 
- `users_id` (UUID): Unique identifier for a user.
- `user_phone_token` (string): Unique identifier for a userphone token.

**Possible status codes:**

    200 OK: Successfully deleted the events.
    404 Not Found: No user found for the provided `users_id` or no token found associated with the `users_id`.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    200 OK:
```json
{
    "message": "Events deleted successfully."
}
```

    404: Not Found:
```json
{
    "detail": "Not Found: No UserPhone matches the given query."
}
```

</details>



## Creators:
### [Facundo Alvarez](https://www.linkedin.com/in/facundo-alvarez4/)   <a href="https://github.com/Faqu22"><img align="center" alt="github" src="https://i.imgur.com/hGwhvpO.png" height="25"/></a>


### [Gabriel Acosta](https://www.linkedin.com/in/gabriel-acosta-333g/)   <a href="https://github.com/GabiAcosta"><img align="center" alt="github" src="https://i.imgur.com/hGwhvpO.png" height="25"/></a>
