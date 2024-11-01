# Create your models here.
from django.db import models

class Passphrase(models.Model):
    code=models.CharField(max_length=50)

def __str__(self):
    return self.code