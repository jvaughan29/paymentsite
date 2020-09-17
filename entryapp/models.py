from django.db import models

class PaymentEntry(models.Model):
   name_text = models.CharField('Patient Name', max_length=200)
   labid_text = models.CharField('Lab ID', max_length=9)
   amount_text = models.CharField('Amount', max_length=200)
   type_text = models.CharField('Type', max_length=200)
   location_text = models.CharField('Location', max_length=200)
   def __str__(self):
      return self.labid_text

   # to limit options for location and type (e.g. radio button or drop down list), create new models and referennce as foreign key
   #