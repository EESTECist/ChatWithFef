from django.shortcuts import render
import cleverbot

# Create your views here.
def home(request):
    cb = cleverbot.Cleverbot('CC4zfUgbrPndTHT3tLdz3q9-2DA')
    reply = cb.say('What is the meaning of life?')
    return render(request, 'index.html', context={'name': reply})
