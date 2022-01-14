import json
import unittest
from nose.tools import *
import requests

from utils.main_functions import *


class TestProfile(unittest.TestCase):
    def setUp(self):
        self.header = {'Authorization': auth_token()}

    def test_get_profiles(self):
        response = requests.get(f"{URL}/profiles", headers=self.header)
        assert_equal(response.status_code, 200)

        json_data = json.loads(response.content)

        profile1 = json_data[0]

        assert_in("id", profile1)
        assert_equal(type(profile1["id"]), int)
        assert_equal(profile1['id'],1)

        assert_in("name", profile1)
        assert_equal(type(profile1["name"]), str)
        assert_equal(profile1['name'], "Administrator")

        assert_in("type", profile1)
        assert_equal(type(profile1["type"]), str)
        assert_equal(profile1['type'], "ADMINISTRATOR")

        profile2 = json_data[1]

        assert_in("id", profile2)
        assert_equal(type(profile2["id"]), int)
        assert_equal(profile2['id'], 2)

        assert_in("name", profile2)
        assert_equal(type(profile2["name"]), str)
        assert_equal(profile2['name'], "Achiever")

        assert_in("type", profile2)
        assert_equal(type(profile2["type"]), str)
        assert_equal(profile2['type'], "ACHIEVER")

        profile3 = json_data[2]

        assert_in("id", profile3)
        assert_equal(type(profile3["id"]), int)
        assert_equal(profile3['id'], 3)

        assert_in("name", profile3)
        assert_equal(type(profile3["name"]), str)
        assert_equal(profile3['name'], "Adviser")

        assert_in("type", profile3)
        assert_equal(type(profile3["type"]), str)
        assert_equal(profile3['type'], "ADVISER")

        profile4 = json_data[3]

        assert_in("id", profile4)
        assert_equal(type(profile4["id"]), int)
        assert_equal(profile4['id'], 4)

        assert_in("name", profile4)
        assert_equal(type(profile4["name"]), str)
        assert_equal(profile4['name'], "Coordinator")

        assert_in("type", profile4)
        assert_equal(type(profile4["type"]), str)
        assert_equal(profile4['type'], "COORDINATOR")