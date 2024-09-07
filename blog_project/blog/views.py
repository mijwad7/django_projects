from django.shortcuts import get_object_or_404, redirect, render
from .models import BlogPost
from django.views.decorators.http import require_POST
# Create your views here.
def index(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog/index.html', {
        'blogs': blogs
    })

def add_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        blog = BlogPost(title=title, content=content)
        blog.save()
        return redirect('index')

    return render(request, 'blog/add_blog.html')

@require_POST
def delete_blog(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    blog.delete()
    return redirect('index')
