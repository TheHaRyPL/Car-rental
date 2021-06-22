from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from carrental.models import Cars, Reservation, Rental
from carrental.forms import CarsForm, ReservationForm, RentalForm


class CarsListView(ListView):
    model = Cars
    paginate_by = 20

    context_object_name = "cars"


class CarsDetailView(DetailView):
    model = Cars


class CarsCreateView(CreateView):
    model = Cars
    form_class = CarsForm


class CarsDeleteView(DeleteView):
    model = Cars
    success_url = reverse_lazy("cars:list")


class CarsUpdateView(UpdateView):
    model = Cars
    form_class = CarsForm


class ReservationListView(ListView):
    model = Reservation
    paginate_by = 100

    context_object_name = "reservations"


class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm

    def get_form_kwargs(self):
        kwargs = super(ReservationCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class RentalListView(ListView):
    model = Rental

    context_object_name = "rentals"


class RentalCreateView(CreateView):
    model = Rental
    form_class = RentalForm
