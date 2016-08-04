import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/pi/py3env/lib/python3.4/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/pi/RaspberryPiMonitor/')
sys.path.append('/home/pi/RaspberryPiMonitor/RaspberryPiMonitor')

os.environ['DJANGO_SETTINGS_MODULE'] = 'RaspberryPiMonitor.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/home/pi/py3env/bin/activate_this.py")
# execfile(activate_env, dict(__file__=activate_env))
exec(compile(open(activate_env, "rb").read(), activate_env, 'exec'), dict(__file__=activate_env))

application = get_wsgi_application()