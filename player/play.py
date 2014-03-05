import json
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server
from player.decision import make_decisom

def application(environ, start_response):
    start_response('200 OK', [('content-type', 'application/json')])
    request_body_size = int(environ['CONTENT_LENGTH'])
    request_body = environ['wsgi.input'].read(request_body_size)
    params = json.loads(request_body.decode('utf-8'))
    result = make_decisom(params)
    response = json.dumps(result)
    return [response.encode('utf-8')]

def run_server():
    print("Serving on http://localhost:4000...")
    make_server('localhost', 4000, application).serve_forever()
