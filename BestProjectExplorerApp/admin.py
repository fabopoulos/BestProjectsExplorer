from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Project)
admin.site.register(Site)
admin.site.register(Waypoint)

admin.site.register(Output)
admin.site.register(Indicator)
admin.site.register(Activity)
admin.site.register(ActivityPlanned)

