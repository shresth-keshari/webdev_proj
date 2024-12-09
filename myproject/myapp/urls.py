from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),  # Login page
    path('submit-login/', views.submit_login, name='submit_login'),  # Form submission
]
