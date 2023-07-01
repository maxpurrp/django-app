from django.contrib import admin
from . import models

admin.site.register(models.Workouts_gym)
admin.site.register(models.Workouts_swimming)
admin.site.register(models.Workouts_swimming_pro)
admin.site.register(models.Registrations)

