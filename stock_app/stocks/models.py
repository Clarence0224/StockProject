from django.db import models

# Create your models here.
class Stock(models.Model):
    stockname = models.CharField(max_length=100, null=False, blank=False)
    stock_abv = models.CharField(max_length=4, null=False, blank=False)
    stockprice = models.DecimalField(max_digits=6, decimal_places=2)
    stockqty = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.stockname