from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.home),
    url(r'^search/', views.search_results, name='search_results'),
    url(r"^page/",views.page, name = "location"),
    url(r"^location/(\w+)",views.location, name = "locations")

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
