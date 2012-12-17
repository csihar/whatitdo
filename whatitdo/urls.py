import settings, signals
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import *
from django.http import HttpResponseRedirect
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('whatitdo.views',
    url(r'^~?$', 'frontpage', name='frontpage'),
    url(r'^~([A-Za-z0-9]{1,30})/?$', 'userhome', name='userhome'),
    url(r'^~([A-Za-z0-9]{1,30})/userpic/?$', 'userpic', name='userpic'),
    url(r'^~([A-Za-z0-9]{1,30})/editlinks/?$', 'editlinks', name='editlinks'),
    url(r'^~([A-Za-z0-9]{1,30})/listsort/?$', 'listsort', name='listsort'),
    url(r'^~([A-Za-z0-9]{1,30})/tv/?$', 'tv', name='tv'),
    url(r'^~([A-Za-z0-9]{1,30})/movies/?$', 'movies', name='movies'),
    url(r'^~([A-Za-z0-9]{1,30})/books/?$', 'books', name='books'),
    url(r'^~([A-Za-z0-9]{1,30})/games/?$', 'games', name='games'),
    url(r'^~([A-Za-z0-9]{1,30})/music/?$', 'music', name='music'),
    url(r'^~([A-Za-z0-9]{1,30})/tv/edit/(\d+)/?$', 'edittv', name='edittv'),
    url(r'^~([A-Za-z0-9]{1,30})/movies/edit/(\d+)/?$', 'editmovie', name='editmovie'),
    url(r'^~([A-Za-z0-9]{1,30})/books/edit/(\d+)/?$', 'editbook', name='editbook'),
    url(r'^~([A-Za-z0-9]{1,30})/games/edit/(\d+)/?$', 'editgame', name='editgame'),
    url(r'^~([A-Za-z0-9]{1,30})/music/edit/(\d+)/?$', 'editmusic', name='editmusic'),
    url(r'^~([A-Za-z0-9]{1,30})/tv/new/?$', 'newtv', name='newtv'),
    url(r'^~([A-Za-z0-9]{1,30})/movies/new/?$', 'newmovie', name='newmovie'),
    url(r'^~([A-Za-z0-9]{1,30})/books/new/?$', 'newbook', name='newbook'),
    url(r'^~([A-Za-z0-9]{1,30})/games/new/?$', 'newgame', name='newgame'),
    url(r'^~([A-Za-z0-9]{1,30})/music/new/?$', 'newmusic', name='newmusic'),
    url(r'^~([A-Za-z0-9]{1,30})/tv/del/(\d+)$', 'deltv', name='deltv'),
    url(r'^~([A-Za-z0-9]{1,30})/movies/del/(\d+)$', 'delmovie', name='delmovie'),
    url(r'^~([A-Za-z0-9]{1,30})/books/del/(\d+)$', 'delbook', name='delbook'),
    url(r'^~([A-Za-z0-9]{1,30})/games/del/(\d+)$', 'delgame', name='delgame'),
    url(r'^~([A-Za-z0-9]{1,30})/music/del/(\d+)$', 'delmusic', name='delmusic'),

)

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/login/redirect$', 'whatitdo.views.login_redir', name='login_redir'),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/change_password/$', password_change, {'post_change_redirect' : '/accounts/change_password/done/'}),
    url(r'^accounts/change_password/done/$', password_change_done),
    url(r'^accounts/reset_password/$', password_reset),
    url(r'^accounts/password/reset/confirm/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm),
    url(r'^contact/?$', 'whatitdo.views.contact'),
    url(r'^contact/thanks/?$', 'whatitdo.views.contact_thanks'),
    url(r'^users/[A-Za-z0-9]{1,30}/$', lambda x: HttpResponseRedirect('/')),
)
