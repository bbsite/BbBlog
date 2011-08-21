from bbsite.blog.models import BlogEntry, BlogStatus
from django.shortcuts import render_to_response
from django.http import Http404
from django.core.context_processors import csrf

def list_draft_blogs(request):
    b = BlogEntry.objects.filter(status=BlogStatus.is_draft)
    return render_to_response('blogs.html', {'blogs': b})

def list_published_blogs(request):
    b = BlogEntry.objects.filter(status=BlogStatus.is_published).order_by('-pub_date')
    return render_to_response('blogs.html', {'blogs': b})

def show_published_blog(request, blog_title):
    # we try to get the blog with the slug supplied
    try:
        b = BlogEntry.objects.filter(slug=blog_title)[0:1].get()
    
    # if it doesn't exist, we throw a 404
    except BlogEntry.DoesNotExist:
        raise Http404
    
    c = {'blog': b}
    c.update(csrf(request))
    
    # otherwise we return the blog
    return render_to_response('blog.html', c)