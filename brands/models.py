from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Propriedade auto_now_add=True (toda vez que eu criar um registro ja pega a data e hora automaticamente)
    update_at = models.DateTimeField(auto_now=True)  # Diferente da propriedade de cima ela so salva quando é alterado.

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
