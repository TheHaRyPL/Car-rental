import datetime

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
    mark = models.TextField(verbose_name=_("Mark"), null=True, blank=True)
    power = models.TextField(verbose_name=_("Power"), null=True, blank=True)
    type = models.TextField(verbose_name=_("Type"), null=True, blank=True)
    price = models.TextField(verbose_name=_("Price"), null=True, blank=True)
    picture = models.URLField(verbose_name=_("Picture"), null=True, blank=True)

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
