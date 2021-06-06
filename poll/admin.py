from django.contrib import admin
from .models import Option, Poll, Response
# Register your models here.

class InlineOption(admin.TabularInline):
    model = Option

class InlineResponse(admin.TabularInline):
    model = Response

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ['title', 'active_until', 'status']
    inlines = [InlineOption, ]

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['title', 'poll']
    inlines = [InlineResponse]