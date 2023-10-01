from django.db import models


class Role(models.Model):
    emp_deg = models.CharField(max_length=100)
    emp_salary=models.IntegerField()
    emp_join_date = models.CharField(max_length=100)

class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_age = models.IntegerField()
    emp_email = models.CharField(max_length=100)
    emp_number = models.CharField(max_length=100)
    emp_address = models.CharField(max_length=100)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name







