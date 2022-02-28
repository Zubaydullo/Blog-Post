from django.contrib import admin
from .models import Post, Category, Profile
from theblog.models import CustomUser

admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Profile)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}