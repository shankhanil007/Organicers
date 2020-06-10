from django.db import models
from Category_Auth.models import Category

# Create your models here.
class Event(models.Model):

    EVENT_STATUS = (
        ('Upcoming','Upcoming'),
        ('Ongoing','Ongoing'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),
    )

    PAYMENT_STATUS = (
        ('Due', 'Due'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('Failed','Failed'),
    )

    name = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.CharField(max_length=300)

    bookie_first_name = models.CharField(max_length=50)
    bookie_last_name = models.CharField(max_length=50)
    bookie_phone = models.IntegerField()
    bookie_email = models.EmailField()
    bookie_address = models.CharField(max_length=300)
    date = models.DateTimeField()
    event_status = models.CharField(max_length=20, choices= EVENT_STATUS, default='Upcoming')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='due')

    alt_first_name = models.CharField(max_length=50)
    alt_last_name = models.CharField(max_length=50)
    alt_phone = models.IntegerField()
    alt_email = models.EmailField()

    def __str__(self):
        return self.desc