from django.db import models

class Passenger(models.Model):
    fullname = models.CharField(max_length=128 , verbose_name="نام مسافر")
    national_id = models.CharField(max_length=10 , unique=True , verbose_name="کد ملی مسافر")



class Driver(models.Model):
    fullname = models.CharField(max_length=128 , verbose_name="نام راننده")
    national_id = models.CharField(max_length=10 , unique=True , verbose_name="کد ملی راانده")


class Attendant(models.Model):
    fullname = models.CharField(max_length=128 , verbose_name="نام مهماندار")
    national_id = models.CharField(max_length=10 , unique=True , verbose_name="کد ملی مهماندار")



class Train(models.Model):
    code = models.CharField(max_length=20 , verbose_name="کد قطار" , unique=True)
    capacity = models.PositiveIntegerField(verbose_name="ظرفیت قطار")



class Station(models.Model):
    name = models.CharField(max_length=100 , verbose_name="نام ایستگاه")
    city = models.CharField(max_length=100 , verbose_name="شهر ایستگاه")



class Trip(models.Model):
    train = models.ForeignKey(Train , on_delete=models.SET_NULL , related_name="train_trip" , null=True , blank=True)
    station = models.ForeignKey(Station, on_delete=models.SET_NULL , null=True , blank=True)
    passengers = models.ManyToManyField(Passenger ,  related_name="passengers_trip" , null=True , blank=True)
    driver = models.ForeignKey(Driver , on_delete=models.SET_NULL , related_name= "driver_trip" , null=True , blank=True)
    arrival_time = models.DateTimeField()