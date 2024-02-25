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
    
    def getPlural(self):
        return self.plural
    
    def getGender(self):
        return self.gender
    
    def __str__(self):
        return self.word
    
class Allwords(models.Model):
    id = models.IntegerField(primary_key = True)
    word = models.CharField(max_length=60, blank = False)
    code = models.IntegerField(blank = False)
    code_parent = models.IntegerField(blank = False)
    type = models.CharField(max_length=10, null = True)
    type_sub = models.CharField(max_length=10, null = True)
    type_ssub = models.CharField(max_length=10, null = True)
    plural = models.SmallIntegerField(null = True)
    gender = models.CharField(max_length=3, null = True)
    wcase = models.CharField(max_length=4, null = True)
    comp = models.CharField(max_length=5, null = True)
    soul = models.SmallIntegerField(null = True)
    transit = models.CharField(max_length=6, null = True)
    perfect = models.SmallIntegerField(null = True)
    face = models.CharField(max_length=4, null = True)
    kind = models.CharField(max_length=3, null = True)
    time = models.CharField(max_length=4, null = True)
    inf = models.SmallIntegerField(null = True)
    vozv = models.SmallIntegerField(null = True)
    nakl = models.CharField(max_length=5, null = True)
    short = models.SmallIntegerField(null = True)
    
    def getGender(self):
        return self.gender
    
    def __str__(self):
        return self.word
    
class Checkbox(models.Model):
    checkbox_model = models.BooleanField()