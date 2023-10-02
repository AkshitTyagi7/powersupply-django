from django.urls import re_path 
from . import consumers

websocket_urlpatterns = [
    #Add the url of the websocket here which includes the user ids of the users involved in the chat
    re_path(r'summary', consumers.SummaryConsumer.as_asgi()),
]