from django.db import models

class Gift(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    day = models.IntegerField(default=1, null=False, blank=False)
