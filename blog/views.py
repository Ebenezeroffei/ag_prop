from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.http import JsonResponse
from .models import Blog

# Create your views here.
class IndexView(generic.ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'
    
class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['blogs'] = Blog.objects.exclude(id = super().get_object().id)
        return context

# Don't forget to add some mixins
class BlogCreateView(generic.CreateView):
    """ This class is used to create a new blog """
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title','image','content']
    
# Don't forget to add some mixins
class BlogEditView(generic.UpdateView):
    """ This class is used to create a new blog """
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title','image','content']
    
# Don't forget to add some admin mixins
class AdminBlogIndexView(generic.ListView):
    """ This class is responsible for showing all the blogs created by the user """
    model = Blog
    template_name = 'blog/admin_index.html'
    context_object_name = 'blogs'
    
class DeleteBlogView(generic.View):
    """ This class is responsible for deleting a blog """
    
    def get(self,request,*args,**kwargs):
        blog_id = int(request.GET.get('blogId'))
        blog = get_object_or_404(Blog,id = blog_id)
        img_path = blog.image.path
        # Delete Blog
        blog.delete()
        # Delete Image from the disk
        import os
        os.remove(img_path)
        data = {'count': Blog.objects.count()}
        return JsonResponse(data)
    
    
