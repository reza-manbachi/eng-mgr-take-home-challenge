from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from .users import User

class WorkedHour(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, date) found, that is not supported. The first column is selected.
    date = models.DateField()
    hours = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(24)])
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user}: {self.date} {self.hours}'

    class Meta:
        db_table = 'worked_hours'
        managed = False
        unique_together = (('user', 'date'),)
