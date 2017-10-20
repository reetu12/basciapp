from rest_framework import serializers
from role.models import Pets

class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pets
        fields = ['pk', 'name', 'pet_type', 'birthday']