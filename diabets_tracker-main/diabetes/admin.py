from django.contrib import admin

# Register your models here.
from .models import Diet, Bloodsugar, Appointment, Food, Weight, Exercisecalorie, Exercise


admin.site.register (Food)
admin.site.register (Diet)
admin.site.register (Weight)
admin.site.register (Bloodsugar)
admin.site.register (Appointment)
admin.site.register (Exercisecalorie)
admin.site.register (Exercise)
