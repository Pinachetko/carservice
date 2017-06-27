from django.contrib import admin
from .models import Service, ServiceType, ServicedCar, MaterialUsed

# Register your models here.


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(ServicedCar)
class ServicedCarAdmin(admin.ModelAdmin):
    pass

@admin.register(MaterialUsed)
class MaterialUsedAdmin(admin.ModelAdmin):
    pass
