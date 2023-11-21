# Planty-backend
This Django backend service provides a RESTful API to manage various data models including plants, devices, users among others and an notification system. The API serves as a central platform to handle operations related to these entities, offering endpoints for creation, retrieval, modification, and deletion of model instances.
## Index

- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Notifications API](#notifications-api)
     - [Overview](#overview)
     - [Setup](#setup)
         - [Docker Compose](#docker-compose)
         - [Django Settings](#django-settings)
         - [Celery Configuration](#celery-configuration)
     - [Usage](#usage)
         - [Tasks Management](#tasks-management)
         - [Notification Functions](#notification-functions)
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



## API Endpoints

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


<details>
<summary><b>Planty of Users Endpoints</b></summary>


**Endpoint:** `/users_planty/{users_id}`

**Method:** `GET`

**Description:**
Retrieves a list of all the planty devices linked to the specified user.

**Parameters:** 
- `users_id` (UUID): Unique identifier for a user.

**Possible status codes:**

    200 OK: Successfully retrieved the list of devices linked to the user.
    404 Not Found: No planty devices found for the provided `users_id`.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    200 OK:
```json
[
    {
        "id": "b87f4a57-17a0-44c2-a58b-894241512091",
        "plant_name": "Dante",
        "image_url": "firebase_url_image",
        "location": "Kitchen",
        "color_card": "#38CE61",
        "user": {
            "id": "a0c1eecf-b417-4b3c-a7e0-eced4ab5e73d",
            "name": "John",
            "email": "johndoe@email.com",
            "token": null
        },
        "planty": {
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
    },
    ...
]
```

    404: Not Found:
```json
{
    "detail": "Not Found: No Users_planty matches the given query."
}
```

**Endpoint:** `/users_planty/{users_id}/planty/{planty_id}`

**Method:** `GET`

**Description:**
Retrieves details of a specific planty device linked to a user.

**Parameters:** 
- `users_id` (UUID): Unique identifier for a user.
- `planty_id` (UUID): Unique identifier for a planty device.

**Possible status codes:**

    200 OK: Successfully retrieved the details of the specified planty device linked to the user.
    404 Not Found: No planty device found for the provided `users_id` and `planty_id`.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    200 OK:
```json
{
    "id": "b87f4a57-17a0-44c2-a58b-894241512091",
    "plant_name": "Dante",
    "image_url": "firebase_url_image",
    "location": "Kitchen",
    "color_card": "#38CE61",
    "user": {
        "id": "a0c1eecf-b417-4b3c-a7e0-eced4ab5e73d",
        "name": "John",
        "email": "johndoe@email.com",
        "token": null
    },
    "planty": {
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
}
```

    404: Not Found:
```json
{
    "detail": "Not Found: No Users_planty matches the given query."
}
```

**Endpoint:** `/users_planty/{users_id}/planty/{planty_id}`

**Method:** `POST`

**Description:**
Creates a new relationship between a user and a planty device with specified details.

**Parameters:** 
- `users_id` (UUID): Unique identifier for a user.
- `planty_id` (UUID): Unique identifier for a planty device.

**Possible status codes:**

    201 Created: Successfully created the relationship and retrieved details of the specified planty device linked to the user.
    400 Bad Request: Invalid input data.
    404 Not Found: No planty device or user found for the provided `users_id` or `planty_id`.
    500 Internal Server Error: Server error during the operation.

**Payload:**
```json
{
    "token_phone": "string",
    "user_planty": {
        "plant_name": "string",
        "color_card": "string",
        "location": "string",
        "image_url": "string"
    },
    "plants_info_id": "string",
    "timezone": 0,
    "phone_event": [
        {
            "frequency": 0,
            "event_type": "string",
            "message": "string"
        }
    ]
}
```

**Responses:**

    201 Created:
```json
{
    "user_planty": {
        "id": "b87f4a57-17a0-44c2-a58b-894241512091",
        "plant_name": "Dante",
        "image_url": "firebase_url_image",
        "location": "Kitchen",
        "color_card": "#38CE61",
        "user": {
            "id": "a0c1eecf-b417-4b3c-a7e0-eced4ab5e73d",
            "name": "John",
            "email": "johndoe@email.com",
            "token": null
        },
        "planty": {
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
    },
    "phone_events": [
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
}
```

    404: Not Found:
```json
{
    "detail": "Not Found: No UserPhone matches the given query."
}
```

**Endpoint:** `/users_planty/{user_planty_id}`

**Method:** `PUT`

**Description:**
Updates the details of a user-planty relationship with the specified ID.

**Parameters:** 
- `user_planty_id` (UUID): Unique identifier for a user-planty relationship.

**Possible status codes:**

    200 OK: Successfully updated the details of the specified user-planty relationship and retrieved the updated information.
    400 Bad Request: Invalid input data.
    404 Not Found: No user-planty relationship found for the provided `user_planty_id`.
    500 Internal Server Error: Server error during the operation.

**Payload:**
```json
{
    "token_phone": "string",
    "user_planty": {
        "plant_name": "string",
        "color_card": "string",
        "location": "string",
        "image_url": "string"
    },
    "plants_info_id": "string",
    "timezone": 0,
    "phone_event": [
        {
            "frequency": 0,
            "event_type": "string",
            "message": "string"
        }
    ]
}
```

**Responses:**

    200 OK:
```json
{
    "id": "b87f4a57-17a0-44c2-a58b-894241512091",
    "plant_name": "Maripili",
    "image_url": "firebase_url_image",
    "location": "Living Room",
    "color_card": "#2f31a3",
    "user": {
        "id": "a0c1eecf-b417-4b3c-a7e0-eced4ab5e73d",
        "name": "John",
        "email": "johndoe@email.com",
        "token": null
    },
    "planty": {
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
}
```

    404: Not Found:
```json
{
    "detail": "Not Found: No Users_planty matches the given query."
}
```

**Endpoint:** `/users_planty/{user_planty_id}`

**Method:** `DELETE`

**Description:**
Deletes a user-planty relationship with the specified ID.

**Parameters:** 
- `user_planty_id` (UUID): Unique identifier for a user-planty relationship.

**Possible status codes:**

    200 OK: Successfully deleted the specified user-planty relationship.
    400 Bad Request: Invalid input data.
    404 Not Found: No user-planty relationship found for the provided `user_planty_id`.
    500 Internal Server Error: Server error during the operation.

**Responses:**

    200 OK:
```json
{
    "message": "Deleted sucesfully"
}
```

    404: Not Found:
```json
{
    "detail": "Not Found: No Users_planty matches the given query."
}
```


</details>

# Notifications API

## Overview

This repository houses a Django Ninja backend microservice for the Planty application, focusing on managing notifications related to plant care. The microservice incorporates Celery for task scheduling, Redis as a message broker, and integrates with Expo services for mobile notifications.

## Setup

### Docker Compose

Use Docker Compose to orchestrate the deployment of the microservice and its dependencies. The `docker-compose.yml` file defines services for the backend (`planty_be`), Celery worker (`worker`), Celery beat (`beat`), and Redis (`redis`).

```yaml
# Docker Compose snippet (details omitted for brevity)
services:
  planty_be:
    image: ${GHCR_IMAGE}
    container_name: planty_be
    command: bash -c "python manage.py makemigrations Users && python manage.py makemigrations Plants && python manage.py makemigrations Devices && python manage.py makemigrations User_devices &&  python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8080"
    ports:
      - "8080:8080"
    networks:
      - plantynet

  worker:
    image: ${GHCR_IMAGE}
    container_name: planty_wr
    command: celery -A config worker --loglevel=info
    depends_on:
      - redis
    networks:
      - plantynet

  beat:
    image: ${GHCR_IMAGE}
    container_name: planty_bt
    command: celery -A config beat --loglevel=info
    depends_on:
      - redis
    networks:
      - plantynet

  redis:
    image: redis:latest
    container_name: redis
    depends_on:
      - planty_be
    networks:
      - plantynet
```

### Django Settings

Configure Django settings in settings.py to enable Celery for task management. Specify the Celery broker and result backend, along with scheduling details for periodic tasks.

```py
# Django settings snippet (details omitted for brevity)
CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

CELERY_BEAT_SCHEDULE = {
    'manage_notifications': {
        'task': 'manage_notifications',
        'schedule': timedelta(days=1), 
    },
    "manage_status_plants": {
        "task": "manage_status_plants",
        "schedule": timedelta(hours=4)
    }
}
```

### Celery Configuration

In celery.py, configure Celery and discover tasks in separate modules.

```py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
```

## Usage
### Tasks Management

#### manage_notifications
This task handles Watering Reminder notifications. It checks if the last notification date plus the frequency equals today's date and sends notifications accordingly.
```py
@app.task(name="manage_notifications")
def manage_notifications():
    responses = []
    watering_notifications = get_phoneEvent_model().objects.filter(event_type__icontains="Watering Reminder")
    for notification in watering_notifications:
        if (notification.last_event_date + timedelta(days=notification.frequency - 1)) == datetime.today().date():
            notification_dict = model_to_dict(notification)
            status = send_notifications(expo_token=notification.user_phone.token, title=notification.event_type, body=notification.message)
            responses.append({"event": notification_dict, "response": status["data"]})
            if status == 200:
                notification.last_event_date = notification.last_event_date + timedelta(days=notification.frequency).date()
                notification.save()
    return responses
```

#### manage_status_plants
This task manages Temperature, Light, and Humidity alerts. It filters notifications based on alert type and user-defined thresholds. The function then calls handle_sensors_alert to send notifications.

```py
@app.task(name="manage_status_plants")
def manage_status_plants():
    responses = []

    alerts = [
        {"type": "temperature", "threshold_high": 6, "threshold_low": 8, "event_type": "Temperature Alert"},
        {"type": "light", "threshold_high": 30, "threshold_low": 30, "event_type": "Light Alert"},
        {"type": "humidity", "threshold_high": 30, "threshold_low": 30, "event_type": "Humidity Alert"},
    ]

    for alert in alerts:
        notifications = get_phoneEvent_model().objects.filter(event_type__icontains=alert["event_type"])
        for notification in notifications:
            try:
                current_time = datetime.now(pytz.timezone(f"Etc/GMT{notification.user_device.planty.timezone}"))
                if 6 <= current_time.hour < 22:
                    responses.extend(handle_sensors_alert(notification, **alert))
            except Exception as e:
                pass

    return responses
```

#### handle_sensors_alert
This function handles specific sensor alerts based on the type of sensor (Temperature, Humidity, or Light). It compares sensor values with plant values and sends notifications if conditions are outside the recommended range.

```py
def handle_sensors_alert(notification, type, threshold_high, threshold_low, event_type):
    user_device = notification.user_device
    sensors_dict = {
        "temperature": {"sensor_value": user_device.planty.actual_temperature[-1],
                        "plant_value": user_device.planty.plants_info.temperature,
                        "title": f'Temperature Alert - {user_device.plant_name}'},
        "humidity": {"sensor_value": user_device.planty.actual_watering[-1],
                     "plant_value": user_device.planty.plants_info.watering,
                     "title": f'Humidity Alert - {user_device.plant_name}'},
        "light": {"sensor_value": user_device.planty.actual_light[-1],
                  "plant_value": user_device.planty.plants_info.light,
                  "title": f'Light Alert - {user_device.plant_name}'},
    }

    response = {}
    if sensors_dict[type]["sensor_value"] + threshold_high < sensors_dict[type]["plant_value"]:
        response = send_notification(sensors_dict[type]["title"], f'Your plant {user_device.plant_name} might be feeling {event_type.lower()}.', get_list_or_404(get_userPhone_model(), user_id=notification.user_device.user.id))
    elif sensors_dict[type]["sensor_value"] - threshold_low > sensors_dict[type]["plant_value"]:
        response = send_notification(sensors_dict[type]["title"], f'To keep your plant {user_device.plant_name} happy and healthy, adjust the {event_type.lower()} conditions.', get_list_or_404(get_userPhone_model(), user_id=notification.user_device.user.id))

    return response
```

### Notification Functions

#### send_notification
Sends a notification to a list of user devices using Expo services. It receives a title, body, and a list of tokens.

```py
def send_notification(title, body, tokens):
    responses = []
    for token in tokens:
        status = send_notifications(expo_token=token.token, title=title, body=body)
        responses.append({"to": token.user.email, "token": token.token, "body": title, "response": status["data"]["status"]})
    return responses
```

#### send_notifications
Sends notifications to user devices using Expo services. It receives an Expo token, title, and body and returns the response from the Expo service.

```py
def send_notifications(expo_token: str, title: str, body: str):
    url = "https://exp.host/--/api/v2/push/send"
    headers = {
        "host": "exp.host",
        "accept": "application/json",
        "accept-encoding": "gzip, deflate",
        "content-type": "application/json"
    }
    data = {
        "to": expo_token,
        "sound": "default",
        "title": title,
        "body": body
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()
```

## Creators:
### [Facundo Alvarez](https://www.linkedin.com/in/facundo-alvarez4/)   <a href="https://github.com/Faqu22"><img align="center" alt="github" src="https://i.imgur.com/hGwhvpO.png" height="25"/></a>


### [Gabriel Acosta](https://www.linkedin.com/in/gabriel-acosta-333g/)   <a href="https://github.com/GabiAcosta"><img align="center" alt="github" src="https://i.imgur.com/hGwhvpO.png" height="25"/></a>
