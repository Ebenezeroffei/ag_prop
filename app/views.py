from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test,login_required
from .models import Property,ScheduleTour

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
    
    
class CreateSheduleView(generic.View):
    """ This class is responsible for creating a schedule """
    def get(self,request,*args,**kwargs):
        if request.GET.get('message') == 'confirm':
            date = request.GET.get('date')
            time = request.GET.get('time')
            print(date)
            print(time)
            data = {}
            if request.user.is_authenticated: # A user has logged in
                data['isLoggedIn'] = True
                data['name'] = f"{request.user.first_name} {request.user.last_name}" if request.user.first_name and request.user.last_name else ''
    #            # Check if the user has contact details
    #            data['contact'] = True if request.user.contactdetail.phone1 else False
            else:
                data['isLoggedIn'] = False
            return JsonResponse(data)
        elif request.GET.get('message') == 'create':
            if request.user.is_authenticated:
                print("I am logged in")
                # Use the property id to get the property
                prop_id = int(request.GET.get('propId'))
                prop = get_object_or_404(Property,id = prop_id)
                name = request.GET.get('name')
                mobile_number = request.GET.get('mobileNumber')
                date = request.GET.get('date')
                time = request.GET.get('time')
                print(prop)
#                schedule_tour = ScheduleTour(
#                    prop = prop,
#                    name = name,
#                    email = request.user.email,
#                    contact = mobile_number,
#                )
            else:
                prop_id = request.GET.get('propId')
                name = request.GET.get('name')
                email = request.GET.get('email')
                mobile_number = request.GET.get('mobileNumber')
                date = request.GET.get('date')
                time = request.GET.get('time')
                print("I am not logged in")
            return JsonResponse({})
