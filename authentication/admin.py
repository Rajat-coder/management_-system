from django.contrib import admin
from authentication.models import SpecializationModel,AssociatesMasterModel
from django.contrib.admin.sites import AlreadyRegistered, site
from django.apps import apps


for model in apps.get_app_config('authentication').get_models():
    try:
        admin.site.register(model)
    except AlreadyRegistered as e:
        pass