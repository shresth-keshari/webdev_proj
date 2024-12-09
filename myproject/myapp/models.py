from django.db import models

class LoginData(models.Model):
    username = models.CharField(max_length=255)  # Field to store username or email
    password = models.CharField(max_length=255)  # Field to store password

    def __str__(self):
        return self.username  # Display username in the admin panel
