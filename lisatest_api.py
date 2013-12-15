import random
import unittest
from base import RequestApi
import json


class Test_functionApi(unittest.TestCase):
    def setUp(self):
        pass

    def test_notnull(self):
        data = RequestApi.get_json('/book/subject/1220562', {'alt': 'json'}, host="api.douban.com")
        self.assertIsNotNone(data)
        self.assertIsNone(data)


if __name__ == '__main__':
     unittest.main()