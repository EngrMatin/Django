from django.db import models

# Create your models (database table schema) here.
class reviewer(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    review = models.CharField(max_length=100)
    age = models.IntegerField()
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)
    youtube = models.BooleanField()
    