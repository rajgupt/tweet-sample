from django.contrib import admin
from .models import message, handle
from asyncio.events import Handle

# Register your models here.
class MessageInline(admin.StackedInline):
    model = message
    extra = 1


class HandleAdmin(admin.ModelAdmin):
    fields = ['value']
    inlines = [MessageInline]

admin.site.register(handle, HandleAdmin)

