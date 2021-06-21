from django.urls import path
from carrental.views import (
CarsListView, CarsCreateView, CarsDeleteView, CarsDetailView, CarsUpdateView)

app_name = "cars"
urlpatterns = [ path("", CarsListView.as_view(), name="list"),
                path("create/", CarsCreateView.as_view(), name="create"),
                path("<str:slug>/", CarsDetailView.as_view(), name="detail"),
                path("<str:slug>/update/", CarsUpdateView.as_view(), name="update"),
                path("<str:slug>/delete/", CarsDeleteView.as_view(), name="delete"),
                ]
