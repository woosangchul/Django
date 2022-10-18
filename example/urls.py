from django.shortcuts import render
from django.urls import path,include
from .views import booksAPI
urlpatterns = [
    path("fbv/books/", booksAPI),
]
