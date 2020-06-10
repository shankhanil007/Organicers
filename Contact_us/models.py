from django.db import models

# Create your models here.
class Contact_Us(models.Model):

    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=300)
    query = models.CharField(max_length=100)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name