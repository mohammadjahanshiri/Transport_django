from rest_framework.views import APIView
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.viewsets import ViewSet , ModelViewSet
from train.models import *
from train.serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsDriver



class PassengersModelviewset(ModelViewSet):
    queryset = Passengers.objects.all()
    serializer_class = PassengerSerializer


class DriverModelviewset(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class AttendantModelviewset(ModelViewSet):
    queryset = Attendants.objects.all()
    serializer_class = AttendantSerializer


class TrainModelviewset(ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer


class StationModelviewset(ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer



class EnrollPassengersApi(APIView):

    def post(self, request):
        data = request.data
        ps_id = data["passenger_id"]
        tp_id = data["trip_id"]
        try:
            passenger = Passengers.objects.get(id=ps_id) 
            trip = Trip.objects.get(id=tp_id)
            if passenger in trip.passengers.all():
                return Response({"message": "this passenger has exists"}, status=status.HTTP_400_BAD_REQUEST)
            passenger.trip.add(trip)
        except ObjectDoesNotExist:
            return Response({"message": "error does not exists"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"message": "passenger added"}, status=status.HTTP_200_OK)
    

class EnrollAttendantApi(APIView):

    def post(self, request):
        data = request.data
        at_id = data["attendant_id"]
        tp_id = data["trip_id"]
        try:
            attendant = Attendants.objects.get(id=at_id) 
            trip = Trip.objects.get(id=tp_id)
            if attendant in trip.passengers.all():
                return Response({"message": "this attendant has exists"}, status=status.HTTP_400_BAD_REQUEST)
            attendant.trip.add(trip)
        except ObjectDoesNotExist:
            return Response({"message": "error does not exists"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"message": "attendant added"}, status=status.HTTP_200_OK)
    

class CreateTripApi(APIView):
    permission_classes = [IsAuthenticated , IsDriver]
    def post(self , request):
        serializer = TripSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        driver = Driver.objects.get(user=request.user)
        trip = serializer.save(driver=driver)
        return Response({"message" : "successfully created"} , status=status.HTTP_201_CREATED)