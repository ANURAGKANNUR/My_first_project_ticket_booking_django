from django.db import models

# Create your models here.
class Bus(models.Model):
    bus_name=models.CharField(max_length=100)
    source=models.CharField(max_length=20)
    dest=models.CharField(max_length=20)
    nos = models.IntegerField()
    rem = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    date=models.CharField(max_length=5000)
    time=models.CharField(max_length=5000)

    def __str__(self):
        return self.bus_name

class Book(models.Model):
    BOOKED='B'
    CANCELLED='C'
    TICKET_STATUSES=((BOOKED,'Booked'),(CANCELLED,'Cancelled'),)
    email=models.EmailField(max_length=200)
    name=models.CharField(max_length=100)
    userid = models.IntegerField()
    busid=models.DecimalField(decimal_places=0, max_digits=2)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return self.email
