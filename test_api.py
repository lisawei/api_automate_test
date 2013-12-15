import random
import unittest
from base import RequestApi
import json

class TestApiFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_not_null(self):
        data = RequestApi.get_json('/book/subject/1220562', {'alt': 'json'}, host="api.douban.com")
        self.assertIsNotNone(data)

    def test_title_required(self):
        data = RequestApi.get_json('/book/subject/1220562', {'alt': 'json'}, host="api.douban.com")
        self.assertIsNotNone(data)
        self.assertIsNotNone(data["title"])

    def test_sample(self):
        data = RequestApi.get_json('/book/subject/1220562', {'alt': 'json'})
        self.assertIsNone(data)


if __name__ == '__main__':
    unittest.main()
