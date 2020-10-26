from django.db import models

# Create your models here.

class employees(models.Model):
    emp_id=models.IntegerField()
    firstName=models.CharField(max_length=10)
    lastName=models.CharField(max_length=10)

    def __str__(self):
        return self.firstName