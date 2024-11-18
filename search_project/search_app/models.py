from django.db import models
from .consts import MAX_RATE

CATEGORY = (('anime', 'アニメ'), ('game', 'ゲーム'), ('other', 'その他'))

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]


class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.CharField(
        max_length=100,
        choices=CATEGORY,
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Like(models.Model):
    user_id = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    target = models.ForeignKey(Book,on_delete=models.CASCADE)