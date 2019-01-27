from django.contrib import admin

# Register your models here.
from .models import Join

class JoinAdmin(admin.ModelAdmin):
	list_display=['email','ref_id','friend','ip_address','timestamp','updated']

admin.site.register(Join,JoinAdmin)