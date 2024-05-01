from django.urls import path
from .views import saybye

urlpatterns = [
    path('bye/', saybye)
]