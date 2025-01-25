from django.db import models


class AiResult(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    result = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
