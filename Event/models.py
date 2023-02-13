from datetime import datetime
from django.db import models
from PIL import Image
from Person.models import Person 
from django.db.models.signals import post_save
from django.dispatch import receiver
class Event(models.Model):
    DESCRIPTION_CHOICES = (
        ('Musique', 'Musique'),
        ('Cinema', 'Cinema'),
        ('Sport', 'Sport')
    )
    title = models.CharField(default=False,max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='events/')
    state = models.BooleanField(default=False)
    
    nbe_participant = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=DESCRIPTION_CHOICES)
    evt_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    organizer=models.ForeignKey(   
        Person,
        on_delete=models.CASCADE
    )
    participations=models.ManyToManyField(  
         Person,
         related_name="participations",
         through="Participation"
    )

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(evt_date__gte=datetime.now()), name='Date doit être superieur au date systeme'),
        ]
        
    def __str__(self):
        return self.description

    """  @receiver(post_save, sender='Event.Participation')
    def increment_participation_count(sender, instance, created, **kwargs):
     if created:
        instance.event.nbe_participant += 1
        instance.event.save() """
class Participation(models.Model):
    participation_date = models.DateTimeField(auto_now_add=True)
    personne = models.ForeignKey(Person, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


    
class Meta:
    unique_together = ['person', 'event']