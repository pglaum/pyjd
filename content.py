from pyjd import make_request
from pyjd.jd_types import IconDescriptor

endpoint = 'contentV2'


def action(route, params=None, binary=False):
    route = f'{endpoint}{route}'
    return make_request(route, params, binary=binary)


def get_fav_icon(hostername):
    """Get the fav icon for a hoster."""

    params = [hostername]
    resp = action("/getFavIcon", params, True)
    return resp


def get_file_icon(filename):
    """Get the file icon."""

    params = [filename]
    resp = action("/getFileIcon", params, True)
    return resp


def get_icon(key, size):
    """Get an icon."""

    params = [key, size]
    resp = action("/getIcon", params, True)
    return resp


def get_icon_description(key):
    """Get an icon description."""

    params = [key]
    resp = action("/getIconDescription", params)
    descriptor = IconDescriptor(resp)
    return descriptor
