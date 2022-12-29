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
    path('<int:pk>/update/', views.Updatepost.as_view(),name='update_post'),
    path('blogpost-like/<int:pk>', views.like_post, name="blogpost_like"),
    path('<int:id>/delete/', views.delete_post,name='delete_post'),
    path('like/', views.like_post, name='like-post'),
    # user 
    path('register/', views.registerpage,name='register'),
    path('login/', views.loginpage,name='login'),
    path('logout/', views.logoutuser,name='logout'),
 ] 



# from .views import PostListView
  
# ''' using CBV '''

# urlpatterns = [
#     #path('', PostListView.as_view(),name='index'),

# ]
