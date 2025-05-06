# E-Commerce Platform

A modern, scalable e-commerce platform built with Django and Django REST Framework. This platform provides a robust API, secure JWT authentication, and an intuitive admin interface powered by Unfold.

## 🚀 Features

### User Management
- **Authentication & Authorization**
  - Custom user model with email/username login
  - JWT-based authentication with refresh tokens
  - Role-based access control (Admin, Staff, Customer)
  - Secure password management with validation

- **Profile Management**
  - Comprehensive user profiles
  - Address management (shipping/billing)
  - Profile customization
  - Account settings

### Product Management
- **Catalog System**
  - Hierarchical category management
  - Rich product information
  - Multiple product images with primary image support
  - Stock tracking and inventory management
  - Product availability status

- **Search & Filtering**
  - Advanced search functionality
  - Category-based filtering
  - Price range filtering
  - Sorting options

### Shopping Experience
- **Cart System**
  - Persistent shopping cart
  - Real-time price calculations
  - Quantity management
  - Cart item validation

- **Order Processing**
  - Multi-step checkout process
  - Order status tracking
  - Order history
  - Invoice generation

- **Payment Integration**
  - Secure payment processing
  - Multiple payment methods
  - Transaction history
  - Payment status tracking

### Admin Dashboard
- **Modern Interface**
  - Unfold-powered admin theme
  - Responsive design
  - Intuitive navigation
  - Real-time statistics

- **Management Tools**
  - Product catalog management
  - Order processing
  - User management
  - Payment tracking
  - Inventory control

## 🏗️ Project Structure

```
e-commerce/
├── accounts/           # User authentication and profiles
│   ├── models.py      # Custom user model
│   ├── views.py       # Authentication views
│   └── urls.py        # Auth endpoints
├── cart/              # Shopping cart functionality
│   ├── models.py      # Cart models
│   ├── views.py       # Cart operations
│   └── urls.py        # Cart endpoints
├── orders/            # Order processing
│   ├── models.py      # Order models
│   ├── views.py       # Order management
│   └── urls.py        # Order endpoints
├── payments/          # Payment processing
│   ├── models.py      # Payment models
│   ├── views.py       # Payment operations
│   └── urls.py        # Payment endpoints
├── products/          # Product management
│   ├── models.py      # Product models
│   ├── views.py       # Product operations
│   └── urls.py        # Product endpoints
└── ecommerce/         # Project configuration
    ├── settings.py    # Project settings
    ├── urls.py        # Main URL routing
    └── wsgi.py        # WSGI configuration
```

## 🛠️ Setup and Installation

1. **Clone the Repository**
```bash
git clone <repository-url>
cd e-commerce
```

2. **Set Up Virtual Environment**
```bash
python -m venv my_venv
source my_venv/bin/activate  # On Windows: my_venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Environment Variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Database Setup**
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. **Run Development Server**
```bash
python manage.py runserver
```

## 📚 API Documentation

The API documentation is available in multiple formats:
- **Swagger UI**: `/api/docs/swagger/`
- **ReDoc**: `/api/docs/redoc/`
- **JSON Schema**: `/api/docs/json/`

For detailed API documentation, see [API_DOCUMENTATION.md](API_DOCUMENTATION.md)

## 🛡️ Security Features

- JWT-based authentication
- Password hashing and validation
- CSRF protection
- XSS prevention
- Rate limiting
- Input validation
- Secure headers

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

## 📦 Dependencies

- Django 5.2
- Django REST Framework 3.16.0
- Django REST Framework SimpleJWT 5.5.0
- Django Filter 25.1
- Pillow 11.2.1
- PyJWT 2.9.0
- Python-dotenv 1.0.1
- Django Unfold 0.8.0
- DRF Yasg 1.21.7

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- Django REST Framework
- Unfold Admin Theme
- All contributors and supporters
