from django.urls import path
from .views import places_page, about,landing,AddCommentView

app_name = 'places'
urlpatterns = [
    path('places/', places_page, name='places-page'),
    path('about/<int:id>/', about, name='about-page'),  
    path('landing/', landing, name='landing-page'),  
    path('add-comment/<int:id>/',AddCommentView.as_view(), name='add-comment'),  
]
