import pytest

from pyjd.jd_types import DirectConnectionInfos
from . import get_jdownloader


class TestContent:
    @classmethod
    def setup_class(cls):
        cls.jdownloader = get_jdownloader()

    def test_get_direct_connection_infos(self):
        res = self.jdownloader.device.get_direct_connection_infos()
        assert isinstance(res, DirectConnectionInfos)

    def test_get_session_public_key(self):
        self.jdownloader.device.get_session_public_key()

    def test_ping(self):
        assert self.jdownloader.device.ping() == True
