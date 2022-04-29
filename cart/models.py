from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img')
    price = models.FloatField()
    product_id = models.UUIDField(default=uuid.uuid4, primary_key = True, unique = True, editable=False)

    def __str__(self):
        return self.title

class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    cart_id = models.UUIDField(default=uuid.uuid4, primary_key = True, unique = True, editable=False)
    
    @property
    def total(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.subtotal for item in cartitems])
        return total
    
    @property
    def quantity(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.quantity for item in cartitems])
        return total
    

    def __str__(self):
        return str(self.completed)

class Cartitems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    @property
    def subtotal(self):
        total = self.quantity * self.product.price
        return total
    
  

    def __str__(self):
        return self.product.title
