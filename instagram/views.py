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
    
    current_user = request.user 
    if request.method == 'POST':
        form = CommentForm(request.POST, auto_id=False)
        img_id = request.POST['image_id']
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = current_user
            image = Image.get_image(img_id)
            comment.image = image
            comment.save()
        return redirect(f'/#{img_id}',)
    else:
        form = CommentForm(auto_id=False)
    # comments = Comment.get_comment_by_id(int(id)).count()
    return render(request, 'home.html', {"date": date,"images":images, "users":users, "form": form})
    # return render(request, 'index.html', {"date": date,"images":images, "form": form, "users":users})


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

@login_required(login_url='/accounts/login/')
def get_image(request, id):
    comments = Comment.get_comment()

    try:
        image = Image.objects.get(pk = id)        
        
    except ObjectDoesNotExist:
        raise Http404()
    
    current_user = request.user 
    if request.method == 'POST':
        form = CommentForm(request.POST, auto_id=False)
        img_id = request.POST['image_id']
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = current_user
            image = Image.get_image(img_id)
            comment.image = image
            comment.save()
            return redirect(f'/image/{img_id}',)
    else:
        form = CommentForm(auto_id=False)
    
    return render(request, "images.html", {"image":image, "form":form, "comments":comments})
