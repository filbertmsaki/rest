from django.db import models

# Create your models here.
class Light(models.Model):
    state_choices = (
        ('off', 'off'),
        ('on', 'on')
    )

    name = models.CharField(max_length=10, blank=True, null=True)
    state = models.CharField(max_length=10, choices=state_choices, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

class Road(models.Model):
    direction_choice = (
        ('R', 'Right to left'),
        ('L', 'Left to right'),
        ('U', 'Up to down'),
        ('D', 'down to up'),
    )
    road_status = (
        ('A', 'Available'),
        ('M', 'Maintenance'),
        ('R', 'Restricted'),
    )
    name = models.CharField(max_length=20, help_text="The road name", null=True, blank=True)
    distance = models.FloatField(help_text="The distance of the road", null=True, blank=True)
    direction = models.CharField(max_length=2, help_text="The direction of the road",choices=direction_choice)
    traffic_queue = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=2, blank=True, null=True, help_text="Road status availability", default='A')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
