from pyjd.myjd_connection_helper import MyJDConnectionHelper
from .accounts import Accounts
from .captcha import Captcha
from .config import Config
from .content import Content
from .dialogs import Dialogs
from .device import Device
from .downloads import Downloads
from .events import Events
from .extensions import Extensions
from .linkgrabber import LinkGrabber
from .log import Log
from .plugins import Plugins
from .polling import Polling
from .system import System
from .toolbar import Toolbar
from .ui import UI
from .update import Update
from typing import Any


class JDDevice:
    """A class that represents a JDownloader device and its functions."""

    def __init__(
        self,
        connector: Any,
        connection_helper: Any,
        device_dict: dict,
        refresh_direct_connections: bool = True,
    ):
        """Initializes the device instance.

        :param connector: The connector object (direct or MyJD)
        :type connector: Any
        :param device_dict: Dictionary with device properties
        :type device_dict: dict
        :returns: A JDDevice object
        :rtype: JDDevice
        """

        self.name = device_dict["name"]
        self.device_id = device_dict["id"]
        self.device_type = device_dict["type"]

        self.connector = connector
        if connection_helper == MyJDConnectionHelper:
            self.connection_helper = connection_helper(
                self, refresh_direct_connections=refresh_direct_connections
            )
        else:
            self.connection_helper = connection_helper(self)

        self.accounts = Accounts(self)
        self.captcha = Captcha(self)
        self.config = Config(self)
        self.content = Content(self)
        self.dialogs = Dialogs(self)
        self.device = Device(self)
        self.downloads = Downloads(self)
        self.events = Events(self)
        self.extensions = Extensions(self)
        self.linkgrabber = LinkGrabber(self)
        self.log = Log(self)
        self.plugins = Plugins(self)
        self.polling = Polling(self)
        self.system = System(self)
        self.toolbar = Toolbar(self)
        self.ui = UI(self)
        self.update = Update(self)
