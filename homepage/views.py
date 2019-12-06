from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import time
import random


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

@csrf_exempt
def kris_facts(request):
    app_url = request.path
    if request.method == 'GET' and 'key' in request.GET:
        security_key = request.GET['key']
    else:
        return HttpResponse(status=400)
    if security_key != '1234':
        return HttpResponse(status=403)
    
    # Return a random Kris Fact
    facts = [
        "Norwood? More like Nandwood",
        "Did you mean 'Chris'?",
        "Did you know Kris is an endangered species?",
        "Go Cowboys",
        "Kris: At least he's not Logan",
        "Did you know twenty-two billion billion billion Kris's can fit inside the sun? And we don't even want one of them!",
        "Have you ever noticed how gnome-like and stupid he is?",
        "Yeah I can't go to lunch, I just got here, can you bring me something back thoooo?",
        "I'm not gnome like though, more dwarf without the beard",
        "Kris enjoys: cat'ing out logs in his terminal to look busy.",
        "Kris is unable to watch Rick and Morty due to his dwindling IQ",
        "Kris is a good man",
        "Hold my diapers!",
        "Kris's bulking season is now dubbed 'Kris-mass'",
        "As Krispy as a Krispy Cracker",
        "Why isn't this working? *Slams Desk* uwu'",
        "The body does not turn because the face is not confident'",
        "Woooo!",
        "I love Tuckers",
        "I wish I was on Team Vector!",
        "I hate breast cancer supporters.",
        "Rest in peps",
        "I like my women like I like my coffee. Dark and bitter.",
        "You guy's don't?",
        "How often do men throw money at me? Often enough.",
        "I'm rebooting the server guys give me a second.",
        "Don't talk about my body, I don't have any armor.",
        "I'm weak-willed and thin-skinned.",
        "I love the new Carly Rae Jepsin album. It slaps!",
        "That's too bad.",
        "Bruuuuuh",
        "I love Gabe. He has Cooper's hair.",
        "I'm starving. Let's go eat!",
        "I don't like almonds, but I'm a fan of the almond brothers."
    ]

    random_fact = random.choice(facts)

    return render(request, 'kris.html', {'app_url': app_url, 'fact': random_fact })
