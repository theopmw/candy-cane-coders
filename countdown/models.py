from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Countdown(models.Model):
    day = models.IntegerField(default=1, null=False, blank=False, validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ])
    start_date = models.DateTimeField(null=False, blank=False, editable=True)

    def __str__(self):
        return f'Day: {self.day} - {self.start_date}'
