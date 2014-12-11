from django.db import models
from django.contrib.auth.models import User
from annoying.fields import JSONField
# Create your models here.


class Shapefiler(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    # desc = models.CharField(max_length=500)
    # bBox = models.geom(null=True)
    file = models.FileField()


class UserLeaf(models.Model):
    COLOR_ARRAYS = (
        ('#f7fcf5,#e5f5e0,#c7e9c0,#a1d99b,#74c476,#41ab5d,#238b45,#005a32', 'Green'),
        ('#fff5f0,#fee0d2,#fcbba1,#fc9272,#fb6a4a,#ef3b2c,#cb181d,#99000d', 'Red'),
    )
    user = models.ForeignKey(User)
    shapefile = models.ForeignKey(Shapefiler, null=True)
    jsonstr = models.TextField(default="string cheese")
    fillClr = models.CharField(max_length=4000, default="Green", choices=COLOR_ARRAYS)
    weight = models.IntegerField(default=2)
    opac = models.FloatField(default=1)
    color = models.CharField(max_length=1000)
    dashArray = models.CharField(max_length=50, default=3)
    fillOpac = models.FloatField(default=.7)
    attributes = JSONField(blank=True, null=True)
    selectedattr = models.CharField(max_length=100, null=True, blank=True)

