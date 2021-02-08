from django.shortcuts import render
from django.views import generic
from .models import Post, ImagePost, VideoPost
from django.http import HttpResponse
from django.template import loader
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


    
def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    
    return render(request, template_name, {'post': post,
                                            })


def pic_feed(request):
    template_name = 'pic_feed.html'
    image_feed = ImagePost.objects.filter(status=1).order_by('-created_on')

    return render(request, template_name, {
                                            'image_feeds': image_feed,
                                            })

def pic_feed_detail(request, slug):
    template_name = "pic_feed_detail.html"
    image_feed = get_object_or_404(ImagePost, slug=slug)
    return render(request, template_name, {
                                            'feed': image_feed,
                                            })
    



    
def video_feed(request):
    template_name = 'video_feed.html'
    video_feed = VideoPost.objects.filter(status=1).order_by('-created_on')

    return render(request, template_name, {
                                            'video_feeds': video_feed,
                                            })


def video_feed_detail(request, slug):
    template_name = "video_feed_detail.html"
    video_feed = get_object_or_404(VideoPost, slug=slug)
    return render(request, template_name, {
                                            'feed': video_feed,
                                            })
    