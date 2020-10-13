import os
from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateTimeField(default = timezone.now)
    image = models.ImageField(upload_to = 'blog_images/')
    content = models.TextField()
    
    def save(self,*args,**kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.width > 1200 and img.height > 370:
            img.resize((1200,370))
            img.save(self.image.path)

    def delete(self):
        blog_img = self.image.path
        super().delete()
        os.remove(blog_img)
        
    
    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self,*args,**kwargs):
        return reverse('blog:detail',args = (self.pk,))
