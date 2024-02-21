from django.contrib import admin
from .models import WeightEntry

@admin.register(WeightEntry)
class WeightEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'date')
    search_fields = ('user__username', 'weight', 'date')
    list_filter = ('user', 'date')