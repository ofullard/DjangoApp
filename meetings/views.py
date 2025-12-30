from django.shortcuts import render, redirect, get_object_or_404
from .models import Meeting
from .forms import MeetingForm

# Create your views here.

def home(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings/home.html', {'meetings': meetings})

def meeting_detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/meeting_detail.html', {'meeting': meeting})    

def create_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MeetingForm()
    return render(request, 'meetings/create_meeting.html', {'form': form})