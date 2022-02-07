from .jd_device import JDDevice
from .direct_connection_helper import DirectConnectionHelper
import requests


class DirectConnector:
    def __init__(self, base_url: str = "http://localhost:3128"):

        self.base_url = base_url

    def is_connected(self) -> bool:
        """Check if the JDownloader is reachable.

        This makes a dummy request to the JDownloader and returns True if it
        was successful

        :returns: Connection status
        :rtype: bool
        """

        try:
            requests.get(self.base_url + "/jd/version")
            return True
        except Exception:
            pass

        return False

    def get_device(self):

        device_dict = {
            "id": "local",
            "name": "Local JDownloader",
            "type": "jd",
        }
        return JDDevice(self, DirectConnectionHelper, device_dict)
