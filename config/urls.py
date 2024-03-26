
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landing_page,name='landing'),
    path('base/',base_page, name='base'),
    path('',include('users.urls')),
    path('',include('places.urls')),
]