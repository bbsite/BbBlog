from bbsite.blog.models import BlogEntry, BlogStatus
from django.shortcuts import render_to_response
from django.http import Http404

def list_draft_blogs(request):
    b = BlogEntry.objects.filter(status=BlogStatus.is_draft)
    return render_to_response('blogs.html', {'blogs': b})

def list_published_blogs(request):
    b = BlogEntry.objects.filter(status=BlogStatus.is_published)
    return render_to_response('blogs.html', {'blogs': b})

def show_published_blog(request, blog_title):
    # we try to get the blog with the slug supplied
    try:
        b = BlogEntry.objects.filter(slug=blog_title)[0:1].get()
    
    # if it doesn't exist, we throw a 404
    except BlogEntry.DoesNotExist:
        raise Http404
    
    # otherwise we return the blog
    return render_to_response('blog.html', {'blog': b})