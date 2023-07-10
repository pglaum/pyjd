import pytest
from . import get_jdownloader


class TestContent:
    @classmethod
    def setup_class(cls):
        cls.jdownloader = get_jdownloader()

    @pytest.mark.parametrize(
        "url",
        [
            "youtube.com",
            "example.org",
        ],
    )
    def test_get_fav_icon(self, url):
        assert type(self.jdownloader.content.get_fav_icon(url)) == bytes

    def test_get_file_icon(self):
        assert type(self.jdownloader.content.get_file_icon(".rar")) == bytes

    def test_get_icon(self):
        assert type(self.jdownloader.content.get_icon("clear", 18)) == bytes
