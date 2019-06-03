from django.db import models

class RegistrationData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    mobile_number = models.IntegerField()
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)