from django.db import models
from django.forms import ModelForm

# Create your models here.


class Gift(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class GiftModelForm(ModelForm):
    class Meta:
        model = Gift
        fields = ['name', 'brand', 'price', 'stock']
