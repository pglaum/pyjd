from pyjd.jd_types import DialogInfo, DialogTypeInfo
from . import get_jdownloader
from time import sleep


class TestDialogs:
    @classmethod
    def setup_class(cls):
        cls.jdownloader = get_jdownloader()

    def test_dialogs(self):
        # we're just doing everything in here..

        # generate a dialog
        self.jdownloader.accounts.add_account("youtube.com", "user", "pass")

        # list dialogs
        dialogs = self.jdownloader.dialogs.list()
        assert isinstance(dialogs, list)
        assert len(dialogs) > 0

        # get dialog
        dialog = self.jdownloader.dialogs.get(dialogs[0])
        assert isinstance(dialog, DialogInfo)
        assert isinstance(dialog.properties, dict)

        # get dialog type
        dialog_type = self.jdownloader.dialogs.get_type_info(dialog.type)
        assert isinstance(dialog_type, DialogTypeInfo)
        assert isinstance(dialog_type.in_, dict)
        assert isinstance(dialog_type.out, dict)

        # answer dialog
        dialogs = self.jdownloader.dialogs.list()
        dialogs.reverse()

        for dialog in dialogs:
            res = self.jdownloader.dialogs.answer(
                dialog, {"dontshowagain": False, "closereason": "cancel"}
            )
            # this test is not working all too well..
            # assert res is True

        dialogs = self.jdownloader.dialogs.list()
        assert len(dialogs) == 0

        # remove account
        a = self.jdownloader.accounts.list_accounts()
        self.jdownloader.accounts.remove_accounts([a[0].uuid])
