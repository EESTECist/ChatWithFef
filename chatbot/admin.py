from django.contrib import admin
from chatbot.models import Message


@admin.register(Message)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "timestamp",
        "message"
    ]
