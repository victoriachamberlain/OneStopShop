from django.db import models

# Create your models here.
# class Shipping(models.Model):
#     firstName = models.CharField(max_length=13)
#     lastName = models.CharField(max_length=23)
#     address = models.CharField(max_length=101)
#     address2 = models.CharField(max_length=101)
#     city = models.CharField(max_length=13)
#     state = models.CharField(max_length=13)
#     zipCode = models.IntegerField(max_length=13)
#     created_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
# class Billing(models.Model):
#     userID = models.ForeignKey(User, related_name="post", on_delete = models.CASCADE)
#     card = models.IntegerField(max_length=17)
#     securityCode = models.IntegerField(max_length=3)
#     expiration = models.Datefield()
#     created_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)