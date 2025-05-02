# E-Commerce API Documentation

This document provides comprehensive information about the E-Commerce API endpoints, authentication, and usage.

## Table of Contents
1. [Authentication](#authentication)
2. [API Endpoints](#api-endpoints)
   - [Auth](#auth)
   - [Profile](#profile)
   - [Catalog](#catalog)
   - [Cart](#cart)
   - [Orders](#orders)
   - [Payments](#payments)
3. [Documentation Access](#documentation-access)
4. [Error Handling](#error-handling)

## Authentication

The API uses JWT (JSON Web Token) authentication. To authenticate your requests:

1. Obtain a token by sending a POST request to `/api/accounts/auth/login/` with your credentials:
```json
{
    "email": "your_email",
    "password": "your_password"
}
```

2. Include the token in subsequent requests in the Authorization header:
```
Authorization: Bearer <your_token>
```

3. Refresh your token when it expires by sending a POST request to `/api/accounts/auth/token/refresh/`:
```json
{
    "refresh": "your_refresh_token"
}
```

## API Endpoints

### Auth

#### Register
- **POST** `/api/accounts/auth/register/`
- Register a new user
- Required fields:
  - `username`
  - `email`
  - `password`
  - `password2` (confirm password)
  - `first_name`
  - `last_name`
  - Optional: `profile` object with:
    - `phone_number`
    - `address`
    - `city`
    - `state`
    - `country`
    - `postal_code`

#### Login
- **POST** `/api/accounts/auth/login/`
- Login and get JWT tokens
- Required fields:
  - `email`
  - `password`

#### Refresh Token
- **POST** `/api/accounts/auth/token/refresh/`
- Refresh JWT token
- Required fields:
  - `refresh`

### Profile

#### View Profile
- **GET** `/api/accounts/profile/`
- Returns the authenticated user's profile information
- Requires authentication
- Response includes user details and profile information

#### Update Profile
- **PUT/PATCH** `/api/accounts/profile/`
- Update user profile information
- Requires authentication
- Can update:
  - `first_name`
  - `last_name`
  - `profile` object with:
    - `phone_number`
    - `address`
    - `city`
    - `state`
    - `country`
    - `postal_code`

#### Change Password
- **PUT** `/api/accounts/change-password/`
- Change user password
- Requires authentication
- Required fields:
  - `old_password`: Current password
  - `new_password`: New password
  - `confirm_password`: Confirm new password
- Response:
```json
{
    "message": "Password updated successfully"
}
```

### Catalog

#### List Categories
- **GET** `/api/catalog/categories/`
- Returns a list of all categories
- Query parameters:
  - `search`: Search by category name

#### Category Detail
- **GET** `/api/catalog/categories/<id>/`
- Returns detailed information about a specific category

#### List Products
- **GET** `/api/catalog/products/`
- Returns a list of all products
- Query parameters:
  - `category`: Filter by category
  - `search`: Search by product name or description
  - `min_price`: Minimum price
  - `max_price`: Maximum price

#### Product Detail
- **GET** `/api/catalog/products/<id>/`
- Returns detailed information about a specific product

### Cart

#### View Cart
- **GET** `/api/cart/`
- Returns the current user's cart
- Requires authentication
- Response:
```json
{
    "id": 1,
    "user": 1,
    "items": [
        {
            "id": 1,
            "product": {
                "id": 1,
                "name": "Product Name",
                "price": "99.99"
            },
            "quantity": 2,
            "total_price": "199.98"
        }
    ],
    "total_price": "199.98",
    "created_at": "2025-05-02T16:22:07Z",
    "updated_at": "2025-05-02T16:22:07Z"
}
```

#### View User's Cart (Admin Only)
- **GET** `/api/cart/user/<user_id>/`
- Returns a specific user's cart
- Requires admin authentication
- Response: Same as above
- Error responses:
  - 404: User not found
  - 403: Forbidden (non-admin access)

#### Add to Cart
- **POST** `/api/cart/items/`
- Add a product to the cart
- Requires authentication
- Required fields:
  - `product_id`
  - `quantity`

#### Update Cart Item
- **PUT** `/api/cart/items/<id>/`
- Update cart item quantity
- Requires authentication

#### Delete Cart Item
- **DELETE** `/api/cart/items/<id>/delete/`
- Remove item from cart
- Requires authentication

### Orders

#### List Orders
- **GET** `/api/orders/`
- Returns the current user's orders
- Requires authentication
- Response:
```json
[
    {
        "id": 1,
        "user": 1,
        "status": "pending",
        "total_price": "199.98",
        "shipping_address": "123 Main St",
        "billing_address": "123 Main St",
        "payment_status": false,
        "items": [
            {
                "id": 1,
                "product": {
                    "id": 1,
                    "name": "Product Name",
                    "price": "99.99"
                },
                "quantity": 2,
                "price": "99.99",
                "total_price": "199.98"
            }
        ],
        "created_at": "2025-05-02T16:22:07Z",
        "updated_at": "2025-05-02T16:22:07Z"
    }
]
```

#### View User's Orders (Admin Only)
- **GET** `/api/orders/user/<user_id>/`
- Returns all orders for a specific user
- Requires admin authentication
- Response: Same as above
- Error responses:
  - 404: User not found
  - 403: Forbidden (non-admin access)

#### Create Order
- **POST** `/api/orders/create/`
- Create a new order from cart
- Requires authentication
- Required fields:
  - `shipping_address`
  - `billing_address`

#### Update Order
- **PUT** `/api/orders/<id>/update/`
- Update order status
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
  - Password fields don't match
  - Invalid old password
  - Required fields missing
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