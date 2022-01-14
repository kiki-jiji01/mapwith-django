from rest_framework.serializers import ModelSerializer
from countries.models import Countries
from rest_framework.serializers import ModelSerializer

from rest_framework import serializers

class  CountriesSerializer(serializers.ModelSerializer):
    
    is_owner = serializers.SerializerMethodField()
      
    class Meta:
        model = Countries
        fields = (
            "id",
            "country_name",
            "content",
            "available",
            "user",
            "date_created",
            "is_owner",
            
        )
        read_only_fields = ( "date_created","user")
        
    def get_is_owner(self, obj):
        user = self.context["request"].user
        return obj.user == user