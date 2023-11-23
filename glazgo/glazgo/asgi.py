"""
ASGI config for glazgo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.routing import URLRouter, ProtocolTypeRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from chat import routing
from .tokenauth_middleware import TokenAuthMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "glazgo.settings")

# Переменной application присваивается объект ProtocolTypeRouter. Этот объект отвечает за
# маршрутизацию входящих запросов к соответствующему приложению, зависящему от протокола.
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            TokenAuthMiddleware(URLRouter(routing.websocket_urlpatterns))
        ),
    }
)
