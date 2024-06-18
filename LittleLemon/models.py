from django.db import models
from django.forms.models import model_to_dict
from django.http import JsonResponse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['price']),
        ]

