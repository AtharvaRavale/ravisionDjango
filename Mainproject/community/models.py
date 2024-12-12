from django.db import models
from datetime import datetime

# Create your models here.
"""
contributor
motive
group
group  contributor
intialier group

"""
class MotiveType(models.TextChoices):
    Social_cause='Social cause','Social cause'
    Environmental='Environmental','Environmental'
    Educational='educational','educational'
    Medical='Medical','Medical'
    Charity='Charity','Charity'
    Other='Other','Other'




class Motive(models.Model):
    name =models.CharField(max_length=40,unique=True)
    logo=models.ImageField()
    motive_type=models.CharField(max_length=50,choices=MotiveType.choices,default=MotiveType.Social_cause,null=False)
    description=models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=False)
    update_at= models.DateTimeField(auto_now_add=False)
 



class group(models.Model):
    group_name =models.CharField(max_length=100,default='',null=False)
    group_description=models.CharField(max_length=100,default='helpfull',null=False)
    created_at = models.DateTimeField(auto_now_add=True)






