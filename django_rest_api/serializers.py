from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def validate(self, data):
        special_characters = "!@#$%^&*()-_=+,<>/?|[]"
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError('Name cannot contain special character')


        if data['age'] < 18:
            raise serializers.ValidationError('Age should not be less than 18')
            
        return data