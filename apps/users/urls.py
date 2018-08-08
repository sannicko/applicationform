from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = [
            	url(r'register/$', UserHome.as_view(),name="user_home"),
            	url(r'submitForm$',form_submit, name="submit_form"),
            	url(r'logout/$', LogoutView,name="user_logout"),
				url(r'work/$', generate, name='generate'),
             ]