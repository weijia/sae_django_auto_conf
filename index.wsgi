import sae

#def app(environ, start_response):
#    status = '200 OK'
#    response_headers = [('Content-type', 'text/html; charset=utf-8')]
#    start_response(status, response_headers)
#    return ['<strong>Welcome to SAE!</strong>']

import django.core.handlers.wsgi
from manage import initialize_settings
initialize_settings()
app = django.core.handlers.wsgi.WSGIHandler()

application = sae.create_wsgi_app(app)