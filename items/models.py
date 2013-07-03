from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.forms import ModelForm, HiddenInput
from easy_thumbnails.fields import ThumbnailerImageField
from django.core.validators import URLValidator, validate_email, MaxValueValidator, MinValueValidator, MaxLengthValidator


CATEGORY_CHOICES = (
	('book','book'),
	('tv','tv'),
	('movie','movie'),
	('game','game'),
	('music','music'),
)

class Item(models.Model):
	item_creator = models.CharField(max_length=30) # user name goes here
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)	
	name = models.CharField(max_length=70, validators=[ MaxLengthValidator(70) ])
	category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
	artist = models.CharField(max_length=70, blank=True, validators=[ MaxLengthValidator(70) ]) # use as "author" in books, "platform" in games, "studio" in tv, "director" in movies
	type = models.CharField(max_length=50, blank=True, validators=[ MaxLengthValidator(50) ])
	progress = models.CharField(max_length=30, blank=True, validators=[ MaxLengthValidator(30) ]) # use as "year" in music, ignore in movies
	finished = models.BooleanField(default=False)
	rating = models.IntegerField(max_length=3, blank=True, null=True, validators=[ MinValueValidator(0),MaxValueValidator(100) ])
	comment = models.CharField(max_length=140, blank=True, validators=[ MaxLengthValidator(140) ])
	def __unicode__(self):
		return self.name

class EditItem(ModelForm):
    class Meta:
        model = Item
        widgets = {'item_creator':HiddenInput, 'category':HiddenInput, 'created':HiddenInput, 'modified':HiddenInput,}
		
class ItemAdmin(admin.ModelAdmin):
	list_display = ["category", "name", "artist", "created", "modified", "type", "progress", "finished", "rating", "comment"]
	search_fields = ["name"]
	
class UserProfile(models.Model):
    def userpic_path(instance, filename):
        ext = filename.split('.')[-1]
        userpic_name = '.'.join([instance.user.username, ext])
        return "userpics/"+userpic_name
    
    SORT_CHOICES = (
        ('name','name'),
        ('artist','artist'),
        ('type','type'),
        ('progress','progress'),
        ('finished','finished'),
        ('-finished','-finished'),
        ('rating','rating'),
        ('-rating','-rating'),
        ('created','created'),
        ('-created','-created'),
        ('modified','modified'),
        ('-modified','-modified'),
        ('comment','comment'),
    )
    user = models.OneToOneField(User)
    userpic = ThumbnailerImageField(upload_to=userpic_path, resize_source=dict(size=(100, 100), crop='smart', upscale=True), default="userpics/default.png")
    link1 = models.URLField(blank=True, max_length=100, verbose_name='Link 1', validators=[ MaxLengthValidator(100), URLValidator() ])
    link2 = models.URLField(blank=True, max_length=100, verbose_name='Link 2', validators=[ MaxLengthValidator(100), URLValidator() ])
    link3 = models.URLField(blank=True, max_length=100, verbose_name='Link 3', validators=[ MaxLengthValidator(100), URLValidator() ])
    tvsort1 = models.CharField(max_length=10, choices=SORT_CHOICES, default='name')
    tvsort2 = models.CharField(max_length=10, choices=SORT_CHOICES, default='name')
    moviesort1 = models.CharField(max_length=10, choices=SORT_CHOICES, default='name')
    moviesort2 = models.CharField(max_length=10, choices=SORT_CHOICES, default='name')
    booksort1 = models.CharField(max_length=10, choices=SORT_CHOICES, default='name')
    booksort2 = models.CharField(max_length=10, choices=SORT_CHOICES, default='name')
    gamesort1 = models.CharField(max_length=10, choices=SORT_CHOICES, default='name')
    gamesort2 = models.CharField(max_length=10, choices=SORT_CHOICES, default='name')
    musicsort1 = models.CharField(max_length=10, choices=SORT_CHOICES, default='artist')
    musicsort2 = models.CharField(max_length=10, choices=SORT_CHOICES, default='name')

class Contact(models.Model): 
    email = models.EmailField(blank=True) 
    name = models.CharField(max_length=140, blank=True, validators=[ MaxLengthValidator(140) ]) 
    subject = models.CharField(max_length=140, blank=True, validators=[ MaxLengthValidator(140) ]) 
    message = models.TextField() 

class ContactForm(ModelForm):
	class Meta:
		model = Contact
	
class UserpicUpload(ModelForm):
	class Meta:
		model = UserProfile
		fields = ('userpic',)

class EditLinks(ModelForm):
	class Meta:
		model = UserProfile
		fields = ('link1','link2','link3')



admin.site.register(Item, ItemAdmin)
