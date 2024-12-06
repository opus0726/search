from django.db import models

class Category(models.Model): 
    name = models.CharField(max_length=255) 
 
    def __str__(self): 
        return self.name 
 
class Product(models.Model): 
    id = models.BigAutoField(primary_key=True) 
    name = models.CharField(max_length=255) 
    description = models.TextField() 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) 
 
    def __str__(self): 
        return self.name
    
    class Meta:
        db_table = 'product'


class Review(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Like(models.Model):
    user_id = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    target = models.ForeignKey(Product,on_delete=models.CASCADE)