from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} (Floor {self.floor}, Room {self.room_number})"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.IntegerField(help_text="Duration in minutes")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='meetings')

    def __str__(self):
        return f"{self.title} on {self.date} from {self.start_time} for {self.duration} minutes in {self.room.name}"


