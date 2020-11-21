from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import Image,Comment,Profile
from .forms import NewPostForm

# Create your views here.
def index(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render(request, 'home.html', {"date": date,"images":images})


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

