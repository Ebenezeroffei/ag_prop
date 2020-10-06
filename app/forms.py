from django import forms
from .models import Property,ExteriorFeatures,InteriorFeatures

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields  = ['name','price','category','state_or_region','town_or_city','size','bedroom','bathroom','extras','image1','image2','image3','image4','image5']

        labels = {
            'image1': "Property Image 1",
            'image2': "Property Image 2",
            'image3': "Property Image 3",
            'image4': "Property Image 4",
            'image5': "Property Image 5"
        }

        help_texts = {
            'extras': 'Seperate each extra feature with a comma (,)',
            'size': "The size of the property must be in square feet"
        }

        widgets = {
            'name':forms.TextInput(attrs = {
                'class': 'form-control form-control-sm'
            }),
            'price':forms.NumberInput(attrs = {
                'class': 'form-control form-control-sm'
            }),
            'category':forms.Select(attrs = {
                'class': 'form-control form-control-sm'
            }),
            'state_or_region':forms.TextInput(attrs = {
                'class': 'form-control form-control-sm'
            }),
            'town_or_city':forms.TextInput(attrs = {
                'class': 'form-control form-control-sm'
            }),
            'size':forms.NumberInput(attrs = {
                'class': 'form-control form-control-sm'
            }),
            'bedroom':forms.NumberInput(attrs = {
                'class': 'form-control form-control-sm'
            }),
            'bathroom':forms.NumberInput(attrs = {
                'class': 'form-control form-control-sm'
            }),
            'extras':forms.TextInput(attrs = {
                'class': 'form-control form-control-sm'
            }),
        }

class InteriorFeaturesForm(forms.ModelForm):
    class Meta:
        model = InteriorFeatures
        fields = ['kitchen','reception']

        widgets = {
            'kitchen': forms.NumberInput(attrs = {
                'class': 'form-control form-control-sm'
            }),
            'reception': forms.NumberInput(attrs = {
                'class': 'form-control form-control-sm'
            })
        }

class ExteriorFeaturesForm(forms.ModelForm):
    class Meta:
        model = ExteriorFeatures
        fields = ['garage','parking','domestic_accomodation','security','pool']

        widgets = {
            'garage': forms.NumberInput(attrs = {
                'class': 'form-control form-control-sm'
            }),
            'parking': forms.NumberInput(attrs = {
                'class': 'form-control form-control-sm'
            }),
            'domestic_accomodation': forms.NumberInput(attrs = {
                'class': 'form-control form-control-sm'
            }),
            'security': forms.Select(attrs = {
                'class': 'form-control form-control-sm'
            }),
            'pool': forms.Select(attrs = {
                'class': 'form-control form-control-sm'
            })
        }
