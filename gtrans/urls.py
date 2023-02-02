from django.urls import path
from .views import translator

urlpatterns = [
    path('', translator, name='translator'),
]
