from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    date = dt.date.today()
   
    return render(request, 'home.html', {"date": date})

