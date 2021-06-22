import datetime
import wtforms
import wtforms.widgets
from cfgv import ValidationError
from django.forms import ModelForm, HiddenInput
from carrental.models import Cars, Reservation, Rental
from car_rental.users.models import User

class CarsForm(ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'

class ReservationForm(ModelForm):
    """Reservation model form"""
    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop('request')
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['cars'].queryset = Cars.objects.filter(quantity__gt=0)
        self.fields['user'].queryset = User.objects.filter(id=self.request.user.id)
        self.fields['user'].initial = User.objects.get(id=self.request.user.id)
        self.fields['user'].widget = HiddenInput()

    class Meta:
        model = Reservation
        fields = ['cars', 'user']

class RentalForm(ModelForm):
    """Rental model form"""
    def __init__(self, *args, **kwargs):

        super(RentalForm, self).__init__(*args, **kwargs)
        self.fields['return_helper'].widget = HiddenInput()
        self.fields['reservation'].queryset = Reservation.objects.filter(isrented=False)

    class Meta:
        model = Rental
        fields = ['reservation', 'return_helper', 'isreturned']
