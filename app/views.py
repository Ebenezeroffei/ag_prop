from django.shortcuts import render
from django.views import generic

# Create your views here.
class IndexView(generic.View):
    template_name = 'app/base.html'
    
    def dispatch(self,request,*args,**kwargs):
        return render(request,self.template_name)
