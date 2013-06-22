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


def frontpage(request):
	return render_to_response('frontpage.html', RequestContext(request))

def userhome(request,list_owner):
	last_login = User.objects.get(username=list_owner).last_login
	date_joined = User.objects.get(username=list_owner).date_joined
	current_user = User.objects.get(username=list_owner)
	userpic = UserProfile.objects.get(user=current_user).userpic
	link1 = UserProfile.objects.get(user=current_user).link1
	link2 = UserProfile.objects.get(user=current_user).link2
	link3 = UserProfile.objects.get(user=current_user).link3
	book_list = Item.objects.all().filter(item_creator=list_owner).filter(category='book')
	tv_list = Item.objects.all().filter(item_creator=list_owner).filter(category='tv')
	movie_list = Item.objects.all().filter(item_creator=list_owner).filter(category='movie')
	game_list = Item.objects.all().filter(item_creator=list_owner).filter(category='game')
	music_list = Item.objects.all().filter(item_creator=list_owner).filter(category='music')
	book_size = len(book_list)
	tv_size = len(tv_list)
	movie_size = len(movie_list)
	game_size = len(game_list)
	music_size = len(music_list)
	return render_to_response('userhome.html', {'current': 'userhome', 'booksize': book_size, 'tvsize': tv_size, 'moviesize': movie_size, 'gamesize': game_size, 'musicsize': music_size, 'lastlogin': last_login, 'datejoined': date_joined, 'listowner': list_owner, 'userpic':userpic, 'link1':link1, 'link2':link2, 'link3':link3}, 
	RequestContext(request))
	
	
def books(request,list_owner):
	list_user = User.objects.get(username=list_owner)
	book_sort1 = UserProfile.objects.get(user=list_user).booksort1
	book_sort2 = UserProfile.objects.get(user=list_user).booksort2
	book_list = Item.objects.all().filter(item_creator=list_owner).filter(category='book').order_by(book_sort1,book_sort2,'name')
	return render_to_response('list.html', {'current': 'books', 'booklist': book_list, 'listowner': list_owner}, 
	RequestContext(request))

def tv(request,list_owner):
	list_user = User.objects.get(username=list_owner)
	tv_sort1 = UserProfile.objects.get(user=list_user).tvsort1
	tv_sort2 = UserProfile.objects.get(user=list_user).tvsort2
	tv_list = Item.objects.all().filter(item_creator=list_owner).filter(category='tv').order_by(tv_sort1,tv_sort2,'name')
	return render_to_response('list.html', {'current': 'tv', 'tvlist': tv_list, 'listowner': list_owner}, 
	RequestContext(request))

def movies(request,list_owner):
	list_user = User.objects.get(username=list_owner)
	movie_sort1 = UserProfile.objects.get(user=list_user).moviesort1
	movie_sort2 = UserProfile.objects.get(user=list_user).moviesort2
	movie_list = Item.objects.all().filter(item_creator=list_owner).filter(category='movie').order_by(movie_sort1,movie_sort2,'name')
	return render_to_response('list.html', {'current': 'movies', 'movielist': movie_list, 'listowner': list_owner}, 
	RequestContext(request))

def games(request,list_owner):
	list_user = User.objects.get(username=list_owner)
	game_sort1 = UserProfile.objects.get(user=list_user).gamesort1
	game_sort2 = UserProfile.objects.get(user=list_user).gamesort2
	game_list = Item.objects.all().filter(item_creator=list_owner).filter(category='game').order_by(game_sort1,game_sort2,'name')
	return render_to_response('list.html', {'current': 'games', 'gamelist': game_list, 'listowner': list_owner}, 
	RequestContext(request))

def music(request,list_owner):
	list_user = User.objects.get(username=list_owner)
	music_sort1 = UserProfile.objects.get(user=list_user).musicsort1
	music_sort2 = UserProfile.objects.get(user=list_user).musicsort2
	music_list = Item.objects.all().filter(item_creator=list_owner).filter(category='music').order_by(music_sort1,music_sort2,'name')
	return render_to_response('list.html', {'current': 'music', 'musiclist': music_list, 'listowner': list_owner}, 
	RequestContext(request))

