from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/<int:room_id>/', views.booking, name='booking'),
]
