from rest_framework.generics import ListAPIView, CreateAPIView
from countries.models import Countries
from .serializers import CountriesSerializer


class CountryListView(ListAPIView):
    serializer_class = CountriesSerializer

    def get_queryset(self):
        return Countries.objects.all()
    
class CountryCreateView(CreateAPIView):
    
    serializer_class = CountriesSerializer