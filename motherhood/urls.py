from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^about',views.about,name='about'),
    url(r'^contact',views.contact,name='contact'),
    url(r'^nannies',views.nannies,name='nannies'),
    url(r'^pricing',views.pricing,name='pricing'),
    url(r'^services',views.services,name='services'),
    url(r'^testimonial',views.testimonial,name='testimonial'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
