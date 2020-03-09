from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from .api import router

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Redirect index to the homepage as it is the true homepage
    path('', lambda request: redirect('/home/', permanent=True)),
    
    # Home Page App
    path('home/', include('homepage.urls')),

    # API Paths
    path('api/v1/', include(router.urls))


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)