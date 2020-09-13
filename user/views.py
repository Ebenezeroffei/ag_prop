from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import SignUpUserForm

# Create your views here.

class LoginUserView(LoginView):
    """ This class signs in users """
    template_name = 'user/signin.html'
    
    def get_success_url(self,*args,**kwargs):
        return reverse('app:home')
    
class SignUpUserView(generic.View):
    """ This class creates a new accout for a user """
    form_class = SignUpUserForm
    template_name = 'user/signup.html'
    
    def get(self,request,*args,**kwargs):
        form = self.form_class()
        print("I am a get method")
        return render(request,self.template_name,{'form':form})
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Save valif form
            form.save()
            messages.success(request,f"Your account has been created. You can now signin")
            return HttpResponseRedirect(reverse('user:signin'))
        
        return render(request,self.template_name,{'form':form})