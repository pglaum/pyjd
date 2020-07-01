from .jd import make_request
from .jd_types import IconDescriptor

endpoint = 'contentV2'


def action(route: str, params: any = None, binary: bool = False) -> any:
    route = f'{endpoint}{route}'
    return make_request(route, params, binary=binary)


def get_fav_icon(hostername: str) -> bytes:
    """Get the fav icon for a hoster.

    :param hostername: Name of the hoster for which the favicon will be returned
    :type hostername: str
    :returns: The favicon as png
    :rtype: bytes
    """

    params = [hostername]
    resp = action("/getFavIcon", params, True)
    return resp


def get_file_icon(filename: str) -> bytes:
    """Get the file icon.

    :param filename: The name of the icon
    :type filename: str
    :returns: The icon as png
    :rtype: bytes
    """

    params = [filename]
    resp = action("/getFileIcon", params, True)
    return resp


def get_icon(key: str, size: int) -> bytes:
    """Get an icon, scaled for size.

    :param filename: The name of the icon
    :type filename: str
    :param size: The size of the icon in px (it's a square)
    :type size: int
    :returns: The icon as png
    :rtype: bytes
    """

    params = [key, size]
    resp = action("/getIcon", params, True)
    return resp


def get_icon_description(key: str) -> str:
    """Get an icon description.

    :param key: The icon key
    :type key: str
    :returns: Description for the key
    :rtype: str
    """

    params = [key]
    resp = action("/getIconDescription", params)
    descriptor = IconDescriptor(resp)
    return descriptor
