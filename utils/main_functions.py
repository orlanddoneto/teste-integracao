import json
import unittest
from nose.tools import *
import requests


URL = "https://testapi.jasgme.com/sgme/api"

def auth_token():
    data = {
        "login": "test.sgme@gmail.com",
        "password": "abcd1234"
    }

    response = requests.post(f"{URL}/authenticate/login", json=data)
    assert_equal(response.status_code, 200)

    json_data = json.loads(response.content)
    return f"Bearer {json_data['token']}"