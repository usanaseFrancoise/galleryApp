from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    url(r'^$',views.index,name='index'),
    url(r'^images/(\d+)',views.image,name = 'image'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(\d+)',views.filter_by_location,name ='location')

]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)