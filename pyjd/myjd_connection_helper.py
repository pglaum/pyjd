import time
from typing import List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .jd_device import JDDevice


class MyJDConnectionHelper:
    def __init__(
        self, device: "JDDevice", refresh_direct_connections: bool = True
    ) -> None:

        self.device = device

        self.__direct_connection_info: Optional[list] = None
        if refresh_direct_connections:
            print("refreshing direct connections")
            self.__refresh_direct_connections()
        self.__direct_connection_enabled = True
        self.__direct_connection_cooldown = 0
        self.__direct_connection_consecutive_failures = 0

    def __refresh_direct_connections(self) -> None:
        """Check again if a direct connection is possible."""

        response = self.device.connector.request_api(
            "/device/getDirectConnectionInfos", "POST", None, self.__action_url()
        )

        if (
            response is not None
            and "data" in response
            and "infos" in response["data"]
            and len(response["data"]["infos"]) != 0
        ):

            self.__update_direct_connections(response["data"]["infos"])

    def __update_direct_connections(self, direct_info: list) -> None:
        """Update the direct_connection info while keeping the correct order.

        :param direct_info: Information about direct connections
        :type direct_info: dict
        """

        tmp = []
        if self.__direct_connection_info is None:
            for conn in direct_info:
                tmp.append({"conn": conn, "cooldown": 0})

            self.__direct_connection_info = tmp
            return

        # Remove old connections that are not available any longer.
        for i in self.__direct_connection_info:
            if i["conn"] not in direct_info:
                tmp.remove(i)
            else:
                direct_info.remove(i["conn"])

        # Add new connections
        for conn in direct_info:
            tmp.append({"conn": conn, "cooldown": 0})

        self.__direct_connection_info = tmp

    def enable_direct_connection(self) -> None:
        """Enable direct connections."""

        self.__direct_connection_enabled = True
        self.__refresh_direct_connections()

    def disable_direct_connect(self) -> None:
        """Disable direct connections."""

        self.__direct_connection_enabled = False
        self.__direct_connection_info = None

    def get_direct_connection_info(self) -> Optional[list]:
        """
        Get information about the direct connections.

        :return: Information about the direct connections
        :rtype: list
        """

        return self.__direct_connection_info

    def set_direct_connection_info(self, direct_info: list) -> None:
        """
        Set information about the direct connections.

        :param direct_info: Information about the direct connections
        :type direct_info: list
        """

        self.__direct_connection_info = direct_info

    def action(
        self,
        path: str,
        params: List = [],
        http_action: str = "POST",
        binary: bool = False,
    ) -> Optional[dict]:
        """Execute any action for the device using the params.

        All the information about the parameters and their default values,
        types, etc. can be found in the API specification for MyJDownloader
        (https://my.jdownloader.org/developers/).

        :param path: The URL of the endpoint (excluding the base url)
        :type path: str
        :param params: URL parameters, in a list of tuples.
            Example: ``[("param1","ex"),("param2","ex2")]`` becomes
            ``/example?param1=ex&param2=ex2``
        :type params: List
        :param http_action: The HTTP request type ('GET' or 'POST')
        :type http_action: str
        :param binary: Return binary response, if needed
        :type binary: bool
        :return: Response from the MyJD API
        :rtype: dict
        """

        action_url = self.__action_url()

        if (
            not self.__direct_connection_enabled
            or self.__direct_connection_info is None
            or time.time() < self.__direct_connection_cooldown
        ):

            # No direct connection available, use the MyJD API
            response = self.device.connector.request_api(
                path, http_action, params, action_url, binary=binary
            )

            if response is None:
                return None
            elif binary:
                return response
            else:
                if (
                    self.__direct_connection_enabled
                    and time.time() >= self.__direct_connection_cooldown
                ):
                    self.__refresh_direct_connections()

                if "data" in response:
                    return response["data"]
                return response

        else:

            # A direct connection is available, try to use it
            for conn in self.__direct_connection_info:

                if time.time() > conn["cooldown"]:

                    # Use the direct connection
                    connection = conn["conn"]
                    api = f'http://{connection["ip"]}:{connection["port"]}'

                    response = self.device.connector.request_api(
                        path, http_action, params, action_url, api, binary=binary
                    )

                    if response is None:
                        # Don't try this connection for a minute.
                        conn["cooldown"] = time.time() + 60

                    elif binary:
                        return response

                    else:
                        # This connection worked, push it to the top of the
                        # list.
                        self.__direct_connection_info.remove(conn)
                        self.__direct_connection_info.insert(0, conn)
                        self.__direct_connection_consecutive_failures = 0

                        if "data" in response:
                            return response["data"]
                        return response

            # None of the direct connections worked, set a cooldown for all
            # direct connections
            self.__direct_connection_consecutive_failures += 1
            self.__direct_connection_cooldown = int(
                time.time() + (60 * self.__direct_connection_consecutive_failures)
            )

            # Use the MyJD API instead
            response = self.device.connector.request_api(
                path, http_action, params, action_url, binary=binary
            )

            if response is None:
                return None

            self.__refresh_direct_connections()

            if "data" in response:
                return response["data"]
            return response

    def __action_url(self) -> str:
        """Generate the action url for the device and session."""

        return (
            "/t_"
            + self.device.connector.get_session_token()
            + "_"
            + self.device.device_id
        )