@login_required
def editbook(request,list_owner,pk):
	list_user = User.objects.get(username=list_owner)
	book_sort1 = UserProfile.objects.get(user=list_user).booksort1
	book_sort2 = UserProfile.objects.get(user=list_user).booksort2
	book_list = Item.objects.all().filter(item_creator=list_owner).filter(category='book').order_by(book_sort1,book_sort2,'name')
	item_to_edit = Item.objects.get(pk=pk)
	if request.method == 'POST':
		form = EditItem(request.POST, instance=item_to_edit)
		if form.is_valid():
			form.save()
			returnurl = "/~" + list_owner + "/books"
			return HttpResponseRedirect(returnurl)
	else:
		form = EditItem(instance=item_to_edit)
	return render_to_response('edit.html', {'current': 'books', 'listowner': list_owner, 'item_to_edit': item_to_edit, 'form':form}, RequestContext(request))

@login_required
def edittv(request,list_owner,pk):
	list_user = User.objects.get(username=list_owner)
	tv_sort1 = UserProfile.objects.get(user=list_user).tvsort1
	tv_sort2 = UserProfile.objects.get(user=list_user).tvsort2
	tv_list = Item.objects.all().filter(item_creator=list_owner).filter(category='tv').order_by(tv_sort1,tv_sort2,'name')
	item_to_edit = Item.objects.get(pk=pk)
	if request.method == 'POST':
		form = EditItem(request.POST, instance=item_to_edit)
		if form.is_valid():
			form.save()
			returnurl = "/~" + list_owner + "/tv"
			return HttpResponseRedirect(returnurl)
	else:
		form = EditItem(instance=item_to_edit)
	return render_to_response('edit.html', {'current': 'tv', 'listowner': list_owner, 'item_to_edit': item_to_edit, 'form':form}, RequestContext(request))

@login_required
def editmovie(request,list_owner,pk):
	list_user = User.objects.get(username=list_owner)
	movie_sort1 = UserProfile.objects.get(user=list_user).moviesort1
	movie_sort2 = UserProfile.objects.get(user=list_user).moviesort2
	movie_list = Item.objects.all().filter(item_creator=list_owner).filter(category='movie').order_by(movie_sort1,movie_sort2,'name')
	item_to_edit = Item.objects.get(pk=pk)
	if request.method == 'POST':
		form = EditItem(request.POST, instance=item_to_edit)
		if form.is_valid():
			form.save()
			returnurl = "/~" + list_owner + "/movies"
			return HttpResponseRedirect(returnurl)
	else:
		form = EditItem(instance=item_to_edit)
	return render_to_response('edit.html', {'current': 'movies', 'listowner': list_owner, 'item_to_edit': item_to_edit, 'form':form}, RequestContext(request))

@login_required
def editgame(request,list_owner,pk):
	list_user = User.objects.get(username=list_owner)
	game_sort1 = UserProfile.objects.get(user=list_user).gamesort1
	game_sort2 = UserProfile.objects.get(user=list_user).gamesort2
	game_list = Item.objects.all().filter(item_creator=list_owner).filter(category='game').order_by(game_sort1,game_sort2,'name')
	item_to_edit = Item.objects.get(pk=pk)
	if request.method == 'POST':
		form = EditItem(request.POST, instance=item_to_edit)
		if form.is_valid():
			form.save()
			returnurl = "/~" + list_owner + "/games"
			return HttpResponseRedirect(returnurl)
	else:
		form = EditItem(instance=item_to_edit)
	return render_to_response('edit.html', {'current': 'games', 'listowner': list_owner, 'item_to_edit': item_to_edit, 'form':form}, RequestContext(request))

@login_required
def editmusic(request,list_owner,pk):
	list_user = User.objects.get(username=list_owner)
	music_sort1 = UserProfile.objects.get(user=list_user).musicsort1
	music_sort2 = UserProfile.objects.get(user=list_user).musicsort2
	music_list = Item.objects.all().filter(item_creator=list_owner).filter(category='music').order_by(music_sort1,music_sort2,'name')
	item_to_edit = Item.objects.get(pk=pk)
	if request.method == 'POST':
		form = EditItem(request.POST, instance=item_to_edit)
		if form.is_valid():
			form.save()
			returnurl = "/~" + list_owner + "/music"
			return HttpResponseRedirect(returnurl)
	else:
		form = EditItem(instance=item_to_edit)
	return render_to_response('edit.html', {'current': 'music', 'listowner': list_owner, 'item_to_edit': item_to_edit, 'form':form}, RequestContext(request))

