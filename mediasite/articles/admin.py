from django.contrib import admin

# Register your models here.

from articles.models import Post, PostAdmin, Comment, Author, Category

class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
