from django.db import models

class KeyChainInput(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField("date created")