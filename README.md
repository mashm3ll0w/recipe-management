# Recipe Management System App

## Table Of Contents

- [Recipe Management System App](#recipe-management-system-app)
  - [Table Of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Local Server Setup](#local-server-setup)
    - [Clone The Repository](#clone-the-repository)
    - [Install Dependencies](#install-dependencies)
    - [Make database migrations](#make-database-migrations)
    - [Run the Server](#run-the-server)
  - [**EndPoints**](#endpoints)
  - [Authors](#authors)
  - [License](#license)

## Introduction

Welcome to the Recipe Management System App! This document provides detailed information on setting up the server locally and the API endpoints.

Django Ninja was used as it is more efficient and faster than Plain Django, Django REST-framework and Flask as shown by this [benchmark](https://github.com/vitalik/django-ninja-benchmarks) results.

---

## Local Server Setup

### Clone The Repository

To get started with the local development environment, clone the repository:

```bash
$ git clone https://github.com/mashm3ll0w/recipe-management.git
$ cd recipe-management
```

### Install Dependencies

Set up the environment using `venv`:

```bash
# create Virtual Environment
$ python3 -m venv venv

# Activate Virtual Env
$ source venv/bin/activate

# Install Dependencies
$ pip install -r requirements.txt
```


### Make database migrations

```bash
$ python3 manage.py makemigrations

$ python3 manage.py migrate
```


### Run the Server

```bash
$ python3 manage.py runserver
```

## **EndPoints**

The documentation for the api is made using [Swagger UI](https://swagger.io/tools/swagger-ui/) and can be found at `127:0.0.1:8000/api/docs`


## Authors

- [@Charles Swaleh](https://github.com/mashm3ll0w)

## License

MIT License
