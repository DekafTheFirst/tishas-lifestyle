from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name = 'home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('pics', views.pic_feed, name= 'pics'),  
    path('pics/<slug:slug>/', views.pic_feed_detail, name= 'pic_feed_detail'),    
    path('videos', views.video_feed, name= 'videos'), 
    path('videos/<slug:slug>/', views.video_feed_detail, name= 'video_feed_detail'),    
]
