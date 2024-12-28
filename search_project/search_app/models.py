from django.db import models
 
class Items(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    reviewAverage = models.FloatField(default=0)
    reviewCount = models.IntegerField(default=0)
    def __str__(self): 
        return self.name
    
class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    yahooGenreId = models.IntegerField(default=0)
    rakutenGenreId = models.IntegerField(default=0)
 
    def __str__(self): 
        return self.name

class Images(models.Model):
    Id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    image = models.URLField()

class Urls(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    rakutenUrl = models.URLField()
    YahooUrl = models.URLField()

class Price(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    maxPrice = models.IntegerField(default=0)
    averagePrice = models.IntegerField(default=0)
    minPrice = models.IntegerField(default=0)

class Review(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)