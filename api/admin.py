from django.contrib import admin
from .models import Ride, Rider, Request, Requester
# Register your models here..

# class RiderAdmin(admin.ModelAdmin):
#     list_display=('id',)
#     # search_fields=('name',)   
    
# class RequsterAdmin(admin.ModelAdmin):
#     list_display=('id',)
#     # list_filter=('company',)

# class RideAdmin (admin.ModelAdmin):
#     list_display=('id',)
#     # list_filter=('id',)

# class RequestAdmin (admin.ModelAdmin): 
#     list_display=('id',)
#     # list_filter=('company',)

# admin.site.register(Requester, RequsterAdmin)
# admin.site.register(Rider,RiderAdmin)
# admin.site.register (Request, RequestAdmin)
# admin.site.register (Ride, RideAdmin)

admin.site.register (Ride)
admin.site.register (Rider)
admin.site.register (Request)
admin.site.register (Requester)

