from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter


from countries.api.views import CountryListView, CountryCreateView ,CountryUpdateView,  CountryDeleteView, CountryDetailView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()




app_name = "api"

urlpatterns = [
    path("countries/", CountryListView.as_view()),
    path("countries/<pk>/", CountryDetailView.as_view()),
    path("countries/<pk>/update/", CountryUpdateView.as_view()),
    path("countries/<pk>/delete/",  CountryDeleteView.as_view()),
    path("create-countries/", CountryCreateView.as_view()),
    ]

urlpatterns += router.urls