from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

#The decorator is how we register a class, compared to just registering the standard model as we did before. 
# When we use a class, we register it with a decorator that is more Pythonic and allows us to customise how 
# the models we are registering will appear on the admin site.
@admin.register(Post)

#This code will give your admin panel greater functionality and clarity. We'll discuss this in more detail soon.

class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'content')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Comment)
