from django.urls import path, re_path
from django.utils import archive

from .views import *

urlpatterns =[
    path('', index, name = 'home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),

    #path('chat/<int:chat_id>/', home),
    #re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive'),

]
