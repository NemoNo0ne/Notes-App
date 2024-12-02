from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'created_at', 'updated_at')
    list_filter = ('priority', 'created_at')
    search_fields = ('title', 'connect')

