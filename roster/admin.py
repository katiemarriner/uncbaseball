from django.contrib import admin
from roster.models import Player, Coach

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    
admin.site.register(Player, PlayerAdmin)

class CoachAdmin(admin.ModelAdmin):
    search_fields =('name',)
    
admin.site.register(Coach, CoachAdmin)