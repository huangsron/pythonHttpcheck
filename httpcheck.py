# python 3

import unittest
import requests
import json
import os
from argparse import ArgumentParser

jsonFile = ""

class TestStringMethods(unittest.TestCase):
    def test_http_request(self):
        with open(jsonFile) as json_file:
            json_data = json.load(json_file)

        actual = []
        expected = []

        for d in json_data:
            http_request = d["request"]
            print(http_request)

            # 使用 GET 方式下載普通網頁 allow_redirects：URL導向
            r = requests.get(http_request['host'],
                             headers=http_request['headers'])

            actual.append(
                {'host': http_request['headers']['host'], 'status_code': r.status_code})
            expected.append(
                {'host': http_request['headers']['host'], 'status_code': d['expected']['status_code']})

        # print(actual)
        # print(expected)

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("file", help="json file")

    args = parser.parse_args()

    if args.file:
        jsonFile = args.file
    else:
        exit()

    # print(jsonFile)
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
