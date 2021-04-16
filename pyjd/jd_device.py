from .downloads import Downloads
from .myjd_connection_helper import MyJDConnectionHelper
from typing import Any
import time


class JDDevice:
    """A class that represents a JDownloader device and its functions."""

    def __init__(self, connector: Any, device_dict: dict):
        """Initializes the device instance.

        :param connector: The connector object (direct or MyJD)
        :type connector: Any
        :param device_dict: Dictionary with device properties
        :type device_dict: dict
        :returns: A JDDevice object
        :rtype: JDDevice
        """

        self.name = device_dict['name']
        self.device_id = device_dict['id']
        self.device_type = device_dict['type']

        self.connector = connector
        self.connection_helper = MyJDConnectionHelper(self)

        self.downloads = Downloads(self)
