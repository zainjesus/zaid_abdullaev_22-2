from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.title


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField()
    price = models.IntegerField()
    description = models.TextField()
    characteristics = models.TextField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.seller.username}_{self.title}'


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()

    rate = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')
    )

    grade = models.CharField(default=5, choices=rate, max_length=10)

    def __str__(self):
        return f'{self.author.username}_{self.product}'
