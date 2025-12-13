from rest_framework import serializers
from airplane.models import *



class PassengerSerializer(serializers.ModelSerializer):
    flight = serializers.SerializerMethodField()
    class Meta:
        model = Passenger
        fields = "__all__"

    def get_flight(self , obj):
        return obj.flight.values()



class PilotSerializer(serializers.ModelSerializer):
    flight = serializers.SerializerMethodField()
    class Meta:
        model = Pilot
        fields = "__all__"

        def get_flight(self , obj):
            return obj.flight.values()



class AttendantSerializer(serializers.ModelSerializer):
    flight = serializers.SerializerMethodField()
    class Meta:
        model = Attendant
        fields = "__all__"

    def get_flight(self , obj):
        return obj.flight.values()



class AirplaneSerializer(serializers.ModelSerializer):
    flight = serializers.SerializerMethodField()
    class Meta:
        model = Airplane
        fields = "__all__"

    def get_flight(self , obj):
        return obj.flight.values()


class AirportSerializer(serializers.ModelSerializer):
    flight = serializers.SerializerMethodField()
    class Meta:
        model = Airport
        fields = "__all__"

    def get_flight(self , obj):
        return obj.flight.values()
    
class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["airport_origin","airport_destination" , "airplane"]