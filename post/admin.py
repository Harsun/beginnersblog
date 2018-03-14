from django.contrib import admin

# Register your models here.

from .models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'pubdate', 'update','slug',]
    list_display_links = ['title', 'pubdate', 'update',]
    list_filter = ['title', 'pubdate', 'update',]
    search_fields = ['title', 'content',]

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)

