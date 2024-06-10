from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.hashers import make_password

class CustomUser(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    info = models.TextField()
    slug = models.SlugField(unique=True, max_length=255)

    def save(self, *args, **kwargs):
        # Generate the slug automatically if not provided
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


