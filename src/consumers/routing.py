from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter

from src.consumers.middlewares import TokenAuthMiddlewareStack
from src.consumers.echo_consumer import EchoConsumer


application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    # 'http': application,

    # websockets
    'websocket': TokenAuthMiddlewareStack(
        URLRouter([
            path('echo/', EchoConsumer)
        ])
    )
})
