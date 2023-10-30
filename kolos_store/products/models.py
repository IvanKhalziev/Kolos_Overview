# products/models.py
from django.db import models


class GlobalCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quantity(models.Model):
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.quantity}"


class Color(models.Model):
    name = models.CharField(max_length=255)
    hex = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f"{self.name} | {self.hex}"


class Size(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# collections add

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    global_category = models.ForeignKey(
        GlobalCategory, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    colors = models.ManyToManyField(Color, through='QuantityItemColorSize')
    sizes = models.ManyToManyField(Size, through='QuantityItemColorSize')

    def __str__(self):
        return self.name


class QuantityItemColorSize(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)
    photo_url = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.item.name} | {self.size.name} | {self.color.name} | {self.color.hex} | {self.quantity.quantity}"
