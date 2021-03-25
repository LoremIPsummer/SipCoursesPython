"""
This script runs the application using a development server.
"""

import bottle
import os
import sys

# routes contains the HTTP handlers for our server and must be imported.
import routes

if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    bottle.debug(True)

def wsgi_app():
    return bottle.default_app()

if __name__ == '__main__':
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = 13224
    except ValueError:
        PORT = 13225


    # Starts a local test server.
    bottle.run(server='wsgiref', host=HOST, port=13224)
