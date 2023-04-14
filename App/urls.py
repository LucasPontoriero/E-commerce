from django.urls import path
from App.views import home 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="Home"),
    
    
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)