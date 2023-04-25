from django.contrib import admin
# from.models import UploadImage
# # Register your models here.
# admin.site.register(UploadImage)

from .models import Image

class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]

admin.site.register(Image, imageAdmin)
