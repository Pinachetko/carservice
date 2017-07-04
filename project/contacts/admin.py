from django.contrib import admin
from .models import  Message
# from .models import  smsSendingSetting
# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass

# @admin.register(smsSendingSetting)
# class smsSendingSettingAdmin(admin.ModelAdmin):
#     pass
