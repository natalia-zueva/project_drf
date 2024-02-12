from rest_framework import serializers

from vehicle.models import Car


class CarSerializer(serializers.ModelSerializer):
    model = Car
    fields = '__all__'
