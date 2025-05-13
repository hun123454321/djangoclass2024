from django.contrib import admin
from .models import Post, Category

from .models import Post

admin.site.register(Post)
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Category,CategoryAdmin)
