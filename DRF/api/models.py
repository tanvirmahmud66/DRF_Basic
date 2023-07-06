from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

