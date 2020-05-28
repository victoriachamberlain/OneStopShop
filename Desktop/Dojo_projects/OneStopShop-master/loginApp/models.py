from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
from django.utils.dateparse import parse_date
import re
from productsApp import *

class UserManager(models.Manager):
    def registration_validation(self, postData):
        EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
        PW_REGEX = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,32}$")
        errors = {}

        #First name validation
        if len(postData['first_name']) == 0:
            errors['first_name'] = "This field cannot be left empty!"
        elif len(postData['first_name']) < 2:
            errors['first_name'] = "The first name has to be more than 2 characters long!"
        elif len(postData['first_name']) > 30:
            erorrs['first_name'] = "The first name cannot be more than 30 characters long!"
            
        #Last name validation
        if len(postData['last_name']) == 0:
            errors['last_name'] = "This field cannot be left empty!"
        elif len(postData['last_name']) < 2:
            errors['last_name'] = "The last name has to be more than 2 characters long!"
        elif len(postData['last_name']) > 30:
            erorrs['last_name'] = "The last name cannot be more than 30 characters long!"

        #Email validation
        user = User.objects.filter(email = postData['email'])
        if len(postData['email']) == 0:
            errors['email'] = "This field cannot be left empty!"
        elif len(postData['email']) < 6:
            errors['email'] = "Invalid email address!"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        elif user:
            errors['email'] = "Email already registered! Please use another email address."

        #Birthday validation
        if parse_date(postData['birthdayReg']) > date.today():
            errors['birthdayReg'] = "You must enter a date in the past!"
        elif parse_date(postData['birthdayReg']) >= date(date.today().year - 13, date.today().month, date.today().day):
            errors['birthdayReg'] = "You must be older than 13 to register!"

        #Password validation
        if len(postData['password']) == 0:
            errors['password'] = "This field cannot be left empty!"
        elif len(postData['password']) < 8:
            errors['password'] = "The password must be a minimum of 8 characters!"
        elif not PW_REGEX.match(postData['password']):
            errors['password'] = "Password must contain a minimum of 1 uppercase, 1 lowercase, 1 number, and 1 special character!"
        elif postData['password'] != postData['pw_confirm']:
            errors['password'] = "Passwords do not match!"

        return errors

    def update_validation(self, postData):
        EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
        errors = {}

        if len(postData['updated_first_name']) == 0:
            errors['updated_first_name'] = "This field cannot be left blank!"
        elif len(postData['updated_first_name']) < 2:
            errors['updated_first_name'] = "The first name has to be more than 2 characters long!"
        elif len(postData['updated_first_name']) > 30:
            erorrs['updated_first_name'] = "The first name cannot be more than 30 characters long!"
            
        if len(postData['updated_last_name']) == 0:
            errors['updated_last_name'] = "This field cannot be left blank!"
        elif len(postData['updated_last_name']) < 2:
            errors['updated_last_name'] = "The last name has to be more than 2 characters long!"
        elif len(postData['updated_last_name']) > 30:
            erorrs['updated_last_name'] = "The last name cannot be more than 30 characters long!"

        user = User.objects.exclude(email = postData['updated_email'])
        if len(postData['updated_email']) == 0:
            errors['updated_email'] = "This field cannot be left empty!"
        elif len(postData['updated_email']) < 6:
            errors['updated_email'] = "Invalid email address!"
        elif not EMAIL_REGEX.match(postData['updated_email']):
            errors['updated_email'] = "Invalid email address!"
        elif postData['updated_email'] in user:
            errors['updated_email'] = "Email already registered! Please use another email address."

        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50)
    birth_date = models.DateField()
    password = models.CharField(max_length = 200)

    # one to one relationships with wishlist and shopping cart
    # one to many relationhip with order
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()