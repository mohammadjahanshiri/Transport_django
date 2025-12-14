from django.contrib import admin
from train.models import *

# Register your models here.
admin.site.register(Passengers)
admin.site.register(Driver)
admin.site.register(Attendants)
admin.site.register(Train)
admin.site.register(Trip)
admin.site.register(Station)