
from django.urls import path
from .views import RegisterView, LoginView
from . import views
urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('main/', views.login_main, name="main"),
    
]
