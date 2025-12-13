from rest_framework.views import APIView
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.viewsets import ViewSet , ModelViewSet
from airplane.models import *
from airplane.serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsPilot



class PassengersModelviewset(ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class PilotModelviewset(ModelViewSet):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer


class AttendantModelviewset(ModelViewSet):
    queryset = Attendant.objects.all()
    serializer_class = AttendantSerializer


class AirplaneModelviewset(ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


class AirportModelviewset(ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer



class EnrollPassengersApi(APIView):

    def post(self, request):
        data = request.data
        ps_id = data["passenger_id"]
        fl_id = data["flight_id"]
        try:
            passenger = Passenger.objects.get(id=ps_id) 
            flight = Flight.objects.get(id=fl_id)
            if passenger in flight.passengers.all():
                return Response({"message": "this passenger has exists"}, status=status.HTTP_400_BAD_REQUEST)
            passenger.flight.add(flight)
        except ObjectDoesNotExist:
            return Response({"message": "error does not exists"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"message": "passenger added"}, status=status.HTTP_200_OK)
    

class EnrollAttendantApi(APIView):

    def post(self, request):
        data = request.data
        at_id = data["attendant_id"]
        fl_id = data["flight_id"]
        try:
            attendant = Attendant.objects.get(id=at_id) 
            flight = Flight.objects.get(id=fl_id)
            if attendant in flight.passengers.all():
                return Response({"message": "this attendant has exists"}, status=status.HTTP_400_BAD_REQUEST)
            attendant.flight.add(flight)
        except ObjectDoesNotExist:
            return Response({"message": "error does not exists"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"message": "attendant added"}, status=status.HTTP_200_OK)
    

class CreateFlightApi(APIView):
    permission_classes = [IsAuthenticated , IsPilot]
    def post(self , request):
        serializer = FlightSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pilot = Pilot.objects.get(user=request.user)
        flight = serializer.save(pilot=pilot)
        return Response({"message" : "successfully created"} , status=status.HTTP_201_CREATED)