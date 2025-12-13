from django.db import models
from django.contrib.auth.models import User

class Passenger(models.Model):
    fullname = models.CharField(max_length=128 , verbose_name="نام مسافر")
    national_id = models.CharField(max_length=10 , unique=True , verbose_name="کد ملی مسافر")
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.fullname



class Pilot(models.Model):
    fullname = models.CharField(max_length=128 , verbose_name="نام خلبان")
    national_id = models.CharField(max_length=10 , unique=True , verbose_name="کد ملی خلبان")
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.fullname


class Attendant(models.Model):
    fullname = models.CharField(max_length=128 , verbose_name="نام مهماندار")
    national_id = models.CharField(max_length=10 , unique=True , verbose_name="کد ملی مهماندار")
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.fullname



class Airplane(models.Model):
    code = models.CharField(max_length=20 , verbose_name="کد هواپیما" , unique=True)
    capacity = models.PositiveIntegerField(verbose_name="ظرفیت هواپیما")
    def __str__(self):
        return self.code



class Airport(models.Model):
    name = models.CharField(max_length=100 , verbose_name="نام فرودگاه")
    city = models.CharField(max_length=100 , verbose_name="شهر فرودگاه")
    def __str__(self):
        return self.name
    
    

class Flight(models.Model):
    airplane = models.ForeignKey(Airplane , on_delete=models.SET_NULL , related_name="fligt" , null=True , blank=True  , verbose_name="هواپیمای پرواز")
    airport_origin = models.ForeignKey(Airport, on_delete=models.SET_NULL , related_name="flight" , null=True , blank=True , verbose_name="فرودگاه مبدا")
    airport_destination = models.ForeignKey(Airport , on_delete=models.SET_NULL , related_name="flight2" , null=True , blank=True , verbose_name="فرودگاه مقصد")
    passengers = models.ManyToManyField(Passenger ,  related_name="flight" , verbose_name="مسافر های پرواز" , null=True , blank=True)
    attendant = models.ManyToManyField(Attendant , related_name="flight" , verbose_name="مهماندار های پرواز" , null=True , blank=True)
    pilot = models.ForeignKey(Pilot , on_delete=models.SET_NULL , related_name="flight" , null=True , blank=True , verbose_name="خلبان پرواز")
    arrival_time = models.DateTimeField(verbose_name="زمان اتمام پرواز" , null=True)