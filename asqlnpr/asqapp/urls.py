from django.urls import path
from . import views

app_name='asqapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('gallery/',views.gallery,name='gallery'),
    path('register/',views.register,name='register'),

]