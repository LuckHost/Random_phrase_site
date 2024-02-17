from django.db import models

# Create your models here.
class Rusnounsmorfs(models.Model):
    id = models.IntegerField(primary_key = True)
    word = models.CharField(max_length=60, blank = False)
    code = models.IntegerField(blank = False)
    code_parent = models.IntegerField(blank = False)
    plural = models.SmallIntegerField(blank=False)
    gender = models.CharField(max_length=3, blank = False)
    wcase = models.CharField(max_length=4, blank = False)
    soul = models.SmallIntegerField(blank=False)
    
    def __str__(self):
        return self.word
    
class Checkbox(models.Model):
    checkbox_model = models.BooleanField()