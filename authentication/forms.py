from django import forms
import datetime
from authentication.models import AssociatesMasterModel,SpecializationModel



class AssociatesMasterkForm(forms.ModelForm):
    specialization = forms.ModelMultipleChoiceField(queryset=SpecializationModel.objects.all(),label = "SPECIALIZATION")
    class Meta:
        model = AssociatesMasterModel
        exclude = ("id",)
        labels = {
            'name':'NAME',
            'phone':'PHONE NUMBER',
            'address':'ADDRESS'
        } 