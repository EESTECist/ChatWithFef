from django.conf.urls import url
from chatbot.views import home, say, clear

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^say$', say, name="say"),
    url(r'^clear$', clear, name="clear")
]
