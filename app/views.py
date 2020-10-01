from django.shortcuts import render
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test,login_required
from .models import Property

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
    
class PropertiesView(generic.ListView):
    model = Property
    template_name = 'app/properties.html'
    context_object_name = 'properties'
    
class PropertiesDetailView(generic.DetailView):
    """ This class displays the details of the property """
    model = Property
    
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['props'] = [super().get_object()]
        return context