from django.contrib import admin
from django.urls import path,include
from app import views
# paxadi / use garne bani basa
urlpatterns = [
    path('',views.home,name='home'),
    path('blog/',views.blogs,name='blog'),
    path('makeblog/', views.register, name='hehe'),
    path("blogpost/<slug:page_slug>/", views.blogpost,name='name'),
    path('search/',views.search,name='search'),  
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('inp/',views.inp,name='inp'),
    path('postcomment/<int:id>/',views.postcomment,name='postcomment')
]


