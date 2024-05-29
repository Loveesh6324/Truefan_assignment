# Product Inventory API

This project is a Django-based RESTful API for managing a product inventory. It includes CRUD operations for products and is dockerized for easy deployment.

## Features

- Retrieve a list of all products.
- Retrieve details of a single product by ID.
- Create a new product.
- Update an existing product by ID.
- Delete a product by ID.

## Requirements

- Python
- Django 
- Django REST Framework
- Docker

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/product_inventory.git
   cd product_inventory
   
2. **Create a virtual environment**
   
    ```bash
    virtualenv .env
    source .env/bin/activate

3. **Install the dependencies**
   
    ```bash
     pip install -r requirements.txt

4. **Apply the migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
   
5. **Run the development server**

    ```bash
    python manage.py runserver
    Access the API:

Open your browser and navigate to http://localhost:8000/api/products/



## Docker Setup
To run the project in a Docker container, follow these steps:

1. **Build the Docker image**

   ```bash
   docker-compose build
   
2. **Run the Docker container**

   ```bash
   docker-compose up

## Access the API:

Open your browser and navigate to http://localhost:8000/api/products/

