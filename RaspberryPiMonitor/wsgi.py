import os
import sys
import site
from django.core.wsgi import get_wsgi_application

def application(environ, start_response):
    if environ['mod_wsgi.process_group'] != '':
        import signal
        os.kill(os.getpid(), signal.SIGINT)
    return ["killed"]