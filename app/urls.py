from django.urls import path
from . import views as app_views

app_name = 'app'
urlpatterns = [
    path('',app_views.IndexView.as_view(),name = 'home'),
    path('admin/',app_views.AdminIndexView.as_view(),name = 'admin'),
    path('properties/',app_views.PropertiesView.as_view(),name = 'properties'),
    path('admin/properties/',app_views.AdminPropertiesView.as_view(),name = 'admin_properties'),
    path('property/create/',app_views.PropertiesCreateView.as_view(),name = 'property_create'),
    path('property/<int:pk>/edit/',app_views.PropertyEditView.as_view(),name = 'property_edit'),
    path('property/<pk>/detail/',app_views.PropertiesDetailView.as_view(),name = 'properties_detail'),
    path('property/delete/',app_views.DeletePropertyView.as_view(),name = 'property_delete'),
    path('admin/schedules/',app_views.SchedulesView.as_view(),name = 'schedules'),
    path('create/schedule/',app_views.CreateSheduleView.as_view(),name = 'create_schedule'),
    path('schedule/accept-or-reject/',app_views.AcceptOrRejectRequestView.as_view(),name = 'accept_or_reject_request')
]
