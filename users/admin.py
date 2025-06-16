from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Add fields you want to display in the admin interface
    list_display = ['username', 'email', 'first_name', 'last_name' , 'is_staff']
    search_fields = ['username', 'email']  # Required for autocomplete_fields


    @admin.register(Message)
    class MessageAdmin(admin.ModelAdmin):
        list_display = ['id', 'sender', 'subject', 'sent_at']
        search_fields = ['subject', 'body', 'sender__username', ]
        list_filter = ['sent_at']
        readonly_fields = ['sent_at']