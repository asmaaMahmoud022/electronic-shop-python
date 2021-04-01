# list all proudcts app routes 
from django.urls import path
from django.conf.urls import url 
from .views import home

urlpatterns = [
    path('home', home.index, name='home'),
    url(r'^dept/(?P<dept_id>\d+)/$', home.depart, name='dept_filter'),
    path('search/', home.search, name='search'),  
    path('contact/', home.contact, name='contact'),   
    url(r'^product/(?P<item_id>\d+)/$', home.product, name='product'),
    path('about/', home.about, name='about'), 
    path('profile/', home.profile, name='profile'), 
     
]
