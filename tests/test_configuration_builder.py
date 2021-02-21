import unittest

from configuration import ConfigurationBuilder
from configuration.sources import JsonConfigurationSource, MemoryConfigurationSource


class TestConfigurationBuilder(unittest.TestCase):

    def test_build(self):
        config = ConfigurationBuilder() \
            .add(MemoryConfigurationSource(dict(keyA=1))) \
            .build()

        assert config.keyA == 1
        assert config["key2.key2_1"] == "value2.1"
