from django.contrib import admin
from .models import pro_skills, Nanny, Location

# Register your models here.
admin.site.register(pro_skills)
admin.site.register(Location)
admin.site.register(Nanny)
