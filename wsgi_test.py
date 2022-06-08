# pull master boostrap enviornmental variables
import logging
import os
import sys
# it's possible to run the demo app if necessary (but we're not doing that)
from wsgiref.simple_server import demo_app, make_server

import brew
import os
from django.core.wsgi import get_wsgi_application
from brew import settings
from whitenoise import WhiteNoise
from pip._internal.operations import freeze

settings_string = 'brew.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_string)

def test_wsgi_mode(environ, start_response):
    thisfreeze = ''
    x = freeze.freeze()
    for p in x:
        thisfreeze += p + '  |  '
    status = '200 OK'
    output = u'test_wsgi_mode(): brew works - 10:00' + thisfreeze

    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(output)))]

    start_response(status, response_headers)

    return [output.encode('UTF-8')]

application = get_wsgi_application()
# application = WhiteNoise(application)

# tests wsgi mode: https://modwsgi.readthedocs.io/en/master/user-guides/reloading-source-code.html
# application = WhiteNoise(test_wsgi_mode, max_age=59)
# application = WhiteNoise(application, max_age=59)

if __name__ == "__main__":
    # wsgi.application is the django app created to run with wagtail
    with make_server('', 911, application) as httpd:
        message = "wsgi_test.py Serving HTTP via wsgiref.simple_server at http://127.0.0.1:911"
        print(message)
        httpd.serve_forever()
