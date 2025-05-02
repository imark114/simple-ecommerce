from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="E-commerce API",
        default_version='v1',
        description="""
        This is the API documentation for the E-Commerce platform.
        
        ## Authentication
        The API uses JWT (JSON Web Token) authentication. To authenticate your requests:
        1. Obtain a token by sending a POST request to `/api/accounts/auth/login/`
        2. Include the token in subsequent requests in the Authorization header:
            ```
            Authorization: Bearer <your_token>
            ```
        
        ## Rate Limiting
        - 100 requests per minute for authenticated users
        - 20 requests per minute for unauthenticated users
        """,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@ecommerce.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
) 