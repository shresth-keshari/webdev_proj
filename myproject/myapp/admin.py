from django.contrib import admin
from .models import LoginData

@admin.register(LoginData)
class LoginDataAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')  # Show username and password in admin
