from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import AbstractUser
# Create your models here.


class donation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    rupees = models.IntegerField
    EMAIL_ME_A_RECEIPT=models.BooleanField("EMAIL ME A RECEIPT",default=True)
    GIVE_ANONYMOUSLY=models.BooleanField("GIVE ANONYMOUSLY",default=False)
    ADD_ME_TO_EMAIL_LIST=models.BooleanField("ADD ME TO EMAIL LIST",default=False)
