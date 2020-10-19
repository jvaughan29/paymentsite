from django.db import models
from datetime import datetime, date

class Type(models.Model):
   type = models.CharField('Type', max_length=20)
   def __str__(self):
      return self.type

class Location(models.Model):
   location = models.CharField('Location', max_length=20)
   def __str__(self):
      return self.location

class PaymentEntry(models.Model):
   name_text = models.CharField('Patient Name', max_length=200)
   labid_text = models.CharField('Invoice Number', max_length=9)
   amount_double = models.FloatField('Amount')
   type = models.ForeignKey(Type, on_delete=models.CASCADE)
   location = models.ForeignKey(Location, on_delete=models.CASCADE)
   entry_date = models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return self.labid_text



   # to limit options for location and type (e.g. radio button or drop down list), create new models and reference as foreign key
   #