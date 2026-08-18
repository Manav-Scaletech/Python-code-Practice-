from django.urls import path

from websocket.consumers import ChatConsumer


websocket_urlpatterns = [
    path(
        "ws/chat/",
        ChatConsumer.as_asgi(),
    ),
]
