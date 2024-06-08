from django.contrib import admin
from .models import Screenshot, Session



class ScreenshotInline(admin.TabularInline):
  model = Screenshot
  list_display = ["screenshot", "created"]
  readonly_fields = ["screenshot", "created"]
  # classes = ['collapse']
  extra = 1
  max_num = 1



class SessionAdmin(admin.ModelAdmin):
  inlines = [ScreenshotInline]
  fields = ["user", "domain", "machine", "ip", "start_activity", "last_activity", "get_screenshots"]
  list_display = ["user", "domain", "machine", "ip", "start_activity", "last_activity"]
  readonly_fields = ["user", "domain", "machine", "ip", "start_activity", "last_activity"]
  search_fields = ["domain", "machine", "ip", "user"]
  # list_per_page = 30
 
  def has_add_permission(self, request, obj=None):
    return False




admin.site.register(Session, SessionAdmin)

