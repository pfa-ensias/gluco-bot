from django import forms
from .models import Appointment, Diet, Bloodsugar, Weight, Exercise
from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'appointmenttime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        exclude = ["user"]

        labels = {
            'appointmenttime': 'Appointment Time (mm/dd/yyyy hh:mm)'


        }


class DietForm(forms.ModelForm):
    class Meta:
        model = Diet

        fields = '__all__'
        exclude = ["user"]
        widgets = {
            'recordtime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'quantity': 'Quantity (Per 100g)',
            'recordtime': 'Record Time (mm/dd/yyyy)',
        }


class BloodsugarForm(forms.ModelForm):
    class Meta:
        model = Bloodsugar
        exclude = ["user"]
        fields = '__all__'
        widgets = {
            'measuretime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'bloodsugarmeasure': 'Blood Sugar Measurement (mmol/L)',
            'measuretime':'Measurement Time (mm/dd/yyyy)',
        }

class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        exclude = ["user"]
        fields = '__all__'
        widgets = {
            'measuretime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'weight': 'Weight Measurement (Kg)',
            'measuretime': 'Measurement Time (mm/dd/yyyy)',
        }


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        exclude = ["user","updated","totalcalories"]
        widgets = {
            'exercisedate': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        fields = '__all__'
        labels = {
            'exercise': 'Exercise Name',
            'currentweight': 'Current Weight (Kg)',
            'exercisedate': 'Exercise Date (mm/dd/yyyy)',
        }


