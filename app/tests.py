__author__ = 'ruslanpa'

from unittest import TestCase


class StubTestCase(TestCase):

    def test_stub_method(self):
        self.assertEqual(2, 1 + 1, "It is a simple stub")