from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now_add=True, editable=False)
    category = models.ForeignKey('Category')

    def __unicode__(self):
        return u"%s" %self.author

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s" %self.name
