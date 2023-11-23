from django.db import models


class Item(models.Model):
    name = models.CharField(max_lenght=30)
    quantity = models.IntegerField()
