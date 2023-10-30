# discounts/models.py
from django.db import models
from products.models import Category, Gender, Item
from users.models import User


class Discount(models.Model):
    code = models.CharField(max_length=255, unique=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    applicable_categories = models.ManyToManyField(Category)
    applicable_genders = models.ManyToManyField(Gender, blank=True)
    min_purchase_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.code


class UserDiscount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)


class ProductDiscount(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
