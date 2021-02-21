from configuration.sources import JsonConfigurationSource
import unittest
from os import path


class TestJsonConfigurationSource(unittest.TestCase):

    def test_can_get_value(self):
        folder = path.abspath(path.dirname(__file__))
        test_file = path.join(folder, "data/example-config.json")
        source = JsonConfigurationSource(test_file)
        values = source.get_value()
        assert values is not None
