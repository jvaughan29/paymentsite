from django.db import models

class PaymentEntry(models.Model):
   name_text = models.CharField(max_length=200)
   labid_text = models.CharField(max_length=9)
   amount_text = models.CharField(max_length=200)
   type_text = models.CharField(max_length=200)
   location_text = models.CharField(max_length=200)
   def __str__(self):
      return self.labid_text