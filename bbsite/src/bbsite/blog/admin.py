from django.contrib import admin
from bbsite.blog.models import *
from django.template.defaultfilters import slugify
from datetime import datetime

class BlogEntryAdmin(admin.ModelAdmin):
    fields = ('author', 'title', 'editable_content', 'tags', 'comments_enabled', 'status')

    def save_model(self, request, obj, form, change):        
        if 'status' in request.POST and request.POST['status']:
            if int(request.POST['status']) == BlogStatus.is_published:
                # We're publishing, so gather timestamps and whatnot
                obj.pub_date = datetime.now()
        
        # setting the slug to be the title slugified
        if 'title' in request.POST and request.POST['title']:
            obj.slug = slugify(request.POST['title'])
            
        # saving the object to the database?
        obj.save()
        
    list_display = ('title', 'author', 'status', 'comments_enabled')
    list_filter = ('author', 'status')

admin.site.register(BlogEntry, BlogEntryAdmin)