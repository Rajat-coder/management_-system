from pyexpat import model
import re
from django.db import models
import uuid
from django.utils import timezone
# Create your models here.


class SpecializationModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self) :
        return self.name

class AssociatesMasterModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    address = models.TextField(null=True,blank=True)
    specialization = models.ManyToManyField(SpecializationModel)

    def __str__(self) :
        return str(self.name) + str(self.specialization.name)

