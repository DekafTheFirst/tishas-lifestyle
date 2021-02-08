from django.contrib import admin
from .models import Post, Comment, ImagePost, VideoPost

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class ImagePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','created_on', 'status')
    list_filter = ("status",)
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class VideoPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'status')
    list_filter = ("status",)
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Post, PostAdmin)
admin.site.register(ImagePost, ImagePostAdmin)
admin.site.register(VideoPost, VideoPostAdmin)
