from django.urls import path, include
from rest_framework.routers import DefaultRouter
from train.api import *


app_name = "train"

router = DefaultRouter()

router.register("all-passengers",PassengersModelviewset , basename="all-passengers")
router.register("all-drivers", DriverModelviewset, basename="all-drivers")
router.register("all-attendants", AttendantModelviewset, basename="all-attendants")
router.register("all-stations", StationModelviewset, basename="all-stations")
router.register("all-trains", TrainModelviewset, basename="all-trains")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/add_passenger/" , EnrollPassengersApi.as_view()),
    path("api/add_attendant/" , EnrollAttendantApi.as_view()),
    path("api/createtrip/", CreateTripApi.as_view())
]