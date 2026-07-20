import os
import sys

path = '/home/tonpseudo/fadlab'  # chemin vers ton projet
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'fadlab.settings'  # adapte au nom de ton module settings

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
