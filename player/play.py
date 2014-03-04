def application(environ, start_response):
    start_response('200 OK', [('content-type', 'text/html')])
    return [b'<h1>Hello world</h1>']

def run_server():
    from wsgiref.simple_server import make_server
    print("Serving on http://localhost:4000...")
    make_server('localhost', 4001, application).serve_forever()
