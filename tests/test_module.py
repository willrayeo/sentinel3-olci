import unittest

import stactools.sentinel3_olci


class TestModule(unittest.TestCase):
    def test_version(self):
        self.assertIsNotNone(stactools.sentinel3_olci.__version__)
