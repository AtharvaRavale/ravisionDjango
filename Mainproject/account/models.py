from django.db import models
from django.contrib.auth.models import AbstractUser
gender_choice=[
    ('M','Male'),
    ('F','Female')

]
from datetime import date


class Contributor(AbstractUser):
    contact_details=models.CharField(max_length=15,default='',null=False)
    d_o_b=models.DateField(default='',null=False)
    gender=models.CharField(max_length=2,choices=gender_choice,default='M')
    def save(self,*args,**kwargs):
        if kwargs.get('commit')==False:
            self.d_o_b=date.today()
            user=super().save(*args,**kwargs)
        else:
            self.d_o_b=date.today()
            user=super().save(*args,**kwargs)
        return user



    class Meta:
        db_table='contributor'



class Address(models.Model):
    contributor =models.ForeignKey(Contributor,on_delete=models.DO_NOTHING)
    address_line_one=models.CharField(max_length=100,default='',null=False)
    address_line_two=models.CharField(max_length=100,default='',null=True)
    street=models.CharField(max_length=100,default='',null=True)
    area=models.CharField(max_length=100,default='',null=False)
    city=models.CharField(max_length=100,default='',null=False)
    state=models.CharField(max_length=100,default='',null=False)
    country=models.CharField(max_length=100,default='',null=False)











