from rest_framework import serializers
from train.models import *



class PassengerSerializer(serializers.ModelSerializer):
    trip = serializers.SerializerMethodField()
    class Meta:
        model = Passengers
        fields = "__all__"

    def get_flight(self , obj):
        return obj.trip.values()



class DriverSerializer(serializers.ModelSerializer):
    trip = serializers.SerializerMethodField()
    class Meta:
        model = Driver
        fields = "__all__"

        def get_flight(self , obj):
            return obj.trip.values()



class AttendantSerializer(serializers.ModelSerializer):
    flight = serializers.SerializerMethodField()
    class Meta:
        model = Attendants
        fields = "__all__"

    def get_flight(self , obj):
        return obj.trip.values()



class TrainSerializer(serializers.ModelSerializer):
    flight = serializers.SerializerMethodField()
    class Meta:
        model = Train
        fields = "__all__"

    def get_flight(self , obj):
        return obj.trip.values()


class StationSerializer(serializers.ModelSerializer):
    flight = serializers.SerializerMethodField()
    class Meta:
        model = Station
        fields = "__all__"

    def get_flight(self , obj):
        return obj.trip.values()
    
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ["station","station_destination" , "train"]