from django.contrib import admin
from .models import Post, Photo

# Register your models here.
class PhotoInline(admin.TabularInline) :
  model = Photo

class PostAdmin(admin.ModelAdmin) :
  inlines = [PhotoInline, ]

admin.site.register(Post, PostAdmin)