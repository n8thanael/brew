"""
WSGI config for brew project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import brew
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

def test_wsgi_mode(environ, start_response):
    status = '200 OK'

    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp = pprint.PrettyPrinter()
    pp.pprint(os.environ)

    key='mod_wsgi.process_group'
    if key not in environ.keys():
    # if not environ['mod_wsgi.process_group']:
      output = u'test_wsgi_mode(): EMBEDDED MODE - brew works'
    else:
      output = u'test_wsgi_mode(): DAEMON MODE - brew works'

    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(output)))]

    start_response(status, response_headers)

    return [output.encode('UTF-8')]


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brew')

application = get_wsgi_application()
application = WhiteNoise(application, max_age=59)

# tests wsgi mode: https://modwsgi.readthedocs.io/en/master/user-guides/reloading-source-code.html
# application = WhiteNoise(test_wsgi_mode, max_age=59)

