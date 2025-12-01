from django.contrib import admin
from train.models import *

# Register your models here.
admin.site.register(Passenger)
admin.site.register(Driver)
admin.site.register(Attendant)
admin.site.register(Train)
admin.site.register(Trip)
admin.site.register(Station)