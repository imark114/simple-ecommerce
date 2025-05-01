# E-Commerce Platform

A modern e-commerce platform built with Django and Django REST Framework, featuring a robust API, JWT authentication, and an admin interface powered by Unfold.

## Features

- **User Management**
  - Custom user model with email/username login
  - JWT authentication
  - User profiles with address management

- **Product Management**
  - Product categories
  - Product images with primary image support
  - Stock management
  - Product availability tracking

- **Shopping Experience**
  - Shopping cart functionality
  - Order management
  - Payment processing
  - Order status tracking

- **Admin Interface**
  - Modern Unfold admin theme
  - Comprehensive product management
  - Order and payment tracking
  - User management

## Project Structure

```
e-commerce/
├── accounts/           # User authentication and profiles
├── cart/              # Shopping cart functionality
├── orders/            # Order processing and management
├── payments/          # Payment processing
├── products/          # Product and category management
└── ecommerce/         # Project configuration
```

## API Documentation

### Authentication

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/auth/register/` | POST | Register a new user |
| `/api/auth/login/` | POST | Login and get JWT tokens |
| `/api/auth/refresh/` | POST | Refresh JWT token |

### Catalog

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/catalog/categories/` | GET | List all categories |
| `/api/catalog/categories/<id>/` | GET | Get category details |
| `/api/catalog/products/` | GET | List all products |
| `/api/catalog/products/<id>/` | GET | Get product details |

### Shopping Cart

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/shopping-cart/` | GET | Get cart details |
| `/api/shopping-cart/items/` | POST | Add item to cart |
| `/api/shopping-cart/items/<id>/` | PUT | Update cart item |
| `/api/shopping-cart/items/<id>/remove/` | DELETE | Remove item from cart |

### Orders

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/orders/` | GET | List user's orders |
| `/api/orders/<id>/` | GET | Get order details |
| `/api/orders/create/` | POST | Create a new order |
| `/api/orders/<id>/update/` | PUT | Update order status |

### Payments

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/payments/` | GET | List user's payments |
| `/api/payments/create/` | POST | Create a new payment |
| `/api/payments/<id>/` | GET | Get payment details |

## Setup and Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd e-commerce
```

2. Create and activate a virtual environment:
```bash
python -m venv my_venv
source my_venv/bin/activate  # On Windows: my_venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Dependencies

- Django 5.2
- Django REST Framework 3.16.0
- Django REST Framework SimpleJWT 5.5.0
- Django Filter 25.1
- Pillow 11.2.1
- PyJWT 2.9.0
- Python-dotenv 1.0.1
- Django Unfold 0.8.0
- DRF Yasg 1.21.7

## API Documentation

The API documentation is available at:
- Swagger UI: `/api/docs/swagger/`
- ReDoc: `/api/docs/redoc/`
- JSON Schema: `/api/docs/json/`

## Admin Interface

Access the admin interface at `/admin/` using your superuser credentials.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
