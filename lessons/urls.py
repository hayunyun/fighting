
from django.urls import path, include
from django.contrib import admin
from . import views
 
app_name = "lessons"
urlpatterns = [
<<<<<<< HEAD
    path('<int:id>/', views.show, name="show"),
    path('', views.home, name="list"),
=======
    # path('<int:id>/', views.show, name="show"),
    # path('', views.home, name="home"),
>>>>>>> 7b1b590b4156051420c25dd63c20c262e8a3fad8

]
