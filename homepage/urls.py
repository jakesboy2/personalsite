from django.urls import path

from . import views

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('send-email-on-download', views.email_on_download, name='email_on_download'),
    path('kris-facts', views.kris_facts, name='kris_facts'),
    path('get-kris-fact', views.get_kris_fact, name='get_kris_fact'),
    path('screeps', views.screeps, name='screeps')
]