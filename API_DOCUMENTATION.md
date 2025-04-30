# E-Commerce API Documentation

This document provides comprehensive information about the E-Commerce API endpoints, authentication, and usage.

## Table of Contents
1. [Authentication](#authentication)
2. [API Endpoints](#api-endpoints)
   - [Products](#products)
   - [Accounts](#accounts)
   - [Orders](#orders)
   - [Payments](#payments)
   - [Cart](#cart)
3. [Documentation Access](#documentation-access)
4. [Error Handling](#error-handling)

## Authentication

The API uses JWT (JSON Web Token) authentication. To authenticate your requests:

1. Obtain a token by sending a POST request to `/api/accounts/token/` with your credentials:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```

2. Include the token in subsequent requests in the Authorization header:
```
Authorization: Bearer <your_token>
```

## API Endpoints

### Products

#### List Products
- **GET** `/api/products/`
- Returns a list of all products
- Query parameters:
  - `category`: Filter by category
  - `search`: Search by product name or description
  - `min_price`: Minimum price
  - `max_price`: Maximum price

#### Product Detail
- **GET** `/api/products/<id>/`
- Returns detailed information about a specific product

### Accounts

#### User Registration
- **POST** `/api/accounts/register/`
- Register a new user
- Required fields:
  - `username`
  - `email`
  - `password`
  - `first_name`
  - `last_name`

#### User Profile
- **GET** `/api/accounts/profile/`
- Returns the authenticated user's profile information
- Requires authentication

### Orders

#### Create Order
- **POST** `/api/orders/`
- Create a new order
- Requires authentication
- Required fields:
  - `items`: List of product IDs and quantities
  - `shipping_address`: Shipping address details

#### Order History
- **GET** `/api/orders/`
- Returns the authenticated user's order history
- Requires authentication

### Payments

#### Process Payment
- **POST** `/api/payments/`
- Process a payment for an order
- Requires authentication
- Required fields:
  - `order_id`
  - `payment_method`
  - `payment_details`

### Cart

#### View Cart
- **GET** `/api/cart/`
- Returns the current user's cart
- Requires authentication

#### Add to Cart
- **POST** `/api/cart/add/`
- Add a product to the cart
- Requires authentication
- Required fields:
  - `product_id`
  - `quantity`

## Documentation Access

The API documentation is available in multiple formats:

1. **Swagger UI**: `/api/docs/swagger/`
   - Interactive API documentation
   - Test endpoints directly from the browser

2. **ReDoc**: `/api/docs/redoc/`
   - Alternative documentation view
   - More readable format

3. **OpenAPI JSON**: `/api/docs/json/`
   - Raw OpenAPI specification
   - For programmatic use

## Error Handling

The API uses standard HTTP status codes and returns error messages in the following format:

```json
{
    "error": "Error message",
    "status": "error",
    "code": "error_code"
}
```

Common error codes:
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error

## Rate Limiting

API requests are rate-limited to prevent abuse:
- 100 requests per minute for authenticated users
- 20 requests per minute for unauthenticated users

## Support

For support or questions about the API, please contact:
- Email: support@ecommerce.com
- Documentation: [API Documentation](http://your-domain/api/docs/swagger/) 