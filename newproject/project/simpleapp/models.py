from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.cache import cache


class Product(models.Model):
    name = models.CharField(
        max_length = 50,
        unique = True,
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators = [MinValueValidator(0)],
    )
    category = models.ForeignKey(
        to = 'Category',
        on_delete = models.CASCADE,
        related_name = 'products',
    )
    price = models.FloatField(
        validators = [MinValueValidator(0.0)],
    )

    @property
    def on_stock(self):
        return self.quantity > 0


    def __str__(self):
        return f'{self.name.title()}: {self.description[:10]}'

    def get_absolute_url(self):
        return reverse('product_detail', args = [str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'product-{self.pk}')


class Category(models.Model):
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.name.title()


class Subscription(models.Model):
    user = models.ForeignKey(
        to = User,
        on_delete = models.CASCADE,
        related_name = 'subscriptions',
    )
    category = models.ForeignKey(
        to = 'Category',
        on_delete = models.CASCADE,
        related_name = 'subscriptions',
    )
