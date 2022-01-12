from rest_framework.serializers import ModelSerializer
from countries.models import Countries


class  CountriesSerializer(ModelSerializer):
    class Meta:
        model = Countries
        fields = (
            "id",
            "country_name",
            "content",
            "available",
            "user",
            "date_created",
            
        )