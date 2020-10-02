from django.contrib import admin
from .models import Property,ExteriorFeatures,InteriorFeatures,ScheduleTour,ContactDetail

# Register your models here.
admin.site.register(Property)
admin.site.register(ExteriorFeatures)
admin.site.register(InteriorFeatures)
admin.site.register(ScheduleTour)
admin.site.register(ContactDetail)