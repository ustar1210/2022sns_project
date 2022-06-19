from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.utils import timezone
# Create your views here
def showindex(request):
    posts = Post.objects.all()
    return render(request, 'main/index.html',{'posts':posts})

def showintroduction(request):
    return render(request, 'main/introduction.html')

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'main/detail.html', {'post':post, 'comments':all_comments})

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