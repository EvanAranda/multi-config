import unittest

from configuration import Configuration, Section


class TestConfiguration(unittest.TestCase):
    def test_property_access(self):
        config = Configuration(
            key1="value1",
            key2=dict(
                key2_2="value2_2"
            )
        )

        assert config.key1 == "value1"
        assert isinstance(config.key2, Section)
        assert config.key2.key2_2 == "value2_2"

    def test_property_path_subscript_access(self):
        config = Configuration(
            key1="value1",
            key2=dict(
                key2_2="value2_2"
            )
        )

        assert config["key1"] == "value1"
        assert isinstance(config["key2"], Section)
        assert config["key2:key2_2"] == "value2_2"
        assert config["key2"]["key2_2"] == "value2_2"
