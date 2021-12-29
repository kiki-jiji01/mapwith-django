from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter


from countries.api.views import CountryListView, CountryCreateView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()




app_name = "api"

urlpatterns = [
    path("countries/", CountryListView.as_view()),
    path("create-countries/", CountryCreateView.as_view()),
    ]

urlpatterns += router.urls