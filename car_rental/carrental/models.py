import datetime
import ast

from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from carrental.utils import generate_slug
from car_rental.users.models import User

class Cars(models.Model):
    """Cars model class"""
    title = models.CharField(max_length=256, verbose_name=_("Title"))
    slug = models.SlugField(max_length=256, unique=True, editable=False)
    mark = models.CharField(max_length=100, verbose_name=_("Mark"), null=True, blank=True)
    power = models.CharField(max_length=100, verbose_name=_("Power"), null=True, blank=True)
    type = models.CharField(max_length=100, verbose_name=_("Type"), null=True, blank=True)
    price = models.CharField(max_length=100, verbose_name=_("Price"), null=True, blank=True)
    picture = models.URLField(verbose_name=_("Picture"), null=True, blank=True)
    quantity = models.IntegerField(verbose_name=_("Quantity"), validators=[MinValueValidator(1), MaxValueValidator(1)])

    def save(self, *args, **kwargs):
        if not self.slug:
            base = self.title.strip()
            for candidate in generate_slug(base):
                if not Cars.objects.filter(slug=candidate).exists():
                    self.slug = candidate
                    break
            else:
                raise Exception("Can't create new Car object")

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Get url for Cars detail view.
        Returns:
            str: slug for Cars detail.
        """
        return reverse("cars:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

class Reservation(models.Model):
    """Reservation model class."""
    start_time_booking = models.DateField(editable=False)
    end_time_booking = models.DateField(editable=False)
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    isactive = models.BooleanField(default=True, blank=False)
    isrented = models.BooleanField(default=False, blank=False)

    @property
    def is_active(self):
        """Property to check if the reservation is still active.
        Checks whether 5 days have elapsed from the time of booking to today.

        Returns:
            bool

        """
        if datetime.date.today() < self.end_time_booking:
            return datetime.date.today() < self.end_time_booking
        elif (datetime.date.today() > self.end_time_booking) and self.isactive is True:
            self.isactive = False
            self.cars.quantity += 1
            self.save()
            self.cars.save()
            return datetime.date.today() < self.end_time_booking
        else:
            return datetime.date.today() < self.end_time_booking

    def save(self, *args, **kwargs):
        """ Custom save method for Reservation object. """
        if not self.pk:
            self.start_time_booking = datetime.date.today()
            self.end_time_booking = self.start_time_booking + datetime.timedelta(days=5)
            self.cars.quantity -= 1
            self.cars.save()
        return super(Reservation, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Get url for Reservation list view"""
        return reverse("cars:reservation_list")

    def __str__(self):
        return self.cars.title + ": " + self.user.username

class Rental(models.Model):
    """Rental model class"""
    start_time_rent = models.DateField(editable=False)
    end_time_rent = models.DateField(editable=False, blank=False, null=False)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, blank=False)
    isreturned = models.BooleanField(default=False, blank=False)
    return_helper = models.BooleanField(default=False, blank=False)

    @property
    def is_returned(self):
        """Property to check if the rented.
        Returns:
            bool.
        """
        if self.isreturned is True and self.return_helper is False:
            self.reservation.cars.quantity += 1
            self.return_helper = True
            self.save()
            self.reservation.cars.save()
            return self.isreturned
        else:
            return self.isreturned

    def save(self, *args, **kwargs):
        """ Custom save method for Rental object """
        if not self.pk:
            self.start_time_rent = datetime.date.today()
            self.end_time_rent = self.start_time_rent + datetime.timedelta(days=7)
            self.reservation.isrented = True
            self.reservation.save()
        return super(Rental, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Get url for Rental's list view."""
        return reverse("cars:rental_list")

    def __str__(self):
        return self.reservation.cars.title + ": " + self.reservation.user.username
