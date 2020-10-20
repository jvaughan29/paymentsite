from django.db import models
import random
from datetime import datetime, date

class Type(models.Model):
   type = models.CharField('Type', max_length=20)
   def __str__(self):
      return self.type

class Location(models.Model):
   location = models.CharField('Location', max_length=20)
   def __str__(self):
      return self.location

def random_string():
   return str(random.randint(100000, 999999))

class PaymentEntry(models.Model):
   name_text = models.CharField('Patient Name', max_length=200)
   labid_text = models.CharField('Invoice Number', max_length=9)
   amount_double = models.FloatField('Amount')
   type = models.ForeignKey(Type, on_delete=models.CASCADE)
   location = models.ForeignKey(Location, on_delete=models.CASCADE)
   staff_code = models.CharField('Staff Code',max_length=7)
   entry_date = models.DateTimeField(auto_now_add=True)
   receipt_number = models.CharField(default = random_string, max_length=7)
   def __str__(self):
      return self.labid_text



