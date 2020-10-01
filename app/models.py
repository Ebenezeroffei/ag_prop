from django.db import models

# Create your models here.
class Property(models.Model):
    category_choices = [
        ('Sale','Sale'),
        ('Rent','Rent'),
        ('Buy','Buy')
    ]
    name = models.CharField(max_length = 100);
    price = models.DecimalField(decimal_places = 2,max_digits = 100000)
    location =  models.CharField(max_length = 100)
    size = models.DecimalField(decimal_places = 2,max_digits = 50)
    extras = models.CharField(max_length = 500)
    features = models.CharField(max_length = 500)
    bedroom = models.PositiveSmallIntegerField(default = 0)
    bathroom = models.PositiveSmallIntegerField(default = 0)
    category = models.CharField(max_length = 10,choices = category_choices,default = 'Sale')
    image1 = models.ImageField(default = 'property_default.png',upload_to = 'properties_pics')
    image2 = models.ImageField(default = 'property_default.png',upload_to = 'properties_pics')
    image3 = models.ImageField(default = 'property_default.png',upload_to = 'properties_pics')
    image4 = models.ImageField(default = 'property_default.png',upload_to = 'properties_pics')
    image5 = models.ImageField(default = 'property_default.png',upload_to = 'properties_pics')
    
    def active_images(self):
        from os import path
        return [img for img in [self.image1,self.image2,self.image3,self.image4,self.image5] if path.exists(img.path) ]
    
    def formatted_extras(self):
        return self.extras.split(',')
    
    def formatted_price(self):
        whole = str(self.price).split('.')[0]
        
        correct_money_format = ''
        for num,i in enumerate(whole):
            if (num + 1) % 3 == 0 and num != 0:
                correct_money_format += f'{i},'
            else:
                correct_money_format += i
        return f"{correct_money_format}.{str(self.price).split('.')[1]}"
    
    def __str__(self):
        return f'{self.name}'
    
class ExteriorFeatures(models.Model):
    """ This class is responsible for storing the external features of the property """
    features_choices = [
        ('Yes','Yes'),
        ('No','No')
    ]
    prop = models.OneToOneField(Property,on_delete = models.CASCADE)
    garage = models.PositiveSmallIntegerField(default = 0);
    parking = models.PositiveSmallIntegerField(default = 0);
    domestic_accomodation = models.PositiveSmallIntegerField(default = 0);
    security = models.CharField(choices = features_choices,default = 'Yes',max_length = 3)
    pool = models.CharField(choices = features_choices,default = 'Yes',max_length = 3)
    
    def __str__(self):
        return f"{self.prop.name}'s exterior features"
    
class InteriorFeatures(models.Model):
    """ This class is responsible for storing the internal features of the property """
    prop = models.OneToOneField(Property,on_delete = models.CASCADE)
    bedroom = models.PositiveSmallIntegerField(default = 0)
    bathroom = models.PositiveSmallIntegerField(default = 0)
    kitchen = models.PositiveSmallIntegerField(default = 0)
    reception = models.PositiveSmallIntegerField(default = 0)
    
    def __str__(self):
        return f"{self.prop.name}'s interior features"