from django.conf.urls import url
from chatbot.views import home

urlpatterns = [
    url(r'^$', home, name="home")
]
