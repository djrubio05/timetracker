from django import forms

from .models import TimeEntry


class TimeEntryForm(forms.ModelForm):
    class Meta:
        model = TimeEntry
        fields = ["description", "worked_hours"]
        widgets = {
            "description": forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            "worked_hours": forms.NumberInput(attrs={'step': '0.5'}),
        }
