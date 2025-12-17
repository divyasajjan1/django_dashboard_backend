from django.contrib import admin
from .models import TeamDC, TeamMarvel

# Register your models here.
admin.site.register([TeamDC, TeamMarvel])