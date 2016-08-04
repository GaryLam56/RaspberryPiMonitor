import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/pi/py3env/lib/python3.4/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/pi/RaspberryPiMonitor/')
sys.path.append('/home/pi/RaspberryPiMonitor/RaspberryPiMonitor')

os.environ['DJANGO_SETTINGS_MODULE'] = 'RaspberryPiMonitor.production_settings'

# Activate your virtual env
activate_env=os.path.expanduser("/home/pi/py3env/bin/activate_this.py")
# execfile(activate_env, dict(__file__=activate_env))
exec(compile(open(activate_env, "rb").read(), activate_env, 'exec'), dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()