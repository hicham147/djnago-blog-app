from django.contrib import admin
from django.urls import path
from . import views
''' using FBV '''

urlpatterns = [
    path('', views.index,name='index'),
    path('author/', views.author,name='author'),
    path('post/', views.post,name='post'),
    path('detail/<int:id>/', views.detail_view,name='detail'),
    path('create_post/', views.Create_post,name='create_post'),
    
 ]


# from .views import PostListView
  
# ''' using CBV '''

# urlpatterns = [
#     #path('', PostListView.as_view(),name='index'),

# ]
