from django.urls import path, include
from rest_framework.routers import DefaultRouter
from airplane.api import *


app_name = "airplane"

router = DefaultRouter()

router.register("all-passengers",PassengersModelviewset , basename="all-passengers")
router.register("all-pilots", PilotModelviewset, basename="all-pilots")
router.register("all-attendants", AttendantModelviewset, basename="all-attendants")
router.register("all-airports", AirportModelviewset, basename="all-airports")
router.register("all-airplanes", AirplaneModelviewset, basename="all-airplanes")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/add_passenger/" , EnrollPassengersApi.as_view()),
    path("api/add_attendant/" , EnrollAttendantApi.as_view()),
    path("api/createflight/", CreateFlightApi.as_view())
]