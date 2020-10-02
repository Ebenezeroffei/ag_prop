from django.urls import path
from . import views as app_views

app_name = 'app'
urlpatterns = [
    path('',app_views.IndexView.as_view(),name = 'home'),
    path('admin/',app_views.AdminIndexView.as_view(),name = 'admin'),
    path('properties/',app_views.PropertiesView.as_view(),name = 'properties'),
    path('property/<pk>/detail/',app_views.PropertiesDetailView.as_view(),name = 'properties_detail'),
    path('create/schedule/',app_views.CreateSheduleView.as_view(),name = 'create_schedule')
]