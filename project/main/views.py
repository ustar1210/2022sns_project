from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Like, Dislike, Guestbook
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import json


def showindex(request):
    posts = Post.objects.all()
    guestbooks = Guestbook.objects.all()
    return render(request, 'main/index.html',{
        'posts':posts,
        'guestbooks': guestbooks,

        })
 
def showintroduction(request):
    guestbooks = Guestbook.objects.all()
    return render(request, 'main/introduction.html', {
        'guestbooks': guestbooks,
    })

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    guestbooks = Guestbook.objects.all()
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'main/detail.html', {
        'post':post, 
        'comments':all_comments, 
        'guestbooks': guestbooks,
        })

def new(request):
    return render(request, 'main/new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('main:detail', new_post.id)

def edit(request, id):
    edit_post = Post.objects.get(id = id)
    return render(request, 'main/edit.html', {'post' : edit_post})

def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer =  request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.image = request.FILES.get('image')
    update_post.save()
    return redirect('main:detail', update_post.id)

def delete(request , id):
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect('main:index')

def create_comment(request, post_id):
    new_comment = Comment()
    new_comment.writer = request.user
    new_comment.content = request.POST['content']
    new_comment.post = get_object_or_404(Post, pk=post_id)
    new_comment.save()
    return redirect('main:detail', post_id)

def edit_comment(request, post_id, comment_id):
    target_post = Post.objects.get(id = post_id)
    edit_comment = Comment.objects.get(id = comment_id)
    return render(request, 'main/edit_comment.html', {'post':target_post, 'comment' : edit_comment})

def update_comment(request, post_id, comment_id):
    target_post = Post.objects.get(id = post_id)
    update_comment = Comment.objects.get(id=comment_id)
    update_comment.content = request.POST['content']
    update_comment.writer =  request.user
    update_comment.save()
    return redirect('main:detail', target_post.id)
  
def delete_comment(request , post_id, comment_id):
    target_post = Post.objects.get(id = post_id)
    delete_comment = Comment.objects.get(id = comment_id)
    delete_comment.delete()
    return redirect('main:detail', target_post.id)

@require_POST
@login_required
def like_toggle(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post_like, post_like_created = Like.objects.get_or_create(user=request.user, post=post)

    if not post_like_created:
        post_like.delete()
        result = "like_cancel"
    else:
        result = "like"
    context = {
        "like_count" : post.like_count,
        "result" : result
    }
    return HttpResponse(json.dumps(context), content_type = "application/json")

@require_POST
@login_required
def dislike_toggle(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post_dislike, post_dislike_created = Dislike.objects.get_or_create(user=request.user, post=post)

    if not post_dislike_created:
        post_dislike.delete()
        result = "dislike_cancel"
    else:
        result = "dislike"
    context = {
        "dislike_count" : post.dislike_count,
        "result" : result
    }
    return HttpResponse(json.dumps(context), content_type = "application/json")



def create_guestbook(request):
    guestbook = Guestbook()
    guestbook.writer = request.user
    guestbook.pub_date = timezone.now()
    guestbook.body = request.POST['body']
    guestbook.save()
    return redirect('main:index')

def delete_guestbook(request , id):
    delete_guestbook = Guestbook.objects.get(id = id)
    delete_guestbook.delete()
    return redirect('main:index')
