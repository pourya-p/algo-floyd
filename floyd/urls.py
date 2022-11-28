from django.urls import path, include
from .views import compute
app_name = 'floyd'
urlpatterns = [
    path('', compute, name='home'),
]