from django.contrib import admin
from .models import Room, Message

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ()

admin.site.register(Room, RoomAdmin)
admin.site.register(Message, RoomAdmin)
