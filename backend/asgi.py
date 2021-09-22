import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from location.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

django_asgi_app = get_asgi_application()

ws_patterns = [
    path('ws/location/', LocationConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(ws_patterns)
    )
})

