from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Poll
from .models import Options
from .models import Response

class PollAdmin(admin.ModelAdmin):
  list_display = ("question", "active_until","status",)
  list_filter = ("status",)
  search_fields = ("question",)
  #fields = ('question',)
  
admin.site.register(Poll,PollAdmin)
admin.site.register(Options)
admin.site.register(Response)

class PollInline(admin.TabularInline):
  model = Poll


class ResponsAdmin(admin.ModelAdmin):
  inlines = (PollInline,)