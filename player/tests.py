import json
import multiprocessing
import unittest
import http.client
from test import test_support
from wsgiref.simple_server import make_server

from player.play import application


class TestCase(unittest.TestCase):

    host = 'localhost'
    port = 4000
    content_type = 'application/json'

    def setUp(self):
        server = make_server(self.host, self.port, application)
        self.server_process = multiprocessing.Process(
            target=server.serve_forever
        )
        self.server_process.start()

    def tearDown(self):
        self.server_process.terminate()
        self.server_process.join()
        del(self.server_process)

    def _get_response(self, data):
        conn = http.client.HTTPConnection('%s:%s' % (self.host, self.port))
        params = json.dumps(data)
        headers = {'Content-type': self.content_type}
        conn.request('POST', '/', params, headers)
        response = conn.getresponse()
        return response

    def test_one(self):
        data = {
            'limit': 10,
            'hand': [('S', '7'), ('H', '3')],
            'min': 2,
            'table': [],
            'can_raise': True,
            'bids': {},
            'pot': 3,
            'account': 500
        }
        r = self._get_response(data)
        assert (r.status == 200), 'Server response error!'

def test_main():
    test_support.run_unittest(TestCase,)

if __name__ == '__main__':
    test_main()
