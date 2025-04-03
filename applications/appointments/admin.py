from django.contrib import admin
from applications.appointments.models import rendezvous
# Register your models here.


@admin.register(rendezvous)
class RendezvousAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date')
    
    