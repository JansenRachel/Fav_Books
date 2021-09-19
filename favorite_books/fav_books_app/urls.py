from django.urls import path
from . import views


urlpatterns = [
    path('', views.books_index),#dashboard
    path('/add_fav_book', views.add_fav_book)

]