@login_required
def newbook(request,list_owner):
	list_user = User.objects.get(username=list_owner)
	book_sort1 = UserProfile.objects.get(user=list_user).booksort1
	book_sort2 = UserProfile.objects.get(user=list_user).booksort2
	book_list = Item.objects.all().filter(item_creator=list_owner).filter(category='book').order_by(book_sort1,book_sort2,'name')
	if request.method == 'POST':
		form = EditItem(request.POST)
		if form.is_valid():
			newentry=form.save()
			returnurl = "/~" + list_owner + "/books"
			return HttpResponseRedirect(returnurl)
	else:
		form = EditItem()
	return render_to_response('edit.html', {'current': 'books', 'listowner': list_owner, 'form':form}, RequestContext(request))

@login_required
def newtv(request,list_owner):
	list_user = User.objects.get(username=list_owner)
	tv_sort1 = UserProfile.objects.get(user=list_user).tvsort1
	tv_sort2 = UserProfile.objects.get(user=list_user).tvsort2
	tv_list = Item.objects.all().filter(item_creator=list_owner).filter(category='tv').order_by(tv_sort1,tv_sort2,'name')
	if request.method == 'POST':
		form = EditItem(request.POST)
		if form.is_valid():
			newentry=form.save()
			returnurl = "/~" + list_owner + "/tv"
			return HttpResponseRedirect(returnurl)
	else:
		form = EditItem()
	return render_to_response('edit.html', {'current': 'tv', 'listowner': list_owner, 'form':form}, RequestContext(request))

@login_required
def newmovie(request,list_owner):
	list_user = User.objects.get(username=list_owner)
	movie_sort1 = UserProfile.objects.get(user=list_user).moviesort1
	movie_sort2 = UserProfile.objects.get(user=list_user).moviesort2
	movie_list = Item.objects.all().filter(item_creator=list_owner).filter(category='movie').order_by(movie_sort1,movie_sort2,'name')
	if request.method == 'POST':
		form = EditItem(request.POST)
		if form.is_valid():
			newentry=form.save()
			returnurl = "/~" + list_owner + "/movies"
			return HttpResponseRedirect(returnurl)
	else:
		form = EditItem()
	return render_to_response('edit.html', {'current': 'movies', 'listowner': list_owner, 'form':form}, RequestContext(request))

@login_required
def newgame(request,list_owner):
	list_user = User.objects.get(username=list_owner)
	game_sort1 = UserProfile.objects.get(user=list_user).gamesort1
	game_sort2 = UserProfile.objects.get(user=list_user).gamesort2
	game_list = Item.objects.all().filter(item_creator=list_owner).filter(category='game').order_by(game_sort1,game_sort2,'name')
	if request.method == 'POST':
		form = EditItem(request.POST)
		if form.is_valid():
			newentry=form.save()
			returnurl = "/~" + list_owner + "/games"
			return HttpResponseRedirect(returnurl)
	else:
		form = EditItem()
	return render_to_response('edit.html', {'current': 'games', 'listowner': list_owner, 'form':form}, RequestContext(request))

@login_required
def newmusic(request,list_owner):
	list_user = User.objects.get(username=list_owner)
	music_sort1 = UserProfile.objects.get(user=list_user).musicsort1
	music_sort2 = UserProfile.objects.get(user=list_user).musicsort2
	music_list = Item.objects.all().filter(item_creator=list_owner).filter(category='music').order_by(music_sort1,music_sort2,'name')
	if request.method == 'POST':
		form = EditItem(request.POST)
		if form.is_valid():
			newentry=form.save()
			returnurl = "/~" + list_owner + "/music"
			return HttpResponseRedirect(returnurl)
	else:
		form = EditItem()
	return render_to_response('edit.html', {'current': 'music', 'listowner': list_owner, 'form':form}, RequestContext(request))

@login_required
def delbook(request,list_owner,pk):
	if request.user.username != list_owner:
		gohomeurl = "/~" + request.user.username
		return HttpResponseRedirect(gohomeurl)
	list_user = User.objects.get(username=list_owner)
	item_to_edit = Item.objects.get(pk=pk)
	item_to_edit.delete()
	returnurl = "/~" + list_owner + "/books"
	return HttpResponseRedirect(returnurl)

