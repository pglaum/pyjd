from .jd import make_request
from .jd_types import Extension, ExtensionQuery
from typing import Any, List

endpoint = 'extensions'


def action(route: str, params: Any = None) -> Any:
    route = f'{endpoint}{route}'
    return make_request(route, params)


def install(extension_id: str) -> bool:
    """Install the extension with extension_id.

    :param extension_id: The ID of the extension
    :type extension_id: str
    :return: Success
    :rtype: boolean
    """

    params = [extension_id]
    resp = action("/install", params)
    return resp


def is_enabled(extension_id: str) -> bool:
    """Check if the extension of extension_id is enabled.

    :param extension_id: ID of the extension
    :type extension_id: str
    :return: Is enabled
    :rtype: boolean
    """

    params = [extension_id]
    resp = action("/isEnabled", params)
    return resp


def is_installed(extension_id: str) -> bool:
    """Check if the extension of extension_id is installed.

    :param extension_id: ID of the extension
    :type extension_id: str
    :return: Is installed
    :rtype: boolean
    """

    params = [extension_id]
    resp = action("/isInstalled", params)
    return resp


def list(query: ExtensionQuery = ExtensionQuery()) -> List[Extension]:
    """List all extensions.

    :param query: A query to filter by (default: all)
    :type query: jd_types.ExtensionQuery
    :result: A list of extensions
    :rtype: List[jd_types.Extension]
    """

    params = [query.to_dict()]
    resp = list(action("/list", params))

    extensions = []
    for ext in resp:
        extension = Extension(ext)
        extensions.append(extension)

    return extensions


def set_enabled(extension_id: str, enabled: bool) -> bool:
    """Enable/Disable an extensions.

    :param extension_id: ID of the extension
    :type extension_id: str
    :param enabled: Enable or disable
    :type enabled: boolean
    :return: Success
    :rtype: boolean
    """

    params = [extension_id, enabled]
    resp = action("/setEnabled", params)
    return resp
