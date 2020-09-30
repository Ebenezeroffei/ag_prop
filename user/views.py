from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
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
    
class LoginAdminView(generic.View):
    """ This form is reponsible for signing in the admin """
    
    def get(self,request,*args,**kwargs):
        return render(request,'user/admin_signin.html')
    
    def post(self,request,*args,**kwargs):
        context = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user and user.is_superuser:
            login(request,user)
            return HttpResponseRedirect(reverse('app:admin'))
        elif user and not user.is_superuser:
            context['error'] = 'You are not an admin.'
        else:
            context['error'] = 'Invalid credentials. Try again.'
        print(user)
        return render(request,'user/admin_signin.html',context)
    

class LogoutAdminView(generic.View):
    """ This class logsout the admin """
    
    def dispatch(self,request,*args,**kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('user:signin_admin'))
    
class Nice(generic.View):
#    @method_decorator(csrf_exempt)
    def get(self,request,*args,**kwargs):
        print(request.GET.get('username'))
        print("I am a get request")
        response = JsonResponse(data = {'hello':'world'})
        response["Access-Control-Allow-Origin"] = "http://localhost:8080"
#        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
#        response["Access-Control-Max-Age"] = "1000"
#        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response
    
#    @method_decorator(csrf_exempt)
    def post(self,request,*args,**kwargs):
        print(request.POST.get('username'))
        print("I am a post request")
        return JsonResponse({'hello':'world'})