from django.contrib import admin
from .models import Deal

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    # Only include fields that actually exist in the Deal model
    list_display = ('title', 'deal_type', 'deal_price', 'start_date', 'end_date', 'is_active', 'created_at')
    list_filter = ('deal_type', 'is_active')
    search_fields = ('title',)
    ordering = ('-created_at',)
