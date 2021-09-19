from django.db import models
from login_and_reg_app.models import *


class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = "Please add a title"
        if len(postData['desc']) < 5:
            errors['description'] = "Book description must contain be at least 5 characters in length."
        return errors

# SAME USER AS USED IN lOGIN_AND_REG_APP
# class User(models.Model):
#     firstname = models.CharField(max_length=255)
#     lastname = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)
#     password = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     # objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete = models.CASCADE)
    users_liked = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
