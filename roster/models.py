from django.db import models

# Player Model
class Player(models.Model):
    name = models.CharField(max_length=50)
    jersey = models.IntegerField(max_length=2)
    height = models.CharField(max_length=4)
    weight = models.IntegerField(max_length=3)
    previousschool = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    imgurl = models.URLField(blank=True)
    position = models.CharField(max_length=6)
    hand = models.CharField(max_length=3)
    highschool = models.TextField()
    freshman = models.TextField(blank=True)
    sophomore = models.TextField(blank=True)
    junior = models.TextField(blank=True)
    senior = models.TextField(blank=True)
    twitterId = models.CharField(null=True, max_length=50)
    twitter = models.CharField(null=True, max_length=50)
    #major = models.CharField(max_length=100)
    class Meta(object):
        verbose_name_plural = "Players"
        ordering = ('jersey', 'name')
        
    def __unicode__(self):
        return U'%s %s' %(self.jersey, self.name)
    
class Coach(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    
    class Meta(object):
        verbose_name_plural = "Coaches"
        ordering = ('name', 'position')