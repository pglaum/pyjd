from typing import Optional
import pytest

from pyjd.jd_types import Account, AccountQuery, BasicAuth, BasicAuthType
from . import get_jdownloader


class TestAccounts:
    @classmethod
    def setup_class(cls):
        cls.jdownloader = get_jdownloader()

    def test_add_account(self):
        self.jdownloader.accounts.add_account("youtube.com", "user", "pass")
        self.jdownloader.accounts.add_account("archive.org", "user", "pass")

    def test_add_basic_auth(self):
        self.jdownloader.accounts.add_basic_auth(
            BasicAuthType.HTTP, "example.org", "user", "pass"
        )

    def test_disable_accounts(self):
        a = self.jdownloader.accounts.list_accounts()[0]
        self.jdownloader.accounts.disable_accounts([a.uuid])

        a = self.jdownloader.accounts.list_accounts(AccountQuery(uuidlist=[a.uuid]))
        assert not a[0].enabled

    def test_enable_accounts(self):
        a = self.jdownloader.accounts.list_accounts()[0]
        self.jdownloader.accounts.enable_accounts([a.uuid])

        a = self.jdownloader.accounts.list_accounts(AccountQuery(uuidlist=[a.uuid]))
        assert a[0].enabled == True

    def test_get_premium_hoster_url(self):
        expected = "http://update3.jdownloader.org/jdserv/BuyPremiumInterface/redirect?https%3A%2F%2Fwww.youtube.com%2F&captcha%2Fwebinterface%2F07072023_1321"
        url = self.jdownloader.accounts.get_premium_hoster_url("youtube.com")

        assert url[:-13] == expected[:-13]

    def test_list_accounts(self):
        accounts = self.jdownloader.accounts.list_accounts()
        assert len(accounts) == 2

    def test_list_basic_auths(self):
        basicAuths = self.jdownloader.accounts.list_basic_auth()
        assert len(basicAuths) == 1
        self.basicAuth = basicAuths[0]

    def test_list_premium_hoster_and_urls(self):
        # test both `list_premium_hoster()` and `list_premium_hoster_urls()`

        hosters = self.jdownloader.accounts.list_premium_hoster()
        urls = self.jdownloader.accounts.list_premium_hoster_urls()

        assert type(hosters) == list
        assert type(hosters[0]) == str
        assert type(urls) == dict

        assert len(hosters) == len(urls.keys())

    def test_refresh_accounts(self):
        accounts = self.jdownloader.accounts.list_accounts()
        ids = [a.uuid for a in accounts]
        self.jdownloader.accounts.refresh_accounts(ids)

    def test_set_username_and_password(self):
        a = self.jdownloader.accounts.list_accounts()[0]
        res = self.jdownloader.accounts.set_username_and_password(
            a.uuid, "test", "pass"
        )
        assert res == True

        a = self.jdownloader.accounts.list_accounts(AccountQuery(uuidlist=[a.uuid]))
        assert a[0].username == "test"

    def test_update_basic_auth(self):
        b = self.jdownloader.accounts.list_basic_auth()[0]
        b.username = "test"
        res = self.jdownloader.accounts.update_basic_auth(b)
        assert res == True

        b = self.jdownloader.accounts.list_basic_auth()[0]
        assert b.username == "test"

    def test_remove_accounts(self):
        for a in self.jdownloader.accounts.list_accounts():
            if a and a.uuid:
                self.jdownloader.accounts.remove_accounts([a.uuid])

    def test_remove_basic_auths(self):
        b = self.jdownloader.accounts.list_basic_auth()[0]
        self.jdownloader.accounts.remove_basic_auths([b.id])
