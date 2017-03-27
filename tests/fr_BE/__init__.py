# coding=utf-8

from __future__ import unicode_literals

import unittest
import re

from faker import Factory


class fr_BE__FactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = Factory.create('fr_BE')

    def test_fr_BE_postcode(self):
        for i in range(100):
            self.assertTrue(re.match(r'^[0-9]{4}$', self.factory.postcode()))
        
