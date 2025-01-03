from django.db import models
from products.models import Product


class Outflow(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='outlflows')
    quantity = models.IntegerField()
    descripition = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # o - antes do creat_at quer dizer que quero as datas mais novas para mais antigas.

    def __str__(self):
        return str(self.product)
