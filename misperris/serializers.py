from rest_framework import serializers
from .models import Goku

class perroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goku   
        fields = '__all__'