#!/usr/bin/env python
# coding: utf-8

import unittest

from teamcity.unittestpy import TeamcityTestRunner


class Test(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(1, 1, 'expect 1 equals 1')


if __name__ == '__main__':
    unittest.main(testRunner=TeamcityTestRunner)
