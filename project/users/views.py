from django.shortcuts import render, get_object_or_404, redirect
from main.models import Post, Guestbook, Comment
from django.contrib.auth.models import User
# Create your views here.
def mypage(request, id):
    user=get_object_or_404(User, pk=id)
    comments=Comment.objects.filter(writer=user)
    context={
        'user': user,
        'comments': comments,
        'followings': user.profile.followings.all(),
        'followers': user.profile.followers.all(),
        'guestbooks': Guestbook.objects.all(),
    }
    return render(request, 'users/mypage.html', context)
    
def follow(request, id):
    user=request.user
    followed_user = get_object_or_404(User, pk=id)
    is_follower=user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)