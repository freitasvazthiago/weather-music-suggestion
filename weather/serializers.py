from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    city_name = serializers.CharField(max_length=200)
    city_id = serializers.CharField(max_length=200)