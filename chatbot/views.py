from django.shortcuts import render, redirect
from chatbot.models import Message
import cleverbot

cb = cleverbot.Cleverbot('CC4zfUgbrPndTHT3tLdz3q9-2DA')


def home(request):
    messages = Message.objects.all()
    return render(request, 'index.html', context={'messages': messages})


def say(request):
    if request.method == "POST":
        message = request.POST["message"]
        msg = Message.objects.create(message=message, is_bot=False)
        msg.save()
        reply = cb.say(message)
        msg2 = Message.objects.create(message=reply, is_bot=True)
        msg2.save()
    return redirect("/")


def clear(request):
    Message.objects.all().delete()
    return redirect("/")

