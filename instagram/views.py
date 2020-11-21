from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import Image,Comment,Profile

# Create your views here.
def index(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render(request, 'home.html', {"date": date,"images":images})

