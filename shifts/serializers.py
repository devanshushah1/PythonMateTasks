from rest_framework import serializers
from .models import Client, Shift
import datetime


class ClientSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=20)
    password2 = serializers.CharField(max_length=20)

    def validate(self, data):
        #password validation
        if len(data['password'])<8:
            raise serializers.ValidationError('Password should be atleast 8 charecters long.')
        if data['password']!=data['password2']:
            raise serializers.ValidationError('Password did not match')
        return data

    def create(self, validated_data):
        data = validated_data
        return Client.objects.create_user(data['email'], data['password'])

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ['id', 'start_date', 'arrival_time', 'departure_time', 'repeat', 'shift_availibility', 'weekdays']
