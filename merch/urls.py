from django.urls import path
from . import views


urlpatterns = [
    path('merch/', views.merch, name='merch'),
]