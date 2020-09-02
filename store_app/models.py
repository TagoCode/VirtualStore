from django.db import models 
import re

class UserManager(models.Manager):
    def reg_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address!"
        if len(post_data['fname']) < 2:
            errors["fname"] = "First name should be at least 2 characters."
        if len(post_data['lname']) < 2:
            errors["lname"] = "Last name should be at least 2 characters."
        if (post_data['password']) != (post_data['conf_password']):
            errors['password'] = "Oops! Passwords do not match."
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be 8 chars or longer!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 

class ItemManager(models.Manager):
    def item_validator(self, post_data):
        errors = {}
        if len(post_data['item_name']) < 3:
            errors['item_name'] = "Item must be no fewer than 3 characters."
        if len(post_data['desc']) < 3:
            errors['desc'] = "Description must be no fewer than 3 characters."
        if len(post_data['electronic']) < 3:
            errors['electronic'] = "Item must be three characters long or greater."
        return errors

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ManyToManyField(User, related_name="items")
    objects = ItemManager()