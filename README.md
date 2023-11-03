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

### Plants information endpoints

**Endpoint:** `/plants_info`

**Method:** `GET`

**Description:**
Retrieves a list of all plant information records.

**Parameters:** 
- `None` 

**Possible status codes:**

    200 OK: Successfully retrieved the list of plant information.
    500 Internal Server Error: Server error during the operation.

**Response:**

```json
[
    {
        "id": "b4155bcf-db9e-445e-bb9c-86bbb03ec2cd",
        "scientific_name": "Plantago major",
        "station": "Indoor",
        "temperature": 22,
        "light": 80,
        "watering": 3
    },
    {
        "id": "2da4e546-bc3d-4db9-84a8-1ae5ef79f4eb",
        "scientific_name": "Ficus lyrata",
        "station": "Outdoor",
        "temperature": 25,
        "light": 90,
        "watering": 2
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

**Response:**

```json
[
    {
        "id": "b4155bcf-db9e-445e-bb9c-86bbb03ec2cd",
        "scientific_name": "Plantago major",
        "station": "Indoor",
        "temperature": 22,
        "light": 80,
        "watering": 3
    }
]

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

**Response:**

    201 Created:
```json
{
    "id": "UUID",
    "message": "Plant information added successfully."
}
```





## Creators:
### [Facundo Alvarez](https://www.linkedin.com/in/facundo-alvarez4/)   <a href="https://github.com/Faqu22"><img align="center" alt="github" src="https://i.imgur.com/hGwhvpO.png" height="25"/></a>


### [Gabriel Acosta](https://www.linkedin.com/in/gabriel-acosta-333g/)   <a href="https://github.com/GabiAcosta"><img align="center" alt="github" src="https://i.imgur.com/hGwhvpO.png" height="25"/></a>
