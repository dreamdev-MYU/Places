
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from .views import *
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landing_page,name='landing'),
    path('base/',base_page, name='base'),
    path('home/',HomeView.as_view(), name='home'),
    path('users/',include('users.urls')),
    path('places/',include('places.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)