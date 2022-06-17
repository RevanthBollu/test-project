from django.db import models

# Create your models here.

class Employee(models.Model):
    Id_No = models.IntegerField()
    Name=models.CharField(max_length=100)
    Address=models.TextField()
    Mobile_No=models.BigIntegerField()
    Emp_Role=models.CharField(max_length=100)

    def __str__(self):
        return self.Name
