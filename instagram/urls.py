from django.urls import path,re_path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.index, name = 'newsToday'),
    path('search/', views.search_results, name='search_results'),
    # re_path('archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    # path('article/(\d+)',views.article,name ='article'),
    path('new/post', views.new_post, name='new_post'),
    path('accounts/profile', views.Profile, name='profile')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)