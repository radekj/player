import json
import multiprocessing
import unittest
import http.client
from test import test_support
from wsgiref.simple_server import make_server

from player.play import application


class TestCase(unittest.TestCase):

    # default values
    host = 'localhost'
    port = 4010
    content_type = 'application/json'
    data = {
        'limit': 10,
        'hand': [('S', '7'), ('H', '3')],
        'min': 2,
        'table': [],
        'can_raise': True,
        'pot': 3,
        'account': 500
    }

    def setUp(self):
        """ Setting up server """
        server = make_server(self.host, self.port, application)
        self.server_process = multiprocessing.Process(
            target=server.serve_forever)
        self.server_process.start()

    def tearDown(self):
        """ Shutting down server """
        self.server_process.terminate()
        self.server_process.join()
        del(self.server_process)

    def _get_response(self, data):
        """ Getting response from the player server for given parameters """
        conn = http.client.HTTPConnection('%s:%s' % (self.host, self.port))
        params = json.dumps(data)
        headers = {'Content-type': self.content_type}
        conn.request('POST', '/', params, headers)
        response = conn.getresponse()
        return response

    def _get_decision(self, response):
        return json.loads(response.read().decode('utf-8'))

    def _validate_response(self, data):
        response = self._get_response(data)
        decision = self._get_decision(response)

        msg = 'Server response error'
        assert (response.status == 200), msg

        msg = 'Bet: %s exceeds maximal limit: %s' % (decision, data['limit'] + data['min'])
        assert (decision <= data['limit'] + data['min']), msg

        msg = 'Non-zero bet %s smaller than mininal possible %s' % \
            (decision, data['min'])
        assert (decision >= data['min'] or decision == 0), msg

        msg = 'Bet: %s higher than account: %s' % (decision, data['account'])
        assert (decision <= data['account']), msg

        if not data['can_raise']:
            msg = 'Raise bet: %s when raise is not allowed' % (decision)
            assert (decision == 0 or decision == data['min']), msg

    def test_sample_data1(self):
        """ Testing the response for the sample data """
        self._validate_response(self.data)

    def test_sample_data2(self):
        """ Testing the response for the sample data """
        data = self.data
        data['can_raise'] = False
        data['hand'] = [('S', 'A'), ('H', 'A')]
        data['table'] = [('C', 'A'), ('D', 'A'), ('D', 'K')]
        self._validate_response(data)

    def test_sample_data3(self):
        """ Testing the response for the sample data """
        data = self.data
        data['can_raise'] = True
        data['hand'] = [('S', 'A'), ('H', 'A')]
        data['table'] = [('C', 'A'), ('D', 'A'), ('D', 'K')]
        self._validate_response(data)

    def test_sample_data4(self):
        """ Testing the response for the sample data """
        data = self.data
        data['can_raise'] = True
        data['hand'] = [('S', '2'), ('H', '5')]
        data['table'] = [('C', '7'), ('D', '9'), ('D', 'K')]
        self._validate_response(data)

    def test_sample_data5(self):
        """ Testing the response for the sample data """
        data = self.data
        data['can_raise'] = True
        data['hand'] = [('S', 'A'), ('H', 'A')]
        data['table'] = [('C', 'A'), ('D', 'A'), ('D', 'K')]
        data['account'] = 1
        self._validate_response(data)


def test_main():
    test_support.run_unittest(TestCase,)

if __name__ == '__main__':
    test_main()
