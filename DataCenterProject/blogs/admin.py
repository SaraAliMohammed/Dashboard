from django.contrib import admin

# Register your models here.

from .models import Server , Mac, Rack

class ServerAdmin(admin.ModelAdmin):
    list_display = ["name","Type" , "RAM" , "Core" , "Storage" , "Rac"]

    def Rac(self, obj):
        return obj.RackNum.RackNum

    class Meta:
        model=Server

class MacAdmin(admin.ModelAdmin):
    list_display = ["ServerID" , "MacNum"]
    class Meta:
        model=Mac

class RacAdmin(admin.ModelAdmin):
    list_display = ["RackNum"]
    class Meta:
        model=Rack

admin.site.register(Server,ServerAdmin)
admin.site.register(Mac,MacAdmin)
admin.site.register(Rack,RacAdmin)