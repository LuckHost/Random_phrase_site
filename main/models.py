from django.db import models

# Create your models here.
class Words(models.Model):
    word = models.CharField(max_length=20, blank = False)
    mood_type = models.CharField(max_length=20, blank = False)
    part_of_speech = models.CharField(max_length=20, blank = False)
    alive = models.BooleanField()
    
    def __str__(self):
        return self.word
    
    
