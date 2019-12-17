from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import time
import random
from  .constants import facts

# Create your views here.

# Render the home page
def index(request):
    app_url = request.path
    year = time.strftime("%Y")
    age = int(year) - 1995
    return render(request, 'home.html', { 'app_url': app_url, 'age': age })

# Render the screeps page
def screeps(request):
    app_url = request.path
    return render(request, 'screeps.html', {'app_url': app_url})

# Send an email to myself when my resume is downloaded
@csrf_exempt
def email_on_download(request):
    send_mail(
        'Resume Downloaded',
        'Your resume was just downloaded on your personal site.',
        'jakeywaldrip@gmail.com',
        ['jakeywaldrip@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse(status=204)

@csrf_exempt
def kris_facts(request):
    app_url = request.path
    if request.method == 'GET' and 'key' in request.GET:
        security_key = request.GET['key']
    else:
        return HttpResponse(status=400)
    if security_key != '1234':
        return HttpResponse(status=403)
    
    random_fact = random.choice(facts)

    return render(request, 'kris.html', {'app_url': app_url, 'fact': random_fact })

@csrf_exempt
def get_kris_fact(request):

    app_url = request.path
    if request.method == 'GET' and 'key' in request.GET:
        security_key = request.GET['key']
    else:
        return HttpResponse(status=400)
    if security_key != '1234':
        return HttpResponse(status=403)

    random_fact = random.choice(facts)
    return JsonResponse({'fact': random_fact})
