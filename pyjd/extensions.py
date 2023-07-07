from .jd_types import Extension, ExtensionQuery
from typing import Optional, Any, List


class Extensions:
    def __init__(self, device):
        self.device = device
        self.endpoint = "extensions"

    def action(self, route: str, params: Optional[Any] = None) -> Any:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params)

    def install(self, extension_id: str) -> bool:
        """Install the extension with extension_id.

        :param extension_id: The ID of the extension
        :type extension_id: str
        :return: Success
        :rtype: boolean
        """

        params = [extension_id]
        resp = self.action("/install", params)
        return resp

    def is_enabled(self, extension_id: str) -> bool:
        """Check if the extension of extension_id is enabled.

        :param extension_id: ID of the extension
        :type extension_id: str
        :return: Is enabled
        :rtype: boolean
        """

        params = [extension_id]
        resp = self.action("/isEnabled", params)
        return resp

    def is_installed(self, extension_id: str) -> bool:
        """Check if the extension of extension_id is installed.

        :param extension_id: ID of the extension
        :type extension_id: str
        :return: Is installed
        :rtype: boolean
        """

        params = [extension_id]
        resp = self.action("/isInstalled", params)
        return resp

    def list_extensions(
        self, query: ExtensionQuery = ExtensionQuery.default()
    ) -> List[Extension]:
        """List all extensions.

        :param query: A query to filter by (default: all)
        :type query: jd_types.ExtensionQuery
        :result: A list of extensions
        :rtype: List[jd_types.Extension]
        """

        params = [query.dict()]
        resp = list(self.action("/list", params))

        extensions = []
        for ext in resp:
            extension = Extension(**ext)
            extensions.append(extension)

        return extensions

    def set_enabled(self, extension_id: str, enabled: bool) -> bool:
        """Enable/Disable an extensions.

        :param extension_id: ID of the extension
        :type extension_id: str
        :param enabled: Enable or disable
        :type enabled: boolean
        :return: Success
        :rtype: boolean
        """

        params = [extension_id, enabled]
        resp = self.action("/setEnabled", params)
        return resp
