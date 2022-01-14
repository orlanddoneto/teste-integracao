import json
import unittest
from nose.tools import *
import requests

from utils.main_functions import *


class TestPermissions(unittest.TestCase):
    def setUp(self):
        self.header = {'Authorization': auth_token()}

    def test_get_permissions(self):
        response = requests.get(f"{URL}/permissions", headers=self.header)
        assert_equal(response.status_code, 200)

        json_data = json.loads(response.content)

        for permissions in json_data:
            assert_in('id', permissions)
            assert_equal(type(permissions['id']), int)

            assert_in('name', permissions)
            assert_equal(type(permissions['name']),str)

            assert_in('adviser', permissions)
            assert_equal(type(permissions['adviser']), bool)

            assert_in('achiever', permissions)
            assert_equal(type(permissions['achiever']), bool)

            assert_in('administrator', permissions)
            assert_equal(type(permissions['administrator']), bool)

            assert_in('coordinator', permissions)
            assert_equal(type(permissions['coordinator']), bool)

            assert_in('active', permissions)
            assert_equal(type(permissions['active']), bool)

            assert_in('tag', permissions)
            assert_equal(type(permissions['tag']), str)