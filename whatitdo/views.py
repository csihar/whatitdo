# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from items.models import Item, EditItem, User, UserProfile, UserpicUpload, EditLinks, ContactForm
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import mail_admins
import logging

PLURALS = { "book":"books",
			"game":"games",
			"movie":"movies",
			"music":"music",
			"tv":"tv"}

def frontpage(request):
	return render_to_response('frontpage.html', RequestContext(request))

def userhome(request, list_owner):
	userprofile = UserProfile.objects.select_related().get(user__username=list_owner)
	all_items = Item.objects.all().filter(item_creator=list_owner)
	return render_to_response('userhome.html', {
			'current': 'userhome', 
			'booksize': sum(1 for item in all_items if item.category=="book"), 
			'tvsize': sum(1 for item in all_items if item.category=="tv"), 
			'moviesize': sum(1 for item in all_items if item.category=="movie"), 
			'gamesize': sum(1 for item in all_items if item.category=="game"), 
			'musicsize': sum(1 for item in all_items if item.category=="music"), 
			'lastlogin': userprofile.user.last_login, 
			'datejoined': userprofile.user.date_joined, 
			'listowner': list_owner, 
			'userpic': userprofile.userpic, 
			'link1': userprofile.link1, 
			'link2': userprofile.link2, 
			'link3': userprofile.link3
		}, RequestContext(request))
	
def item_list(request, list_owner, category):
	userprofile = UserProfile.objects.select_related().get(user__username=list_owner)
	sort1 = getattr(userprofile, category+"sort1")
	sort2 = getattr(userprofile, category+"sort2")
	item_list = Item.objects.all().filter(item_creator=list_owner).filter(category=category).order_by(sort1, sort2, 'name')
	return render_to_response('list.html', {
			'current': PLURALS[category], 
			'itemlist': item_list, 
			'listowner': list_owner
		}, RequestContext(request))

@login_required
def edit_item(request, list_owner, category, pk=None):
	if pk:
		item_to_edit = Item.objects.get(pk=pk)
	else:
		item_to_edit = None
	if request.method == 'POST':
		form = EditItem(request.POST, instance=item_to_edit)
		if form.is_valid():
			form.save()
			returnurl = "/~" + list_owner + "/" + PLURALS[category]
			return HttpResponseRedirect(returnurl)
	else:
		form = EditItem(instance=item_to_edit)
	return render_to_response('edit.html', {'current': PLURALS[category], 'listowner': list_owner, 'item_to_edit': item_to_edit, 'form':form}, RequestContext(request))

@login_required
def delete_item(request, list_owner, category, pk):
	if request.user.username != list_owner:
		gohomeurl = "/~" + request.user.username
		return HttpResponseRedirect(gohomeurl)
	list_user = User.objects.get(username=list_owner)
	item_to_edit = Item.objects.get(pk=pk)
	item_to_edit.delete()
	returnurl = "/~" + list_owner + "/" + PLURALS[category]
	return HttpResponseRedirect(returnurl)

@login_required
def userpic(request,list_owner):
	if request.user.username != list_owner:
		redirect = "/~" + request.user.username + "/userpic"
		return HttpResponseRedirect(redirect)
	current_profile = UserProfile.objects.select_related().get(user__username=list_owner)
	current_userpic = UserProfile.objects.get(user_id=current_profile.user).userpic
	if request.method == 'POST':
		form = UserpicUpload(request.POST, request.FILES, instance=current_profile)
		if form.is_valid():
			try:
				current_profile.userpic=request.FILES['userpic']
				current_profile.save()
			except:
				pass
			gohomeurl = "/~" + request.user.username
			return HttpResponseRedirect(gohomeurl)
	else:
		form = UserpicUpload()
	return render_to_response('userpic.html', {'listowner': list_owner, 'form':form, 'currentuserpic':current_userpic}, RequestContext(request))

@login_required
def editlinks(request,list_owner):
	if request.user.username != list_owner:
		redirect = "/~" + request.user.username + "/editlinks"
		return HttpResponseRedirect(redirect)
	current_profile = UserProfile.objects.select_related().get(user__username=list_owner)
	current_link1 = current_profile.link1
	current_link2 = current_profile.link2
	current_link3 = current_profile.link3
	if request.method == 'POST':
		form = EditLinks(request.POST, instance=current_profile)
		if form.is_valid():
			current_profile.link1 = request.POST['link1']
			current_profile.link2 = request.POST['link2']
			current_profile.link3 = request.POST['link3']
			current_profile.save()
			gohomeurl = "/~" + request.user.username
			return HttpResponseRedirect(gohomeurl)
	else:
		form = EditLinks()
	return render_to_response('editlinks.html', {'listowner': list_owner, 'form':form, 'currentlink1':current_link1, 'currentlink2':current_link2, 'currentlink3':current_link3}, RequestContext(request))

@login_required
def listsort(request,list_owner):
	if request.user.username != list_owner:
		redirect = "/~" + request.user.username + "/listsort"
		return HttpResponseRedirect(redirect)
	current_profile = UserProfile.objects.select_related().get(user__username=list_owner)
	tvsort1 = current_profile.tvsort1
	tvsort2 = current_profile.tvsort2
	moviesort1 = current_profile.moviesort1
	moviesort2 = current_profile.moviesort2
	booksort1 = current_profile.booksort1
	booksort2 = current_profile.booksort2
	gamesort1 = current_profile.gamesort1
	gamesort2 = current_profile.gamesort2
	musicsort1 = current_profile.musicsort1
	musicsort2 = current_profile.musicsort2
	if request.method == 'POST':
		current_profile.tvsort1 = request.POST['tvsort1']
		current_profile.tvsort2 = request.POST['tvsort2']
		current_profile.moviesort1 = request.POST['moviesort1']
		current_profile.moviesort2 = request.POST['moviesort2']
		current_profile.booksort1 = request.POST['booksort1']
		current_profile.booksort2 = request.POST['booksort2']
		current_profile.gamesort1 = request.POST['gamesort1']
		current_profile.gamesort2 = request.POST['gamesort2']
		current_profile.musicsort1 = request.POST['musicsort1']
		current_profile.musicsort2 = request.POST['musicsort2']
		current_profile.save()
		gohomeurl = "/~" + request.user.username
		return HttpResponseRedirect(gohomeurl)
	else:
		return render_to_response('listsort.html', {'listowner': list_owner, 'tvsort1_old':tvsort1, 'tvsort2_old':tvsort2, 'moviesort1_old':moviesort1, 'moviesort2_old':moviesort2, 'booksort1_old':booksort1, 'booksort2_old':booksort2, 'gamesort1_old':gamesort1, 'gamesort2_old':gamesort2, 'musicsort1_old':musicsort1, 'musicsort2_old':musicsort2}, RequestContext(request))
		
def contact(request): 
    if request.method == 'POST': 
        form = ContactForm(request.POST) 
        if form.is_valid(): 
            cd = form.cleaned_data 
            mail_admins( 
                cd['subject'] + " - " + cd['name'], 
                cd['email'] + "\n" + cd['message'], 
            ) 
            return HttpResponseRedirect('/contact/thanks/') 
    else: 
        form = ContactForm() 
    return render_to_response('contact.html', {'form': form}, context_instance=RequestContext(request)) 

def contact_thanks(request): 
	return render_to_response('contact_thanks.html', RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
	return render_to_response("registration/register.html", {'form': form})

def login_redir(request):
	gohomeurl = "/~" + request.user.username
	return HttpResponseRedirect(gohomeurl)
