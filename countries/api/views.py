from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from countries.models import Countries
from .serializers import CountriesSerializer


class CountryListView(ListAPIView):
    serializer_class = CountriesSerializer

    def get_queryset(self):
        return Countries.objects.all()
    
class CountryCreateView(CreateAPIView):
    
    serializer_class = CountriesSerializer
    
    def perform_create(self, serializer):
            serializer.save(user=self.request.user)


class  CountryDetailView(RetrieveAPIView):
    serializer_class = CountriesSerializer

    def get_queryset(self):
        return Countries.objects.all()
    
    
class CountryUpdateView(UpdateAPIView):
    serializer_class = CountriesSerializer

    def get_queryset(self):
        return Countries.objects.filter(available=True)
    

class CountryDeleteView(DestroyAPIView):
    def get_queryset(self):
        return Countries.objects.all()