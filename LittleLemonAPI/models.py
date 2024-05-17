from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)
    
class MenuItem(models.Model):
    title = models.CharField(db_index=True, max_length=255)
    price = models.DecimalField(db_index=True, max_digits=6, decimal_places=2)
    featured = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
class Cart(models.Model):