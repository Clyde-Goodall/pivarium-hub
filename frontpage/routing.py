from django.urls import path
from channels.auth import AuthMiddlewareStack
from . import consumers
from channels.routing import ProtocolTypeRouter, URLRouter


# assigns websocket to a consumer, located in consumers.py
websockets = URLRouter([
    path (
        "ws/station/",
        consumers.StationConsumer.as_asgi()

    ),
    path(
        "ws/frontend/",
        consumers.DataSyncConsumer.as_asgi()
    )
])

#runs websocket through the authmiddleware stack
application = ProtocolTypeRouter({

    "websocket": AuthMiddlewareStack(websockets)

})

