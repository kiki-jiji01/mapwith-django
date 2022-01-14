from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from countries.models import Countries
from .serializers import CountriesSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsCountryOwner

class CountryListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CountriesSerializer

    def get_queryset(self):
        return Countries.objects.all()
    
class CountryCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CountriesSerializer
    
    def perform_create(self, serializer):
            serializer.save(user=self.request.user)


class  CountryDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = CountriesSerializer

    def get_queryset(self):
        return Countries.objects.all()
    
    
class CountryUpdateView(UpdateAPIView):
    permission_classes = [AllowAny,IsCountryOwner]
    serializer_class = CountriesSerializer

    def get_queryset(self):
        return Countries.objects.filter(available=True)
    

class CountryDeleteView(DestroyAPIView):
    permission_classes = [AllowAny,IsCountryOwner]
    def get_queryset(self):
        return Countries.objects.all()