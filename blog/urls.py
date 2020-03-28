from django.urls import path
from .views import post_list, post_detail, post_new, post_edit, about_view, stack_view, contact_view

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/about/', about_view, name='about'),
    path('post/contact/', contact_view, name='about'),
    path('post/stack/', stack_view, name='stack'),
]
