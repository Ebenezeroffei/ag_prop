from django.contrib import admin
from .models import Property,ExteriorFeatures,InteriorFeatures

# Register your models here.
admin.site.register(Property)
admin.site.register(ExteriorFeatures)
admin.site.register(InteriorFeatures)