from django.contrib import admin
from .models import Image,  Profile,Location
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags')

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Location)
