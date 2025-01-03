# forms.py
from django import forms
from .models import HomePage, CarouselImage, JourneyHighlight

class HomePageForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = '__all__'

class CarouselImageForm(forms.ModelForm):
    class Meta:
        model = CarouselImage
        fields = ['image']

class JourneyHighlightForm(forms.ModelForm):
    class Meta:
        model = JourneyHighlight
        fields = '__all__'