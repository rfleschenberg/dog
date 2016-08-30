from django.db import models
from django.contrib.postgres.fields import JSONField


class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = JSONField()
