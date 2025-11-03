from django.contrib import admin
from .models import Brief, BriefImage
from django.db.models import Count

@admin.register(Brief)
class BriefAdmin(admin.ModelAdmin):
    list_display = ['company', 'count']
    def count(self, obj):
        return obj.bid_set.count()

@admin.register(BriefImage)
class BriefAdmin(admin.ModelAdmin):
    list_display = ['brief']