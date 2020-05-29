from django.db import models

class Admin(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    username = models.CharField(max_length = 50)
    email = models.CharField(max_length = 60)
    birth_date = models.DateField()
    password = models.CharField(max_length = 200)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)