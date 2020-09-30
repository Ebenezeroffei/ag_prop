from django.urls import path
from . import views as blog_views


app_name = 'blog'
urlpatterns = [
    path('blog/',blog_views.IndexView.as_view(),name = 'home'),
    path('blog/<int:pk>/',blog_views.BlogDetailView.as_view(),name = 'detail'),
    path('blog/create/',blog_views.BlogCreateView.as_view(),name = 'create'),
    path('blog/<int:pk>/edit/',blog_views.BlogEditView.as_view(),name = 'edit'),
    path('admin/blog/',blog_views.AdminBlogIndexView.as_view(),name = 'admin_home'),
    path('blog/delete/',blog_views.DeleteBlogView.as_view(),name = 'delete'),
]