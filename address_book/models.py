from django.db import models

# Create your models here.
class addressModel(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    def __str__(self):
        return self.Name
