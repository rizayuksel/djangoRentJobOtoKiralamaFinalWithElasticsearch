from django import forms
from .models import Rent

class RentForm(forms.ModelForm): #Bu kez Model Formları kullanacağız
    class Meta:
        model = Rent
        fields = ["rentedCar","rentalDate","totalDays"]

        