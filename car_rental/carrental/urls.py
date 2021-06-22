from django.urls import path
from carrental.views import (
    CarsListView, CarsCreateView, CarsDeleteView, CarsDetailView, CarsUpdateView,
    ReservationListView, ReservationCreateView,RentalCreateView,RentalListView)

app_name = "cars"
urlpatterns = [path("", CarsListView.as_view(), name="list"),

               path("reservations/", ReservationListView.as_view(), name="reservation_list"),
               path("create_reservation/", ReservationCreateView.as_view(), name="create_reservation"),

               path("rentals/", RentalListView.as_view(), name="rental_list"),
               path("create_rental/", RentalCreateView.as_view(), name="create_rental"),

               path("create/", CarsCreateView.as_view(), name="create"),
               path("<str:slug>/", CarsDetailView.as_view(), name="detail"),
               path("<str:slug>/update/", CarsUpdateView.as_view(), name="update"),
               path("<str:slug>/delete/", CarsDeleteView.as_view(), name="delete"),
               ]
