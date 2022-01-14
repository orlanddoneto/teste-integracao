import json
import unittest
from nose.tools import *
import requests

from utils.main_functions import *


class TestUserProfile(unittest.TestCase):
    def setUp(self):
        self.header = {'Authorization': auth_token()}

    def test_get_UserProfile(self):
        response = requests.get(f"{URL}/user-profile", headers=self.header)
        assert_equal(response.status_code, 200)

        json_data = json.loads(response.content)

        languages = json_data['languages']

        portuguese = languages[0]
        assert_in("id", portuguese)
        assert_equal(type(portuguese['id']), int)
        assert_equal(portuguese['id'], 1)

        assert_in("name", portuguese)
        assert_equal(type(portuguese['name']), str)
        assert_equal(portuguese['name'], "Português")

        assert_in("code", portuguese)
        assert_equal(type(portuguese['code']), str)
        assert_equal(portuguese['code'], "pt")

        english = languages[1]
        assert_in("id", english)
        assert_equal(type(english['id']), int)
        assert_equal(english['id'], 2)

        assert_in("name", english)
        assert_equal(type(english['name']), str)
        assert_equal(english['name'], "English")

        assert_in("code", english)
        assert_equal(type(english['code']), str)
        assert_equal(english['code'], "en")

        spanish = languages[2]
        assert_in("id", spanish)
        assert_equal(type(spanish['id']), int)
        assert_equal(spanish['id'], 3)

        assert_in("name", spanish)
        assert_equal(type(spanish['name']), str)
        assert_equal(spanish['name'], "Español")

        assert_in("code", spanish)
        assert_equal(type(spanish['code']), str)
        assert_equal(spanish['code'], "es")

        timezones = json_data['timezones']
        for zones in timezones:
            assert_in('id', zones)
            assert_equal(type(zones['id']),int)

            assert_in('name',zones)
            assert_equal(type(zones['name']),str)

            assert_in('timeAdjustment',zones)
            assert_equal(type(zones['timeAdjustment']),str)

            assert_in('active',zones)
            assert_equal(type(zones['active']), bool)