from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import time


# Create your views here.

# Render the home page
def index(request):
    app_url = request.path
    year = time.strftime("%Y")
    age = int(year) - 1995
    return render(request, 'home.html', { 'app_url': app_url, 'age': age })

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