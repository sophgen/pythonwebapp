from django.urls import path

from . import views

urlpatterns = [
    path('', views.show),
    path('show', views.show),
    path('odr', views.odr),
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]