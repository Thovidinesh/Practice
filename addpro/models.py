from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='downloads/')
    desc = models.TextField()
    price=models.IntegerField()

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    
