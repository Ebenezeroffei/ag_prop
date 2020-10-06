from datetime import datetime
import pytz
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test,login_required
from .models import Property,ScheduleTour
from .forms import PropertyForm,InteriorFeaturesForm,ExteriorFeaturesForm

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
    

# Don't forget to add admin mixins
class PropertiesCreateView(generic.View):
    form_class1 = PropertyForm
    form_class2 = InteriorFeaturesForm
    form_class3 = ExteriorFeaturesForm
    template_name = 'app/property_form.html'

    def get(self,request,*args,**kwargs):
        form1 = self.form_class1()
        form2 = self.form_class2()
        form3 = self.form_class3()
        context = {
            'form1': form1,
            'form2': form2,
            'form3': form3
        }
        return render(request,self.template_name,context)


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
            date = request.GET.get('date').split('-')
            time = request.GET.get('time').split(':')
            print(date)
            print(time)
            data = {}
            # User is logged in
            if request.user.is_authenticated: # A user has logged in
                data['isLoggedIn'] = True
                # Check to see if user's name has already been registered in the database
                data['name'] = f"{request.user.first_name} {request.user.last_name}" if request.user.first_name and request.user.last_name else ''
                # Check to see if user's contact has already been registered in the database
                try:
                    data['contact'] = request.user.contactdetail.phone1
                except AttributeError:
                    data['contact'] = ''
            # User isn't logged in
            else:
                data['isLoggedIn'] = False
            return JsonResponse(data)

        # Creating a tour for a user who is creating is first tour or an anonymouse user
        elif request.GET.get('message') == 'create':

            # User is logged in
            if request.user.is_authenticated:
                print("I am logged in")
                # Use the property id to get the property
                prop_id = request.GET.get('propId')
                prop = get_object_or_404(Property,id = prop_id)
                name = request.GET.get('name')
                mobile_number = request.GET.get('mobileNumber')
                date = request.GET.get('date').split('-')
                time = request.GET.get('time').split(':')
                date_time = datetime(int(date[0]),int(date[1]),int(date[2]),int(time[0]),int(time[1]),tzinfo = pytz.UTC)
                print(date_time)
                # Schedule a tour
                schedule_tour = ScheduleTour(
                    prop = prop,
                    name = name,
                    email = request.user.email,
                    contact = mobile_number,
                    date = date_time
                )
                schedule_tour.save()

            # Anonymous user
            else:
                # Use the property id to get the property
                prop_id = int(request.GET.get('propId'))
                prop = get_object_or_404(Property,id = prop_id)
                name = request.GET.get('name')
                email = request.GET.get('email')
                mobile_number = request.GET.get('mobileNumber')
                date = request.GET.get('date').split('-')
                time = request.GET.get('time').split(':')
                date_time = datetime(int(date[0]),int(date[1]),int(date[2]),int(time[0]),int(time[1]),tzinfo = pytz.UTC)
                print("I am not logged in")
                # Schedule a tour
                schedule_tour = ScheduleTour(
                    prop = prop,
                    name = name,
                    email = email,
                    contact = mobile_number,
                    date = date_time
                )
                schedule_tour.save()
            return JsonResponse({})
