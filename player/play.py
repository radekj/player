import configparser
import json
import os
from wsgiref.simple_server import make_server
from player.decision import Decision


def application(environ, start_response):
    """ Player wsgi application """
    start_response('200 OK', [('content-type', 'application/json')])
    request_body_size = int(environ['CONTENT_LENGTH'])
    request_body = environ['wsgi.input'].read(request_body_size)
    params = json.loads(request_body.decode('utf-8'))
    decision = Decision(params)
    result = decision.make_decison()
    response = json.dumps(result)
    return [response.encode('utf-8')]


def run_server():
    """ Running wsgi server """
    config = configparser.ConfigParser()
    config_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', 'config.ini')
    )
    config.read(config_path)
    host = config['server:main']['host']
    port = int(config['server:main']['port'])
    print("Serving on http://%s:%s..." % (host, port))
    make_server(host, port, application).serve_forever()
