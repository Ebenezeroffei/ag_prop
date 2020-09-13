from django.urls import path
from . import views as user_views

app_name = 'user'
urlpatterns = [
    path('signin/',user_views.LoginUserView.as_view(),name = 'signin'),
    path('signup/',user_views.SignUpUserView.as_view(),name = 'signup')
]