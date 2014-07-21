import settings, signals
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import *
from django.http import HttpResponseRedirect
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import userhome, userpic, editlinks, listsort, item_list, edit_item, delete_item
admin.autodiscover()

urlpatterns = patterns('whatitdo.views',
    url(r'^~?$', 'frontpage', name='frontpage'),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/?$', userhome),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/userpic/?$', userpic),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/editlinks/?$', editlinks),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/listsort/?$', listsort),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/tv/?$', item_list, {'category':'tv'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/movies/?$', item_list, {'category':'movie'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/books/?$', item_list, {'category':'book'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/games/?$', item_list, {'category':'game'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/music/?$', item_list, {'category':'music'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/tv/edit/(?P<pk>\d+)/?$', edit_item, {'category':'tv'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/movies/edit/(?P<pk>\d+)/?$', edit_item, {'category':'movie'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/books/edit/(?P<pk>\d+)/?$', edit_item, {'category':'book'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/games/edit/(?P<pk>\d+)/?$', edit_item, {'category':'game'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/music/edit/(?P<pk>\d+)/?$', edit_item, {'category':'music'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/tv/new/?$', edit_item, {'category':'tv'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/movies/new/?$', edit_item, {'category':'movie'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/books/new/?$', edit_item, {'category':'book'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/games/new/?$', edit_item, {'category':'game'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/music/new/?$', edit_item, {'category':'music'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/tv/del/(?P<pk>\d+)$', delete_item, {'category':'tv'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/movies/del/(?P<pk>\d+)$', delete_item, {'category':'movie'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/books/del/(?P<pk>\d+)$', delete_item, {'category':'book'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/games/del/(?P<pk>\d+)$', delete_item, {'category':'game'}),
    url(r'^~(?P<list_owner>[A-Za-z0-9]{1,30})/music/del/(?P<pk>\d+)$', delete_item, {'category':'music'}),
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

urlpatterns += staticfiles_urlpatterns()
