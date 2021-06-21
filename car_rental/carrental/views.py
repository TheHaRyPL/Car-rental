from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from carrental.models import Cars
from carrental.forms import CarsForm

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

