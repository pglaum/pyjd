import pytest

from . import get_jdownloader


class TestCaptcha:
    @classmethod
    def setup_class(cls):
        cls.jdownloader = get_jdownloader()

    def test_get(self):
        # no captchas available for testing
        assert True

    def test_get_captcha_job(self):
        # no captcha jobs available for testing
        assert True

    def test_list(self):
        self.jdownloader.captcha.list()

    def test_skip(self):
        # no captchas available for testing
        assert True

    def test_solve(self):
        # no captchas available for testing
        assert True
