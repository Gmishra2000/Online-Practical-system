from django.urls import path
from django.conf.urls import url
from . import views

#urlpatterns = [
#    url('',views.index1, name='index1'),
#    url('^',views.Subjects, name='Subjects')
#]

urlpatterns = [
    url(r'^$', views.index1.as_view(), name='index1'), # Notice the URL has been named
    url(r'^Subjects/$', views.Subjects.as_view(), name='Subjects'),
     url(r'^List/$', views.List.as_view(), name='List'),
     url(r'^Ide/$', views.Ide.as_view(), name='Ide'),
]