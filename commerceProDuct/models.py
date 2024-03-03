from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name    

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

# class Cart(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     items = models.ManyToManyField(Product, through='CartItem')

#     def __str__(self):
#         return self.user.username


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name
      

