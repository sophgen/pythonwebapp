"""management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Demo Swagger API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order_entry/', include('order_entry.urls')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('customer/', include('apis.urls')),
    path('swagger/', schema_view),
    path('apis/', include('apis.urls')),
    
]
