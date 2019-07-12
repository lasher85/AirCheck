from rest_framework import serializers
from aircheck.models import Krakow, Tenczynek, Katowice, Krzeszowice, Grudziadz, Gdansk, Gdynia
 
class KrakowSerializer(serializers.ModelSerializer):
    """
    Serializing all records
    """
    class Meta:
        model = Krakow
        fields = ('data', 'pm1', 'pm25', 'pm10', 'pressure', 'humidity', 'temperature')

class TenczynekSerializer(serializers.ModelSerializer):
    """
    Serializing all records
    """
    class Meta:
        model = Tenczynek
        fields = ('data', 'pm1', 'pm25', 'pm10', 'pressure', 'humidity', 'temperature')

class KatowiceSerializer(serializers.ModelSerializer):
    """
    Serializing all records
    """
    class Meta:
        model = Katowice
        fields = ('data', 'pm1', 'pm25', 'pm10', 'pressure', 'humidity', 'temperature')

class KrzeszowiceSerializer(serializers.ModelSerializer):
    """
    Serializing all records
    """
    class Meta:
        model = Krzeszowice
        fields = ('data', 'pm1', 'pm25', 'pm10', 'pressure', 'humidity', 'temperature')

class GrudziadzSerializer(serializers.ModelSerializer):
    """
    Serializing all records
    """
    class Meta:
        model = Grudziadz
        fields = ('data', 'pm1', 'pm25', 'pm10', 'pressure', 'humidity', 'temperature')

class GdanskSerializer(serializers.ModelSerializer):
    """
    Serializing all records
    """
    class Meta:
        model = Gdansk
        fields = ('data', 'pm1', 'pm25', 'pm10', 'pressure', 'humidity', 'temperature')

class GdyniaSerializer(serializers.ModelSerializer):
    """
    Serializing all records
    """
    class Meta:
        model = Gdynia
        fields = ('data', 'pm1', 'pm25', 'pm10', 'pressure', 'humidity', 'temperature')