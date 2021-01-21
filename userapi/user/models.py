from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    dob = models.DateField(_("Date of Birth:"))
    city = models.CharField(max_length=50)
    phone = models.CharField(_("Phone Number:"), max_length=50)

    def __str__(self):
        return f'{self.fname} {self.lname}'
