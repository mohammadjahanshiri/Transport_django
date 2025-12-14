from django.db import models
from django.contrib.auth.models import User

class Passengers(models.Model):
    fullname = models.CharField(max_length=128 , verbose_name="نام مسافر")
    national_id = models.CharField(max_length=10 , unique=True , verbose_name="کد ملی مسافر")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True , blank=True)
    def __str__(self):
        return self.fullname



class Driver(models.Model):
    fullname = models.CharField(max_length=128 , verbose_name="نام راننده")
    national_id = models.CharField(max_length=10 , unique=True , verbose_name="کد ملی راانده")
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.fullname


class Attendants(models.Model):
    fullname = models.CharField(max_length=128 , verbose_name="نام مهماندار")
    national_id = models.CharField(max_length=10 , unique=True , verbose_name="کد ملی مهماندار")
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.fullname



class Train(models.Model):
    code = models.CharField(max_length=20 , verbose_name="کد قطار" , unique=True)
    capacity = models.PositiveIntegerField(verbose_name="ظرفیت قطار")
    def __str__(self):
        return self.code



class Station(models.Model):
    name = models.CharField(max_length=100 , verbose_name="نام ایستگاه")
    city = models.CharField(max_length=100 , verbose_name="شهر ایستگاه")
    def __str__(self):
        return self.name



class Trip(models.Model):
    train = models.ForeignKey(Train , on_delete=models.SET_NULL , related_name="trip" , null=True , blank=True)
    station = models.ForeignKey(Station, on_delete=models.SET_NULL , null=True , blank=True , related_name="trip")
    station_destination = models.ForeignKey(Station , on_delete=models.SET_NULL , null=True , blank=True , related_name="trip2")
    passengers = models.ManyToManyField(Passengers ,  related_name="trip" , blank=True)
    driver = models.ForeignKey(Driver , on_delete=models.SET_NULL , related_name= "trip" , null=True , blank=True)
    attendants = models.ManyToManyField(Attendants , related_name="trip" , blank=True)
    arrival_time = models.DateTimeField(null=True , blank=True)