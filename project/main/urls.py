"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from .views import *

app_name = "main"
urlpatterns = [
    path('', showindex, name="index"),
    path('<int:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('users/',include('users.urls')),
    path('<str:post_id>/create_comment/', create_comment, name="create_comment"),
    path('<str:post_id>/edit_comment/<str:comment_id>', edit_comment, name="edit_comment"),
    path('<str:post_id>/update_comment/<str:comment_id>', update_comment, name="update_comment"),
    path('<str:post_id>/delete_comment/<str:comment_id>', delete_comment, name="delete_comment"),
    path('create_guestbook/', create_guestbook, name="create_guestbook"),
    path('delete_comment/<int:id>', delete_guestbook, name="delete_guestbook"),

]
