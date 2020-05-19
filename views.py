from django.shortcuts import render
from donation.form import donationCreationForm
# Create your views here.

def show_form(request):
    form = donationCreationForm()
    return render(request, 'template.html', {'form': form})