import pytest

from pyjd.jd_types import AdvancedConfigQuery
from . import get_jdownloader


class TestConfig:
    @classmethod
    def setup_class(cls):
        cls.jdownloader = get_jdownloader()

    def test_get(self):
        cfg = self.jdownloader.config.get(
            "org.jdownloader.plugins.components.youtube.YoutubeConfig",
            "cfg/plugins/youtube/Youtube",
            "MaxVideoResolution",
        )
        assert cfg == "P_4320"  # this is jdownloader's default value

    def test_get_default(self):
        cfg = self.jdownloader.config.get(
            "org.jdownloader.plugins.components.youtube.YoutubeConfig",
            "cfg/plugins/youtube/Youtube",
            "MaxVideoResolution",
        )
        assert cfg == "P_4320"  # this is jdownloader's default value

    def test_list(self):
        youtube_config = self.jdownloader.config.list(".*youtube.*")
        all_config = self.jdownloader.config.list()
        assert len(youtube_config) > 0
        assert len(youtube_config) < len(all_config)

    def test_list_enum(self):
        options = self.jdownloader.config.list_enum(
            "org.jdownloader.plugins.components.youtube.itag.VideoResolution"
        )
        assert type(options) == list
        assert len(options) > 0

    def test_query(self):
        query = AdvancedConfigQuery.default()
        query.pattern = ".*youtube.*"
        res = self.jdownloader.config.query(query)
        assert type(res) == list
        assert len(res) > 0

    def test_set(self):
        res = self.jdownloader.config.set(
            "org.jdownloader.plugins.components.youtube.YoutubeConfig",
            "cfg/plugins/youtube/Youtube",
            "MaxVideoResolution",
            "P_1080",
        )
        assert res

        value = self.jdownloader.config.get(
            "org.jdownloader.plugins.components.youtube.YoutubeConfig",
            "cfg/plugins/youtube/Youtube",
            "MaxVideoResolution",
        )
        assert value == "P_1080"

    def test_reset(self):
        res = self.jdownloader.config.reset(
            "org.jdownloader.plugins.components.youtube.YoutubeConfig",
            "cfg/plugins/youtube/Youtube",
            "MaxVideoResolution",
        )
        assert res

        value = self.jdownloader.config.get(
            "org.jdownloader.plugins.components.youtube.YoutubeConfig",
            "cfg/plugins/youtube/Youtube",
            "MaxVideoResolution",
        )
        assert value == "P_4320"
