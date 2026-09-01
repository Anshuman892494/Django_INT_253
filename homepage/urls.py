from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('result/', views.result, name='result'),
    path('result/<int:marks>/', views.result),

# Inerting Items
    path('items/', views.dictionary, name='items'),
    

# Greeting
    path('greet/<str:name>/', views.greet, name='greet'),

# Dynamic Item (Path Parameter)
    path('item/<str:item>/', views.dict, name='item_detail'),

# Query Parameter Routes (Notice: no converter in path)
    path('profile/', views.profile, name='profile'),
    path('search/', views.search_item, name='search_item'),


# ===========================================================================(28-08-2026)

# Regular Expression
    re_path(
        # r'^user/(?P<username>[A-Za-z]+)/$',
        r'^user/(?P<username>[\w-]+)/$',
        views.user_profile,
        name='user_profile'
    ),  

# r' = raw string / ko ignore nhi krta h,  () = capturing group 

    re_path(
        # r'^item_id/(?P<item_id>[0-9]{5}+)/?$',
        # r'^item_id/(?P<item_id>\d+)/?$',
        r'^item_id/(?P<item_id>\d{3,6}+)/?$', #with limit {3}
        views.item_detail,
        name='item_detail'
    ),  

    re_path(
        r'^restro/(?P<category>[\w-]+)/(?P<subcategory>[\w-]*)?$',
        views.restro_details,
        name='resto_details'
    ),

# =======================================================================(01/09/2026)

    path('dash/', views.dash, name='home'),

    path('aboutus/', views.aboutus, name='aboutus'),

    path('filterdemo/', views.filterdemo, name='filterdemo'),

]