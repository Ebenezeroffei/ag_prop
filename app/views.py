from django.shortcuts import render
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test,login_required

# Create your views here.
class IndexView(generic.View):
    template_name = 'app/index.html'
    
    def dispatch(self,request,*args,**kwargs):
        return render(request,self.template_name)
    
    
class AdminIndexView(generic.View):
    template_name = 'app/admin_base.html'
    
    @method_decorator(login_required(login_url = '/admin/signin/'))
    @method_decorator(user_passes_test(lambda x : x.is_superuser))
    def dispatch(self,request,*args,**kwargs):
        return render(request,self.template_name)
    
