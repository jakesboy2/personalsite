from django.urls import path

from . import views

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('send-email-on-download', views.email_on_download, name='email_on_download')
]