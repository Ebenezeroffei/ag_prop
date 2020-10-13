from datetime import datetime
import pytz
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test,login_required
from django.urls import reverse
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
    
# Dont forget to add some mixins
class AdminPropertiesView(generic.ListView):
    model = Property
    template_name = 'app/admin_properties.html'
    context_object_name = 'properties'

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

    def post(self,request,*args,**kwargs):
        form1 = self.form_class1(request.POST,request.FILES)
        form2 = self.form_class2(request.POST)
        form3 = self.form_class3(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            property_details = form1.cleaned_data
            # Create and save the property
            prop = Property(**property_details)
            prop.save()
            # Modify the property exterior and interior features before saving
            form2.instance.bedroom = form1.cleaned_data.get('bedroom')
            form2.instance.bathroom = form1.cleaned_data.get('bathroom')
            form2.instance.prop = prop
            form3.instance.prop = prop
            form2.save()
            form3.save()
            return HttpResponseRedirect(reverse('app:properties_detail',args = (prop.pk,)))
        else:
            print("They are not valid")
        context = {
            'form1': form1,
            'form2': form2,
            'form3': form3
        }
        return render(request,self.template_name,context)

# Don't forget to add mixins
class PropertyEditView(generic.View):
    form_class1 = PropertyForm
    form_class2 = InteriorFeaturesForm
    form_class3 = ExteriorFeaturesForm
    template_name = 'app/property_form.html'

    def get(self,request,*args,**kwargs):
        property_id = self.kwargs.get('pk')
        prop = get_object_or_404(Property,id = property_id)
        form1 = self.form_class1(instance = prop)
        form2 = self.form_class2(instance = prop.interiorfeatures)
        form3 = self.form_class3(instance = prop.exteriorfeatures)
        context = {
            'form1': form1,
            'form2': form2,
            'form3': form3,
            'update': True,
            'image1': prop.image1.url,
            'image2': prop.image2.url,
            'image3': prop.image3.url,
            'image4': prop.image4.url,
            'image5': prop.image5.url
        }
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        property_id = self.kwargs.get('pk')
        prop = get_object_or_404(Property,id = property_id)
        form1 = self.form_class1(request.POST,request.FILES,instance = prop)
        form2 = self.form_class2(request.POST,instance = prop.interiorfeatures)
        form3 = self.form_class3(request.POST,instance = prop.exteriorfeatures)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            property_details = form1.cleaned_data
            # Create and save the property
            # Modify the property exterior and interior features before saving
            form2.instance.bedroom = form1.cleaned_data.get('bedroom')
            form2.instance.bathroom = form1.cleaned_data.get('bathroom')
            form1.save()
            form2.save()
            form3.save()
            return HttpResponseRedirect(reverse('app:properties_detail',args = (prop.pk,)))
        else:
            print("They are not valid")
        context = {
            'form1': form1,
            'form2': form2,
            'form3': form3,
            'update': True,
            'image1': prop.image1.url,
            'image2': prop.image2.url,
            'image3': prop.image3.url,
            'image4': prop.image4.url,
            'image5': prop.image5.url
        }
        return render(request,self.template_name,context)

class PropertiesDetailView(generic.DetailView):
    """ This class displays the details of the property """
    model = Property
    
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['props'] = [super().get_object()]
        return context

# Dont forget to add some mixins
class SchedulesView(generic.ListView):
    """ This class displays all the schedules """
    model = ScheduleTour
    template_name = 'app/schedules.html'
    context_object_name = 'schedules'
    
    
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


class DeletePropertyView(generic.View):
    """ This class is responsible for deleting a blog """

    def post(self,request,*args,**kwargs):
        property_id = int(request.POST.get('propertyId'))
        property = get_object_or_404(Property,id = property_id)
        # Delete Blog
        property.delete()
        # Delete Image from the disk
        data = {'count': Property.objects.count()}
        return JsonResponse(data)


class AcceptOrRejectRequestView(generic.View):
    """ This function either accepts of rejects a request to schedule a tour """

    def post(self,request,*args,**kwargs):
        schedule_id = int(request.POST.get('scheduleId'))
        schedule = get_object_or_404(ScheduleTour, id = schedule_id)
        message = request.POST.get('message')
        if message == 'accept':
            email_message = "Your requesr has been accepted"
            schedule.accepted = True
            schedule.save()
        elif message == 'reject':
            email_message = "Your requesr has been rejected"
            schedule.delete()

        send_mail(
            "Request to Schedule Tour",
            email_message,
            from_email = "Agyapong Properties",
            recipient_list = ['ebenezeroffei@outlook.com']
        )

        return JsonResponse({'count':ScheduleTour.objects.count()})
