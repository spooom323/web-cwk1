from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, db_column='username',)
    name = models.CharField(max_length=128,)

    def __str__(self):
        return self.name




class Story(models.Model):
    key = models.AutoField(unique=True, primary_key= True,)
    headline = models.CharField(max_length=64,)
    category = models.CharField(max_length=64, choices=((u'pol', u'politics'), (u'art', u'art'), (u'tech', u'technology'), (u'trivia', u'trivial'),),)
    region = models.CharField(max_length=64, choices=((u'uk',u'UK'), (u'eu', u'European'), (u'w', u'World')),)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, )
    date = models.DateField('date published', auto_now_add=True)
    details = models.CharField(max_length=512,)

    def __str__(self):
        return u'%s - %s - %s' % (self.key, self.headline, self.date)

