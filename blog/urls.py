from django.urls import path
from .views import post_edit, post_detail, post_new, services_view, about_view, home_view, contact_view

urlpatterns = [
    path('', home_view, name='home'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
]
