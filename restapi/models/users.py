from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    manager_id = models.IntegerField(null=True, blank=True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.id}: {self.first_name} {self.last_name}  ({self.email})'


    class Meta:
        db_table = 'users'
        managed = False
