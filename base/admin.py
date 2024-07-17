from django.contrib import admin

from .models import Testimony, Executive, Event, audioMessage, picture

admin.site.register(Testimony)
admin.site.register(Executive)
admin.site.register(Event)
admin.site.register(audioMessage)
admin.site.register(picture)

# Register your models here.
