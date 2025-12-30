from django import forms
from .models import Meeting
import datetime


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        # Fields aligned with the Meeting model definition
        fields = ['title', 'description', 'date', 'start_time','duration', 'room']

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
        if duration is not None and duration <= 0:
            raise forms.ValidationError("Duration must be a positive number!")
        return duration
    
    def clean_room(self):
        room = self.cleaned_data.get('room')
        if room is None:
            raise forms.ValidationError("Room selection is required!")
        return room

      