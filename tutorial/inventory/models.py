from django.db import models


class Category(models.Model):
    categoryName = models.CharField(max_length=100)


class Product(models.Model):
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productBand = models.CharField(max_length=100)
