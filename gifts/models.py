from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Gift(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    day = models.IntegerField(default=1, null=False, blank=False, validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ])

    def __str__(self):
        return self.name