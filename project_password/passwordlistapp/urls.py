from django.conf.urls import url
from . import views

urlpatterns = [
    # passw views
    # url(r'^$', views.passw_list, name='passw_list'),
    url(r'^$', views.PasswListView.as_view(), name='passw_list'),
    url( r'(?P<id>[\d]+)/$', views.passw_detail,name='passw_detail'),
]