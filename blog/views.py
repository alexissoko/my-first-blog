from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
# new imports that go at the top of the file
from django.template.loader import get_template
from blog.forms import ContactForm


# our view
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                "page": "Contact",
                "title": "contact@tautologico.com",
                "my_html": "<h1>Phone : 6502858613</h1>",
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'blog/contact.html', {
        'form': form_class,
    })

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
        "title": "Tautologico came up to be with family and fiends with common professional interest with a keen for innovation",
        "this_is_true": True,
        "my_number": "Our staff is marked mostly by strong proffesional ethics and a sophisticated software engineering heuristics honed over a decade-plus years top industry experience",
        "my_list": [1313, 4231, 312, "Abc"],
        "my_html": "<h1>Hard working, capable and hungry engineers</h1>"

    }
    return render(request, "nav_bar.html", my_context)


def home_view(request):
    my_context = {
        "page": "Pragmatic scalable teams",
        "title": "easy synch up with inhouse department",
        "this_is_true": True,
        "my_number": "Years of experience: 10",
        "my_list": [1313, 4231, 312, "Abc"],
        "my_html": "Web devs, SDET's and Devops Agile teams"

    }
    return render(request, "nav_bar.html", my_context)


def contact_view_2(request):
    my_context = {
        "page": "Contact",
        "title": "contact@tautologico.com",
        "my_html": "<h1>Phone : 6502858613</h1>"

    }
    return render(request, "nav_bar.html", my_context)


def contact_view(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['contact@tautologico.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')



def careers_view(request):
    my_context = {
        "page": "Careers",
        "title": "Dev ops engineer",
        "my_html": "<h1>3 Years experience with Bash scriptting and TCP/IP</h1>"

    }
    return render(request, "nav_bar.html", my_context)
