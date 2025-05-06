# E-Commerce API Documentation

This document provides comprehensive information about the E-Commerce API endpoints, authentication, request/response formats, and best practices.

## 📑 Table of Contents
1. [Getting Started](#getting-started)
2. [Authentication](#authentication)
3. [API Endpoints](#api-endpoints)
4. [Request/Response Formats](#requestresponse-formats)
5. [Error Handling](#error-handling)
6. [Rate Limiting](#rate-limiting)
7. [Best Practices](#best-practices)

## 🚀 Getting Started

### Base URL
```
https://api.yourdomain.com/api/v1/
```

### API Versioning
The API uses URL versioning. The current version is v1.

### Response Format
All responses are in JSON format and include:
- `status`: HTTP status code
- `message`: Human-readable message
- `data`: Response data (if any)
- `errors`: Error details (if any)

Example:
```json
{
    "status": 200,
    "message": "Success",
    "data": {
        // Response data
    }
}
```

## 🔐 Authentication

The API uses JWT (JSON Web Token) authentication. All authenticated endpoints require a valid JWT token in the Authorization header.

### Obtaining Tokens

#### Register
- **POST** `/api/auth/register/`
- Register a new user account
- Request Body:
```json
{
    "username": "string",
    "email": "string",
    "password": "string",
    "password2": "string",
    "first_name": "string",
    "last_name": "string",
    "profile": {
        "phone_number": "string",
        "address": "string",
        "city": "string",
        "state": "string",
        "country": "string",
        "postal_code": "string"
    }
}
```
- Response:
```json
{
    "status": 201,
    "message": "User registered successfully",
    "data": {
        "user": {
            "id": "integer",
            "username": "string",
            "email": "string",
            "first_name": "string",
            "last_name": "string"
        },
        "tokens": {
            "access": "string",
            "refresh": "string"
        }
    }
}
```

#### Login
- **POST** `/api/auth/login/`
- Authenticate and get JWT tokens
- Request Body:
```json
{
    "email": "string",
    "password": "string"
}
```
- Response:
```json
{
    "status": 200,
    "message": "Login successful",
    "data": {
        "tokens": {
            "access": "string",
            "refresh": "string"
        }
    }
}
```

#### Refresh Token
- **POST** `/api/auth/token/refresh/`
- Get new access token using refresh token
- Request Body:
```json
{
    "refresh": "string"
}
```
- Response:
```json
{
    "status": 200,
    "message": "Token refreshed successfully",
    "data": {
        "access": "string"
    }
}
```

### Using Tokens
Include the access token in the Authorization header:
```
Authorization: Bearer <access_token>
```

## 📡 API Endpoints

### User Management

#### Profile
- **GET** `/api/profile/`
  - Get user profile
  - Requires authentication
  - Response includes user details and profile information

- **PUT/PATCH** `/api/profile/`
  - Update user profile
  - Requires authentication
  - Request Body:
```json
{
    "first_name": "string",
    "last_name": "string",
    "profile": {
        "phone_number": "string",
        "address": "string",
        "city": "string",
        "state": "string",
        "country": "string",
        "postal_code": "string"
    }
}
```

#### Password Management
- **PUT** `/api/change-password/`
  - Change user password
  - Requires authentication
  - Request Body:
```json
{
    "old_password": "string",
    "new_password": "string",
    "confirm_password": "string"
}
```

### Product Catalog

#### Categories
- **GET** `/api/catalog/categories/`
  - List all categories
  - Query Parameters:
    - `search`: Search by name
    - `ordering`: Sort by field
  - Response:
```json
{
    "status": 200,
    "data": {
        "count": "integer",
        "next": "string",
        "previous": "string",
        "results": [
            {
                "id": "integer",
                "name": "string",
                "slug": "string",
                "description": "string"
            }
        ]
    }
}
```

#### Products
- **GET** `/api/catalog/products/`
  - List all products
  - Query Parameters:
    - `category`: Filter by category
    - `search`: Search by name/description
    - `min_price`: Minimum price
    - `max_price`: Maximum price
    - `ordering`: Sort by field
  - Response:
```json
{
    "status": 200,
    "data": {
        "count": "integer",
        "next": "string",
        "previous": "string",
        "results": [
            {
                "id": "integer",
                "name": "string",
                "slug": "string",
                "description": "string",
                "price": "decimal",
                "category": {
                    "id": "integer",
                    "name": "string"
                },
                "stock": "integer",
                "available": "boolean",
                "images": [
                    {
                        "id": "integer",
                        "image": "string",
                        "is_primary": "boolean"
                    }
                ]
            }
        ]
    }
}
```

### Shopping Cart

#### Cart Operations
- **GET** `/api/cart/`
  - Get current user's cart
  - Requires authentication

- **POST** `/api/cart/items/`
  - Add item to cart
  - Requires authentication
  - Request Body:
```json
{
    "product_id": "integer",
    "quantity": "integer"
}
```

- **PUT** `/api/cart/items/<id>/`
  - Update cart item quantity
  - Requires authentication
  - Request Body:
```json
{
    "quantity": "integer"
}
```

- **DELETE** `/api/cart/items/<id>/delete/`
  - Remove item from cart
  - Requires authentication

### Orders

#### Order Management
- **GET** `/api/orders/`
  - List user's orders
  - Requires authentication
  - Query Parameters:
    - `status`: Filter by status
    - `ordering`: Sort by field

- **POST** `/api/orders/create/`
  - Create new order from cart
  - Requires authentication
  - Request Body:
```json
{
    "shipping_address": "string",
    "billing_address": "string",
    "payment_method": "string"
}
```

- **GET** `/api/orders/<id>/`
  - Get order details
  - Requires authentication

### Payments

#### Payment Operations
- **GET** `/api/payments/`
  - List user's payments
  - Requires authentication

- **POST** `/api/payments/create/`
  - Create new payment
  - Requires authentication
  - Request Body:
```json
{
    "order_id": "integer",
    "payment_method": "string",
    "amount": "decimal"
}
```

## 📄 Pagination

All list endpoints support pagination with the following parameters:

- `page`: Page number (default: 1)
- `page_size`: Items per page (default: 10, max: 100)

Response format:
```json
{
    "status": 200,
    "data": {
        "count": 100,
        "next": "https://api.example.com/endpoint?page=2",
        "previous": null,
        "results": []
    }
}
```

## 🔄 Caching

The API implements caching for better performance:

- **Response Caching**
  - Cache-Control headers
  - ETag support
  - Last-Modified headers

- **Cache Headers**
```
Cache-Control: public, max-age=3600
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
Last-Modified: Wed, 21 Oct 2015 07:28:00 GMT
```

## 🔍 Search and Filtering

### Advanced Search

All list endpoints support advanced search with the following operators:

- `exact`: Exact match
- `contains`: Contains text
- `startswith`: Starts with
- `endswith`: Ends with
- `gt`: Greater than
- `lt`: Less than
- `gte`: Greater than or equal
- `lte`: Less than or equal

Example:
```
/api/products/?price__gt=100&name__contains=shirt
```

### Filtering

Common filter parameters:

- **Products**
  - `category`: Filter by category
  - `price_range`: Filter by price range
  - `in_stock`: Filter by stock status
  - `rating`: Filter by rating

- **Orders**
  - `status`: Filter by order status
  - `date_range`: Filter by date range
  - `payment_status`: Filter by payment status

## 📊 Analytics Endpoints

### Sales Analytics
- **GET** `/api/analytics/sales/`
  - Get sales statistics
  - Query Parameters:
    - `start_date`: Start date
    - `end_date`: End date
    - `group_by`: Group by (day/week/month)
  - Response:
```json
{
    "status": 200,
    "data": {
        "total_sales": "decimal",
        "total_orders": "integer",
        "average_order_value": "decimal",
        "sales_by_period": [
            {
                "period": "string",
                "sales": "decimal",
                "orders": "integer"
            }
        ]
    }
}
```

### Product Analytics
- **GET** `/api/analytics/products/`
  - Get product performance metrics
  - Query Parameters:
    - `category`: Filter by category
    - `time_range`: Time range
  - Response:
```json
{
    "status": 200,
    "data": {
        "top_products": [
            {
                "product_id": "integer",
                "name": "string",
                "sales": "decimal",
                "orders": "integer"
            }
        ],
        "category_performance": [
            {
                "category": "string",
                "sales": "decimal",
                "orders": "integer"
            }
        ]
    }
}
```

## 🔔 Webhooks

The API supports webhooks for real-time notifications:

### Available Events
- `order.created`
- `order.updated`
- `order.completed`
- `payment.succeeded`
- `payment.failed`
- `product.stock_updated`

### Webhook Configuration
- **POST** `/api/webhooks/`
  - Register a new webhook
  - Request Body:
```json
{
    "url": "string",
    "events": ["string"],
    "secret": "string"
}
```

### Webhook Payload
```json
{
    "event": "string",
    "timestamp": "datetime",
    "data": {
        // Event-specific data
    },
    "signature": "string"
}
```

## 🔐 API Keys

For third-party integrations, the API supports API key authentication:

### Generate API Key
- **POST** `/api/keys/`
  - Generate new API key
  - Requires authentication
  - Response:
```json
{
    "status": 201,
    "data": {
        "key": "string",
        "created_at": "datetime",
        "expires_at": "datetime"
    }
}
```

### Using API Keys
Include the API key in the X-API-Key header:
```
X-API-Key: your-api-key
```

## 📈 Rate Limiting

Detailed rate limits by endpoint:

| Endpoint | Authenticated | Unauthenticated |
|----------|--------------|-----------------|
| `/api/auth/*` | 100/min | 20/min |
| `/api/products/*` | 1000/min | 100/min |
| `/api/orders/*` | 500/min | 50/min |
| `/api/analytics/*` | 100/min | 10/min |

Rate limit headers:
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1612345678
```

## 🔄 API Versioning

The API uses URL versioning:
- Current version: v1
- Base URL: `https://api.example.com/api/v1/`

Version deprecation policy:
- Versions are supported for 12 months after deprecation
- Deprecation notices are sent 6 months in advance
- Breaking changes are only introduced in new major versions

## 📚 SDK Support

Official SDKs are available for:
- Python
- JavaScript/TypeScript
- PHP
- Ruby
- Java

Example usage (Python):
```python
from ecommerce_sdk import EcommerceClient

client = EcommerceClient(api_key='your-api-key')
products = client.products.list(category='electronics')
```

## 🛠️ Developer Tools

- **API Playground**: `/api/docs/playground/`
- **API Status**: `/api/status/`
- **API Health**: `/api/health/`
- **API Metrics**: `/api/metrics/`

## ⚠️ Error Handling

The API uses standard HTTP status codes and returns error details in the response body:

```json
{
    "status": "integer",
    "message": "string",
    "errors": {
        "field_name": [
            "error message"
        ]
    }
}
```

Common status codes:
- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 429: Too Many Requests
- 500: Internal Server Error

## 🚦 Rate Limiting

The API implements rate limiting to ensure fair usage:
- 100 requests per minute for authenticated users
- 20 requests per minute for unauthenticated users

Rate limit headers:
- `X-RateLimit-Limit`: Maximum requests per window
- `X-RateLimit-Remaining`: Remaining requests in current window
- `X-RateLimit-Reset`: Time when the rate limit resets

## 💡 Best Practices

1. **Authentication**
   - Always use HTTPS
   - Store tokens securely
   - Refresh tokens before they expire
   - Never share tokens

2. **Requests**
   - Use appropriate HTTP methods
   - Include required headers
   - Validate request data
   - Handle rate limits

3. **Responses**
   - Check status codes
   - Handle errors gracefully
   - Cache responses when appropriate
   - Implement retry logic for failed requests

4. **Security**
   - Keep tokens secure
   - Use strong passwords
   - Enable 2FA when available
   - Report security issues

## 📚 Additional Resources

- [API Changelog](CHANGELOG.md)
- [SDK Documentation](SDK.md)
- [Integration Guides](INTEGRATION.md)
- [FAQ](FAQ.md) 