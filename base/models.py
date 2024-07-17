from collections.abc import Iterable
from django.db import models
from datetime import datetime
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Executive(models.Model):
    fullName = models.CharField(max_length=100)
    portfolio = models.TextField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images', default='placeholder')
    fbLink = models.URLField(blank=True, null=True)  #learn how to use this field

    

    def __str__(self):
        return self.fullName
    
    
    class Meta:
        verbose_name_plural= 'Executives'

class Testimony(models.Model):
    title = models.TextField(null=True, blank=True)
    testimony = RichTextUploadingField()
    testifier = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.testimony
    
    

    def save(self, *args, **kwargs):
        if self.slug == None:   #if an object doesn't have a slug field, make one and make it the title
            slug = slugify(self.title)

            hasSlug = Testimony.objects.filter(slug=slug).exists() #checks if slug already exists
            count = 1
            while hasSlug:
                count+= 1
                slug = slugify(self.title) + '-' + str(count)   #while it exists, add 1 to count and add that to the name to update slug
                hasSlug=Testimony.objects.filter(slug=slug).exists() #check again and update hasSlug so the loop can end

            self.slug=slug
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural= 'Testimonies'

class Event(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images', default='placeholder')
    name = models.CharField(max_length=255)
    subdescription = models.CharField(max_length= 255, null=True)
    description = RichTextUploadingField()
    date = models.DateTimeField(default=datetime.now)
    isFeatured = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == None:   #if an object doesn't have a slug field, make one and make it the title
            slug = slugify(self.name)

            hasSlug = Event.objects.filter(slug=slug).exists() #checks if slug already exists
            count = 1
            while hasSlug:
                count+= 1
                slug = slugify(self.name) + '-' + str(count)   #while it exists, add 1 to count and add that to the name to update slug
                hasSlug=Event.objects.filter(slug=slug).exists() #check again and update hasSlug so the loop can end

            self.slug=slug
        super().save(*args, **kwargs)
    
    
    class Meta:
        verbose_name_plural= 'Events'
        ordering=['-id']

class audioMessage(models.Model):
    name = models.CharField(max_length=255)
    audio = models.FileField(upload_to='images')
    internal = models.BooleanField(default= False)
    external = models.BooleanField(default=False)
    eventMessages = models.BooleanField(default=False)
    class Meta:
        ordering = ['-id']

class picture(models.Model):
    image = models.ImageField(upload_to='images')
    date = models.DateTimeField(default=datetime.now)
    isFeatured = models.BooleanField(default=False)
    isWallpaper = models.BooleanField(default=False)

# Create your models here.
