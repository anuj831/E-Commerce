from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('', views.Index, name='index'),
    path('about/', views.About, name='about'),
    path('register/', views.register, name='register'),  # Ensure this view is correct
    path('login/', views.login, name='login'),
    path('contact/', views.Contact, name='contact'),
    path('aboutus/', views.About, name='aboutus'),  # Ensure this view is correct
    path('gallery/', views.Gallery, name='gallery'),
    path('cart/', views.Cart, name='cart'),
    path('payment/', views.Payment, name='payment'),
    path('Mbrid/', views.Mbrid, name='mbrid'),
    path('Charbrid/', views.Charbrid, name='charbrid'),
    path('Skybrid/', views.Skybrid, name='skybrid'),
    path('Sunbrid/', views.Sunbrid, name='sunbrid'),
    path('Harmbrid/', views.Harmbrid, name='harmbrid'),
    path('Description/', views.Description, name='description'),
    path('Videog/', views.Videog, name='videog'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
