from django.contrib import admin
from django.urls import path, include
from polls.views import Index, About, register, Contact, login, Gallery, Cart, Mbrid, Description, Charbrid, Skybrid, Sunbrid, Harmbrid,Videog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
    # path('', Index, name='index'), 
    # path('about/', About, name='about'),   
    # path('register/', register, name='register'),  
    # path('login/', login, name='login'),  
    # path('contact/', Contact, name='contact'),  
    # path('gallery/', Gallery, name='gallery'),  
    
]

# Add static and media URL patterns only when DEBUG is True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
