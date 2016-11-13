from django.db import models
from django.utils import timezone


class Car(models.Model):
    name = models.CharField(max_length='20', unique=True, verbose_name="Name product")
    description = models.TextField()
    quality = models.IntegerField()
    datetime = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = ["-quality", "name"]

    def __unicode__(self):
        return self.name



