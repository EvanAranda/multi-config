import unittest

from configuration.sources import MemoryConfigurationSource


class TestMemoryConfigurationSource(unittest.TestCase):
    def test_get_value(self):
        source = MemoryConfigurationSource()
        source.add("key1", "value1")
        source.add("key2", dict(key2_2="value2_2"))

        value = source.get_value()

        assert value["key1"] == "value1"
        assert value["key2"]["key2_2"] == "value2_2"
