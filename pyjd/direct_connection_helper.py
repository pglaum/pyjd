from typing import Optional, Any
import json
import requests


class DirectConnectionHelper:
    def __init__(self, device):

        self.device = device

    def action(
        self,
        path: str,
        params: Optional[Any] = None,
        http_action: str = "POST",
        binary: bool = False,
    ) -> Any:
        """Make the request to the JDownloader.

        :param path: The URL endpoint (excluding base_url) that is called.
        :type path: str
        :param params: Parameters for the request
        :type params: list, dict or str
        :param http_action: The HTTP method (unused)
        :type http_action: str
        :param binary: Return the response as byte array
        :type binary: bool
        :returns: The result of the request
        :rtype: byte_array, dict, string
        """

        rurl = f"{self.device.connector.base_url}{path}"

        param_list = []
        if params:
            for param in params:
                param_list.append(json.dumps(param))
        rparams = "?" + "&".join(param_list)

        if binary:
            return requests.get(rurl + rparams).content

        rstr = requests.get(rurl + rparams).content.decode()
        robj = json.loads(rstr)

        if "data" in robj:
            return robj["data"]

        return robj
