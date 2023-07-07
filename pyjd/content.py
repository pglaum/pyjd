from .jd_types import IconDescriptor
from typing import Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .jd_device import JDDevice


class Content:
    def __init__(self, device: "JDDevice") -> None:
        self.device = device
        self.endpoint = "contentV2"

    def action(self, route: str, params: Optional[Any] = None, binary: bool = False) -> Any:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params, binary=binary)

    def get_fav_icon(self, hostername: str) -> bytes:
        """Get the fav icon for a hoster.

        :param hostername: Name of the hoster for which the favicon will be
            returned
        :type hostername: str
        :returns: The favicon as png
        :rtype: bytes
        """

        params = [hostername]
        resp = self.action("/getFavIcon", params, True)
        return resp

    def get_file_icon(self, filename: str) -> bytes:
        """Get the file icon.

        :param filename: The name of the icon
        :type filename: str
        :returns: The icon as png
        :rtype: bytes
        """

        params = [filename]
        resp = self.action("/getFileIcon", params, True)
        return resp

    def get_icon(self, key: str, size: int) -> bytes:
        """Get an icon, scaled for size.

        :param filename: The name of the icon
        :type filename: str
        :param size: The size of the icon in px (it's a square)
        :type size: int
        :returns: The icon as png
        :rtype: bytes
        """

        params = [key, size]
        resp = self.action("/getIcon", params, True)
        return resp

    def get_icon_description(self, key: str) -> IconDescriptor:
        """Get an icon description.

        :param key: The icon key
        :type key: str
        :returns: Description for the key
        :rtype: str
        """

        params = [key]
        resp = self.action("/getIconDescription", params)
        print(resp)
        descriptor = IconDescriptor(**resp)
        return descriptor
