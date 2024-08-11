from django import forms
from .models import ParkingImage


class ParkingImageForm(forms.ModelForm):
    class Meta:
        model = ParkingImage
        fields = ['image']

