from django.shortcuts import render
from authentication.models import AssociatesMasterModel
from django.views import View
from django.contrib import messages
from authentication.forms import AssociatesMasterkForm
from django.urls import  reverse
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect

# Create your views here.

def homepage(request):
    if request.GET.get("search",False):
        ass_obj = AssociatesMasterModel.objects.filter(name__icontains = request.GET['search'])
    else:
        ass_obj = AssociatesMasterModel.objects.all()
    context = {
        "obj":ass_obj
    }
    return render(request,'homepage.html',context)

class AssociatesMasterkView(View):
    def post(self,request):
        form_obj = AssociatesMasterkForm(request.POST or None)
        if form_obj.is_valid():
            data = form_obj.save(commit=False)
            data.save()
            messages.success(request, ' Added Associate Succesfully')
            return HttpResponseRedirect(reverse("authentication:associate"))
        else:
            soup = BeautifulSoup(str(form_obj.errors), 'html.parser')
            ui_find = soup.find('ul', class_='errorlist')
            split_details = list(ui_find.stripped_strings)
            messages.error(request, split_details)
            return render(request, 'associates.html', {'form': form_obj})

    def get(self,request):
        form_obj = AssociatesMasterkForm()
        return render(request, 'associates.html', {'form': form_obj})

class UpdateAssociatesView(View):
    def post(self, request, *args, **kwargs):
        ass_obj = AssociatesMasterModel.objects.get(serial=kwargs.get("serial"))
        form_obj = AssociatesMasterkForm(request.POST ,instance=ass_obj)
        if form_obj.is_valid():
            form_obj.save()
            messages.success(request, 'Associates Updated Succesfully')
            return HttpResponseRedirect(reverse("authentication:associate"))
        else:
            soup = BeautifulSoup(str(form_obj.errors), 'html.parser')
            ui_find = soup.find('ul', class_='errorlist')
            split_details = list(ui_find.stripped_strings)
            messages.error(request, split_details[1])
            return HttpResponseRedirect(reverse("authentication:associate"))

    def get(self, request, *args, **kwargs):
        trademark_obj = AssociatesMasterModel.objects.get(id=kwargs.get("id"))
        form_obj = AssociatesMasterkForm(instance=trademark_obj)
        return render(request, 'associates.html', {'form': form_obj})

class DeleteAssociatesView(View):
    def get(self, request, *args, **kwargs):
        try:
            AssociatesMasterModel.objects.filter(id=kwargs.get("id")).delete()
            return HttpResponseRedirect(reverse("authentication:homepage"))
        except:
            pass


