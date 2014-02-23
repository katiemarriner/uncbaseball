from django.db import models

# Player Model
class Player(models.Model):
    name = models.CharField(max_length=50)
    jersey = models.IntegerField(max_length=2)
    # height = models.IntegerField()
    weight = models.IntegerField(max_length=3)
    highschool = models.CharField(max_length=100)
    about = models.TextField()
    imgurl = models.URLField()
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