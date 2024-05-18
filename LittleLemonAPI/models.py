from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, db_index=True)
    
    def __str__(self):
        return self.title
    
class MenuItem(models.Model):
    title = models.CharField(db_index=True, max_length=255)
    price = models.DecimalField(db_index=True, max_digits=7, decimal_places=2)
    featured = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.title
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.unit_price = self.menuitem.price  # Ensuring the unit price matches the menu item price
        self.price = self.unit_price * self.quantity  # Calculating the total price
        super().save(*args, **kwargs)
    
    class Meta:
        unique_together = ('menuitem', 'user')
    
    def __str__(self):
        return f'{self.quantity} x {self.menuitem.title} (Cart of {self.user.username})'
        
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='orders_delivered', null=True)
    is_delivered = models.BooleanField(db_index=True, default=False)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(db_index=True)
    
    def __str__(self):
        return f'Order {self.id} by {self.user.username}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    
    class Meta:
        unique_together = ('order', 'menuitem')
    
    def __str__(self):
        return f'{self.quantity} x {self.menuitem.title} (Order {self.order.id})'
