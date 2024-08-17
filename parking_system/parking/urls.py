from django.urls import path, include
from django.contrib.auth import views as auth_views
#from .views import HomePageView, VehicleListView, ParkingSessionListView
from django.contrib.auth import views as auth_views
from . import views
from .views import add_vehicle


urlpatterns = [
    path('', views.home, name='home'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('sessions/', views.parking_sessions, name='parking_sessions'),
    path('register/', views.register, name='register'),
    path('add_vehicle/', add_vehicle, name='add_vehicle'),
]
