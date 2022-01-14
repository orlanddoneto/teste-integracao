import json
import unittest
from nose.tools import *
import requests

from utils.main_functions import *


class TestTimeZone(unittest.TestCase):
    def setUp(self):
        self.header = {'Authorization': auth_token()}

    def test_get_TimeZone(self):
        response = requests.get(f"{URL}/timezone", headers=self.header)
        assert_equal(response.status_code, 200)

        json_data = json.loads(response.content)

        for zones in json_data:
            assert_in('id', zones)
            assert_equal(type(zones['id']),int)

            assert_in('name',zones)
            assert_equal(type(zones['name']),str)

            assert_in('timeAdjustment',zones)
            assert_equal(type(zones['timeAdjustment']),str)

            assert_in('active',zones)
            assert_equal(type(zones['active']), bool)



