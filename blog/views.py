from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form = PostForm()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def about_view(request):
    my_context = {
        "page": "About",
        "title": "Family of knowledge hungry nerds",
        "this_is_true": True,
        "my_number": "A family of passionate hardworking devs and automation engineers",
        "my_list": [1313, 4231, 312, "Abc"],
        "my_html": "<h1>+10 years of industry expericne on Web dev; QA automation web, android and IOS & Devops services for infra</h1>"

    }
    return render(request, "about.html", my_context)


def stack_view(request):
    my_context = {
        "page": "Stack",
        "title": "Services & Stack",
        "this_is_true": True,
        "my_number": "Years of experience: 10",
        "my_list": [1313, 4231, 312, "Abc"],
        "my_html": "<h1>Java / Junit / Selenium / Postman / Testrail / CI+CD</h1>"

    }
    return render(request, "stack.html", my_context)


def contact_view(request):
    my_context = {
        "page": "Contact",
        "title": "contact@tautologico.com",
        "my_html": "<h1>Phone : 6502858613</h1>"

    }
    return render(request, "contact.html", my_context)
