"""
ASGI config for viral project.
It exposes the ASGI callable as a module-level variable named ``channel_layer``.
For more information on this file, see
https://asgi.readthedocs.io/en/latest/
"""
import os
import dotenv
from channels.asgi import get_channel_layer
dotenv.read_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'src.config.local')

channel_layer = get_channel_layer()
