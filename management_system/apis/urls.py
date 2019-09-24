from django.conf.urls import url
from .views import order_data
from django.urls import path

urlpatterns = [
    path('orders', order_data.as_view()),
]