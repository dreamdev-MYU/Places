from django.urls import path
from .views import places_page, about,landing,AddCommentView
from django.contrib.auth import views as auth_views

app_name = 'places'


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('places/', places_page, name='places-page'),
    path('about/<int:id>/', about, name='about-page'),  
    path('landing/', landing, name='landing-page'),  
    path('add-comment/<int:id>/',AddCommentView.as_view(), name='add-comment'),  
]