@login_required
def delgame(request,list_owner,pk):
	if request.user.username != list_owner:
		gohomeurl = "/~" + request.user.username
		return HttpResponseRedirect(gohomeurl)
	list_user = User.objects.get(username=list_owner)
	item_to_edit = Item.objects.get(pk=pk)
	item_to_edit.delete()
	returnurl = "/~" + list_owner + "/games"
	return HttpResponseRedirect(returnurl)

@login_required
def delmovie(request,list_owner,pk):
	if request.user.username != list_owner:
		gohomeurl = "/~" + request.user.username
		return HttpResponseRedirect(gohomeurl)
	list_user = User.objects.get(username=list_owner)
	item_to_edit = Item.objects.get(pk=pk)
	item_to_edit.delete()
	returnurl = "/~" + list_owner + "/movies"
	return HttpResponseRedirect(returnurl)

@login_required
def deltv(request,list_owner,pk):
	if request.user.username != list_owner:
		gohomeurl = "/~" + request.user.username
		return HttpResponseRedirect(gohomeurl)
	list_user = User.objects.get(username=list_owner)
	item_to_edit = Item.objects.get(pk=pk)
	item_to_edit.delete()
	returnurl = "/~" + list_owner + "/tv"
	return HttpResponseRedirect(returnurl)

@login_required
def delmusic(request,list_owner,pk):
	if request.user.username != list_owner:
		gohomeurl = "/~" + request.user.username
		return HttpResponseRedirect(gohomeurl)
	list_user = User.objects.get(username=list_owner)
	item_to_edit = Item.objects.get(pk=pk)
	item_to_edit.delete()
	returnurl = "/~" + list_owner + "/music"
	return HttpResponseRedirect(returnurl)



@login_required
def userpic(request,list_owner):
	if request.user.username != list_owner:
		redirect = "/~" + request.user.username + "/userpic"
		return HttpResponseRedirect(redirect)
	current_user = User.objects.get(pk=request.user.id)
	current_profile = current_user.get_profile()
	current_userpic = UserProfile.objects.get(user_id=current_user).userpic
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
	current_user = User.objects.get(pk=request.user.id)
	current_profile = current_user.get_profile()
	current_link1 = UserProfile.objects.get(user_id=current_user).link1
	current_link2 = UserProfile.objects.get(user_id=current_user).link2
	current_link3 = UserProfile.objects.get(user_id=current_user).link3
	if request.method == 'POST':
		form = EditLinks(request.POST, instance=current_profile)
		if form.is_valid():
			current_profile.link1=request.POST['link1']
			current_profile.link2=request.POST['link2']
			current_profile.link3=request.POST['link3']
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
	current_user = User.objects.get(pk=request.user.id)
	current_profile = current_user.get_profile()
	tvsort1 = UserProfile.objects.get(user_id=current_user).tvsort1
	tvsort2 = UserProfile.objects.get(user_id=current_user).tvsort2
	moviesort1 = UserProfile.objects.get(user_id=current_user).moviesort1
	moviesort2 = UserProfile.objects.get(user_id=current_user).moviesort2
	booksort1 = UserProfile.objects.get(user_id=current_user).booksort1
	booksort2 = UserProfile.objects.get(user_id=current_user).booksort2
	gamesort1 = UserProfile.objects.get(user_id=current_user).gamesort1
	gamesort2 = UserProfile.objects.get(user_id=current_user).gamesort2
	musicsort1 = UserProfile.objects.get(user_id=current_user).musicsort1
	musicsort2 = UserProfile.objects.get(user_id=current_user).musicsort2
	if request.method == 'POST':
		current_profile.tvsort1=request.POST['tvsort1']
		current_profile.tvsort2=request.POST['tvsort2']
		current_profile.moviesort1=request.POST['moviesort1']
		current_profile.moviesort2=request.POST['moviesort2']
		current_profile.booksort1=request.POST['booksort1']
		current_profile.booksort2=request.POST['booksort2']
		current_profile.gamesort1=request.POST['gamesort1']
		current_profile.gamesort2=request.POST['gamesort2']
		current_profile.musicsort1=request.POST['musicsort1']
		current_profile.musicsort2=request.POST['musicsort2']
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
