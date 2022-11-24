from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    price = models.IntegerField()

    def __str__(self):
        return self.name
