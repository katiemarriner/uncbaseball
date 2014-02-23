from django.db import models

# Player Model
class Player(models.Model):
    name = models.CharField(max_length=50)
    jersey = models.IntegerField(max_length=2)
    height = models.IntegerField(max_length=4)
    weight = models.IntegerField(max_length=3)
    previousschool = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    imgurl = models.URLField(null=True)
    position = models.CharField(max_length=5)
    hand = models.CharField(max_length=3)
    highschool = models.TextField()
    freshman = models.TextField(null=True)
    sophomore = models.TextField(null=True)
    junior = models.TextField(null=True)
    senior = models.TextField(null=True)
    # SHORTSTOP = 'SS'
    # PITCHER = 'PT'
    #POSITION_CHOICES = (
    #    (SHORTSTOP, 'Shortstop'),
    #    (PITCHER, 'Pitcher'),
    #)
    #position = models.CharField(max_length=2,
    #                            choices=POSITION_CHOICES)
    class Meta(object):
        ordering = ('jersey', 'name')
        
    def __unicode__(self):
        return U'%s %s' %(self.jersey, self.name)
    
class Staff(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    experience = models.IntegerField(max_length=2)