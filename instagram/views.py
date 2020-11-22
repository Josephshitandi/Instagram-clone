from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import Image,Comment,Profile
from .forms import NewPostForm,ProfileForm,CommentForm

# Create your views here.
def index(request):
    date = dt.date.today()
    images = Image.objects.all()
    users = Profile.objects.all()
    return render(request, 'home.html', {"date": date,"images":images, "users":users})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.Author = current_user
            post.save()
        return redirect('newsToday')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.Author = current_user
            post.save()
        return redirect('newsToday')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

def search_results(request):

    if 'Author' in request.GET and request.GET["Author"]:
        Author = request.GET.get("Author")
        Author = Image.search_by_author(Author)
        message = f"{Author}"

        return render(request, 'search.html',{"message":message,"Author":Author})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
    
    
@login_required(login_url='/accounts/login/')
def new_comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.Author = current_user
            post.save()
        return redirect('newsToday')

    else:
        form = CommentForm()
    return render(request, 'new_comment.html', {"form": form})
