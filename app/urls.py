from django.urls import path
from . import views as app_views

app_name = 'app'
urlpatterns = [
    path('',app_views.IndexView.as_view(),name = 'home'),
    path('admin/',app_views.AdminIndexView.as_view(),name = 'admin'),
]