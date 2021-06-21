import datetime
from cfgv import ValidationError
from django.forms import ModelForm
from carrental.models import Cars
from car_rental.users.models import User

class CarsForm(ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'
