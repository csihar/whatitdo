from django import forms

CATEGORY_CHOICES = (
	('book','book'),
	('tv','tv'),
	('movie','movie'),
	('game','game'),
	('music','music'),
)

class EditItem(forms.Form):
	item_creator = forms.CharField(max_length=30)
	name = forms.CharField(max_length=70)
	category = forms.ChoiceField(choices=CATEGORY_CHOICES)
	created = forms.DateTimeField()
	modified = forms.DateTimeField()	
	artist = forms.CharField(max_length=70, required=False)
	type = forms.CharField(max_length=50, required=False)
	progress = forms.CharField(max_length=10, required=False)
	finished = forms.BooleanField(required=False)
	rating = forms.IntegerField(max_length=3, min_value=0, max_value=100, required=False)
	comment = forms.CharField(max_length=140, required=False)

class UserpicUpload(forms.ModelForm):
    userpic  = forms.ImageField()

class EditLinks(forms.ModelForm):
    link1 = models.URLField(blank=True, max_length=100, label='Link 1')
    link2 = models.URLField(blank=True, max_length=100, label='Link 2')
    link3 = models.URLField(blank=True, max_length=100, label='Link 3')

class ContactForm(forms.Form): 
    email = forms.EmailField(required=False) 
    name = forms.CharField(max_length=140, required=False) 
    subject = forms.CharField(max_length=140) 
    message = forms.CharField(widget=forms.widgets.Textarea()) 

