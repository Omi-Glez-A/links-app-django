from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Link, Video

# Register your models here.
class MiModeloAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Link)
admin.site.register(Video)