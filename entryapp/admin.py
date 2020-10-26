from django.contrib import admin

from .models import PaymentEntry
from .models import Location


admin.site.register(PaymentEntry)
admin.site.register(Location)
