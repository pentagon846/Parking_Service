from django.urls import path, include
from . import views, admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('parking_system.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    # other patterns
]
