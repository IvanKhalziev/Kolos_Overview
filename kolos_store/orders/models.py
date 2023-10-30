# orders/models.py
from django.db import models
from users.models import User
from products.models import Item

# ALso add point of self delivery /// add NP nalozhenniy platezh


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    post_office = models.CharField(max_length=255)
    basket_history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user.username} - {self.id}"
