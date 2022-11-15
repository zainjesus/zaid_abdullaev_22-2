from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()


class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    price = models.IntegerField()
    description = models.TextField()
    characteristics = models.TextField()
    category = models.ManyToManyField(Category)