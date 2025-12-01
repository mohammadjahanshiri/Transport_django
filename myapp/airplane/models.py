from django.db import models

class Passenger(models.Model):
    fullname = models.CharField(max_length=128 , verbose_name="نام مسافر")
    national_id = models.CharField(max_length=10 , unique=True , verbose_name="کد ملی مسافر")



class Pilot(models.Model):
    fullname = models.CharField(max_length=128 , verbose_name="نام خلبان")
    national_id = models.CharField(max_length=10 , unique=True , verbose_name="کد ملی خلبان")


class Attendant(models.Model):
    fullname = models.CharField(max_length=128 , verbose_name="نام مهماندار")
    national_id = models.CharField(max_length=10 , unique=True , verbose_name="کد ملی مهماندار")



class Airplane(models.Model):
    code = models.CharField(max_length=20 , verbose_name="کد هواپیما" , unique=True)
    capacity = models.PositiveIntegerField(verbose_name="ظرفیت هواپیما")



class Airport(models.Model):
    name = models.CharField(max_length=100 , verbose_name="نام فرودگاه")
    city = models.CharField(max_length=100 , verbose_name="شهر فرودگاه")



class Flight(models.Model):
    airplane = models.ForeignKey(Airplane , on_delete=models.SET_NULL , related_name="airplane_fligt" , null=True , blank=True)
    airport = models.ForeignKey(Airport, on_delete=models.SET_NULL , related_name="airport_flight" , null=True , blank=True)
    passengers = models.ManyToManyField(Passenger ,  related_name="passengers_flight")
    pilot = models.ForeignKey(Pilot , on_delete=models.SET_NULL , related_name="pilot_flight" , null=True , blank=True)
    arrival_time = models.DateTimeField()
