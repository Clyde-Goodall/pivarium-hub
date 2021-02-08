import os
import django
from channels.routing import get_default_application

#It makes the websocket work, and that's about all I know
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tabulator.settings')
django.setup()
application = get_default_application()