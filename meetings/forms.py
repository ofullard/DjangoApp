from django import forms
from .models import Meeting
import datetime


class MeetingForm(forms.ModelForm):
    # Duration choices: 0, 30, 60, 90, 120 minutes (up to 2 hours)
    duration = forms.ChoiceField(
        choices=[(i, f"{i} minutes") for i in range(0, 121, 30)],
        widget=forms.Select(),
        required=True
    )

    class Meta:
        model = Meeting
        # Fields aligned with the Meeting model definition
        fields = ['title', 'description', 'date', 'start_time', 'duration', 'room']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'room': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date

    def clean_start_time(self):
        start_time = self.cleaned_data.get('start_time')
        if start_time is None:
            raise forms.ValidationError("Start time is required!")
        return start_time

    def clean_duration(self):
        duration = self.cleaned_data.get('duration')
        if duration is not None:
            try:
                duration_int = int(duration)
                if duration_int < 0:
                    raise forms.ValidationError("Duration cannot be negative!")
                self.cleaned_data['duration'] = duration_int
            except (ValueError, TypeError):
                raise forms.ValidationError("Invalid duration value!")
        return self.cleaned_data.get('duration')

    def clean_room(self):
        room = self.cleaned_data.get('room')
        if room is None:
            raise forms.ValidationError("Room selection is required!")
        return room