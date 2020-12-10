from django.contrib import admin
from .models import Notification

# Register your models here.
class Filter(admin.ModelAdmin):
    search_fields=('case',)
    list_display=('case','is_read','is_Accepted',)
    list_filter = ("received_at","is_read",'is_Accepted',)

admin.site.register(Notification, Filter)