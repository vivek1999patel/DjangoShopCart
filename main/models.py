# Create your models here.

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    desc = models.TextField(max_length=250)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products_index')

class Cart(models.Model):
    product = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)