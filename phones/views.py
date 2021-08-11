from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .forms import PhoneCreateForm
from .models import Phone


# Create your views here.
class PhonesView(ListView):
    template_name = 'phoneview_list.html'

    def get_queryset(self):
        queryset = Phone.objects.all()
        return queryset


class CreatePhoneView(CreateView):
    form_class = PhoneCreateForm
    template_name = 'createphone.html'
    success_url = '/'


class DeletePhoneView(DeleteView):
    model = Phone
    success_url = '/'


class UpdatePhoneView(UpdateView):
    template_name = 'updatephone.html'
    model = Phone
    fields = [
        'name',
        'phone_number',
        'location',
    ]
    success_url = '/'
