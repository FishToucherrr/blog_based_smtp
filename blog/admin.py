from django.contrib import admin
from .models import Post,Category,Tag,Comment,Post_tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category']
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
class CommentAdmin(admin.ModelAdmin):
    list_display =['name','post','created_time']
    fields = ['name','text','post']

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Post_tag)
