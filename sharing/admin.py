from django.contrib import admin
from .models import Post, Photo, Tag 

# Register your models here.
admin.site.register(Post)

class PhotoInline(admin.TabularInline) :
  model = Photo

class PostAdmin(admin.ModelAdmin) :
  inlines = [PhotoInline, ]

class TagAdmin(admin.ModelAdmin) :
  prepopulated_fields = {'slug':('name', )}

admin.site.register(Tag, TagAdmin)