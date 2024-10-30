from django.db import models

class Student(models.Model):
    profile_image = models.URLField(max_length=255)
    full_name = models.CharField(max_length=100)
    cohort = models.CharField(max_length=50)
    program = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    date_joined = models.DateField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.full_name