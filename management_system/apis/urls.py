from django.conf.urls import url
from .views import ContactData
from django.urls import path

urlpatterns = [
    path('contact', ContactData.as_view()),
]