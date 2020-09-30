from django.urls import path
from . import views as user_views

app_name = 'user'
urlpatterns = [
    path('signin/',user_views.LoginUserView.as_view(),name = 'signin'),
    path('signup/',user_views.SignUpUserView.as_view(),name = 'signup'),
    path('admin/signin/',user_views.LoginAdminView.as_view(),name = 'signin_admin'),
    path('admin/logout/',user_views.LogoutAdminView.as_view(),name = 'logout_admin'),
    path('nice/',user_views.Nice.as_view(),name = 'nice'),
]