from distutils.command.upload import upload
from tabnanny import verbose
from tkinter import CASCADE
from unicodedata import category
from django.db import models

class Category(models.Model):    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    
    name = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    options = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    cost = models.IntegerField()
    percent = models.IntegerField()
    img = models.ImageField(upload_to="images/", null=True, blank=True)
    
    def __str__(self):
        return self.name
