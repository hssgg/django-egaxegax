from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_books),
    url(r'^read/(?P<ind>[0-9]*)/(?P<part>.*)/?$', views.read_book),
    url(r'^read/(?P<tr_wrt>[^/]*)/(?P<tr_titl>[^/]*)/(?P<ind>[0-9]*)/(?P<part>.*)/?$', views.read_book),
    url(r'^get_file/(?P<ind>[0-9]*)/?$', views.get_file),
    url(r'^wrt/i/(?P<ind_wrt>[0-9]*)/?$', views.list_wrt),
    url(r'^wrt/?$', views.list_wrt),
    url(r'^wrt/(?P<id_wrt>[0-9]*)/?$', views.list_books),
    url(r'^wrt/(?P<tr_wrt>[^/]*)/(?P<id_wrt>[0-9]*)/?$', views.list_books),
    url(r'^subj/?$', views.list_subj),
    url(r'^subj/(?P<id_subj>[0-9]*)/?$', views.list_books),
    url(r'^subj/(?P<tr_subj>[^/]*)/(?P<id_subj>[0-9]*)/?$', views.list_books),
    url(r'^add/?$', views.add_book),
    url(r'^del/(?P<id>[0-9]*)/?$', views.delete_book),
    url(r'^edit/(?P<id>[0-9]*)/?$', views.edit_book),
    url(r'^edit_wrt/(?P<id>[0-9]*)/?$', views.edit_wrt),
    url(r'^user/(?P<id>[0-9]*)/?$', views.user_profile),
]
