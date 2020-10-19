from django.contrib import admin

from .models import PaymentEntry
from .models import Location
from .models import Type

admin.site.register(PaymentEntry)
admin.site.register(Location)
admin.site.register(Type)