from .jd_device import JDDevice
from .myjd_connection_helper import MyJDConnectionHelper
from Crypto.Cipher import AES
from typing import Any, Dict, List
from urllib.parse import quote
import base64
import hashlib
import hmac
import json
import requests
import time

BS = 16


def PAD(s: bytes) -> bytes:
    """Pad a string

    :param s: String to pad
    :type s: str
    :return: Padded ``s``.
    :rtype: str
    """

    return s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()


def UNPAD(s: bytes) -> bytes:
    """Unpad a string.

    :param s: String to unpad
    :type s: str
    :return: Unpadded ``s``.
    :rtype: str
    """

    return s[0 : -s[-1]]


class MyJDConnector:
    """Main class for connecting to the MyJD API."""

    def __init__(self) -> None:
        """Initialize MyJD connector."""

        self.__request_id = int(time.time() * 1000)
        self.__api_url = "https://api.jdownloader.org"
        self.__app_key = "https://pglaum.srht.site/pyjd-api"
        self.__api_version = 1
        self.__devices = None

        self.__login_secret = None
        self.__device_secret = None
        self.__session_token = None
        self.__regain_token = None
        self.__server_encryption_token = None
        self.__device_encryption_token = None

        self.__connected = False

    def get_session_token(self) -> str:
        """Get the session token

        :return: Returns ``self.__session_token``.
        :rtype: str
        """

        return self.__session_token

    def is_connected(self) -> bool:
        """Indicate if a connection is established.

        :return: Returns ``self.__connected``.
        :rtype: bool
        """

        return self.__connected

    def set_app_key(self, app_key: str) -> None:
        """Set the app key.

        Use this function to set a custom app key for your own projects.

        :param app_key: The key to set.
        :type app_key: str
        """

        self.__app_key = app_key

    def __create_secret(self, email: str, password: str, domain: str) -> bytes:
        """Create the login_secret and device_secret.

        :param email: MyJDownloader user email
        :type email: str
        :param password: MyJDownloader user email
        :type password: str
        :param domain: The domain of the secret ("server" for login_secret and
            "device" for device_secret)
        :type domain: str
        :return: secret hash
        :rtype: str
        """

        secret_hash = hashlib.sha256()
        secret_hash.update(
            email.lower().encode("utf-8")
            + password.encode("utf-8")
            + domain.lower().encode("utf-8")
        )

        return secret_hash.digest()

    def __update_encryption_tokens(self) -> None:
        """Update the ``server_encryption_token`` and
        ``device_encryption_token``.
        """

        if self.__server_encryption_token is None:
            old_token = self.__login_secret
        else:
            old_token = self.__server_encryption_token
        new_token = hashlib.sha256()
        new_token.update(old_token + bytearray.fromhex(self.__session_token))
        self.__server_encryption_token = new_token.digest()
        new_token = hashlib.sha256()
        new_token.update(self.__device_secret + bytearray.fromhex(self.__session_token))
        self.__device_encryption_token = new_token.digest()

    def __create_signature(self, key: str, data: str) -> bytes:
        """Calculate the signature for the data, given a key.

        :param key: Key for the signature
        :type key: str
        :param data: Data to sign
        :type data: str
        :return: The SHA256 signature
        :rtype: bytes
        """

        signature = hmac.new(key, data.encode("utf-8"), hashlib.sha256)
        return signature.hexdigest()

    def __decrypt(self, secret_token: str, data: str) -> str:
        """Decrypt data from the server using the provided token.

        :param secret_token: Token for the server
        :type secret_token: str
        :param data: The data to decrypt
        :type data: str
        :returns: Decrypted data
        :rtype: str
        """

        init_vector = secret_token[: len(secret_token) // 2]
        key = secret_token[len(secret_token) // 2 :]
        decryptor = AES.new(key, AES.MODE_CBC, init_vector)

        decrypted_data = UNPAD(decryptor.decrypt(base64.b64decode(data)))

        return decrypted_data

    def __encrypt(self, secret_token: str, data: str) -> str:
        """Encrypt data for the server using the provided token.

        :param secret_token: Token for the server
        :type secret_token: str
        :param data: The data to decrypt
        :type data: str
        :returns: Decrypted data
        :rtype: str
        """

        data = PAD(data.encode("utf-8"))
        init_vector = secret_token[: len(secret_token) // 2]
        key = secret_token[len(secret_token) // 2 :]
        encryptor = AES.new(key, AES.MODE_CBC, init_vector)
        encrypted_data = base64.b64encode(encryptor.encrypt(data))

        return encrypted_data.decode("utf-8")

    def update_request_id(self) -> None:
        """Update ``__request_id``.

        This has to be done for every new request.
        """

        self.__request_id = int(time.time())

    def connect(self, email: str, password: str) -> bool:
        """Establish a connection to the MyJD Api.

        :param email: MyJDownloader user email
        :type email: str
        :param password: MyJDownloader user email
        :type password: str
        :returns: True if successful, False if there was any error.
        :rtype: bool
        """

        self.update_request_id()
        self.__login_secret = None
        self.__device_secret = None
        self.__session_token = None
        self.__regain_token = None
        self.__server_encryption_token = None
        self.__device_encryption_token = None
        self.__devices = None
        self.__connected = False

        self.__login_secret = self.__create_secret(email, password, "server")
        self.__device_secret = self.__create_secret(email, password, "device")
        response = self.request_api(
            "/my/connect", "GET", [("email", email), ("appkey", self.__app_key)]
        )
        self.__connected = True
        self.update_request_id()
        self.__session_token = response["sessiontoken"]
        self.__regain_token = response["regaintoken"]
        self.__update_encryption_tokens()
        self.update_devices()

        return response

    def reconnect(self) -> bool:
        """Re-establish connection to the API.

        :returns: True if successful, False if there was any error.
        :rtype: bool
        """

        response = self.request_api(
            "/my/reconnect",
            "GET",
            [
                ("sessiontoken", self.__session_token),
                ("regaintoken", self.__regain_token),
            ],
        )
        self.update_request_id()
        self.__session_token = response["sessiontoken"]
        self.__regain_token = response["regaintoken"]
        self.__update_encryption_tokens()

        return response

    def disconnect(self) -> bool:
        """Disconnect from the API.

        :returns: True if successful, False if there was any error.
        :rtype: bool
        """

        response = self.request_api(
            "/my/disconnect", "GET", [("sessiontoken", self.__session_token)]
        )
        self.update_request_id()
        self.__login_secret = None
        self.__device_secret = None
        self.__session_token = None
        self.__regain_token = None
        self.__server_encryption_token = None
        self.__device_encryption_token = None
        self.__devices = None
        self.__connected = False

        return response

    def update_devices(self) -> bool:
        """Update available devices.

        Use ``list_devices()`` to get the device list.

        :returns: True if successful, False if there was any error
        :rtype: bool
        """

        response = self.request_api(
            "/my/listdevices", "GET", [("sessiontoken", self.__session_token)]
        )
        self.update_request_id()
        self.__devices = response["list"]

        return response

    def list_devices(self) -> List[Dict]:
        """Get available devices.

        Use ``update_devices()`` to update the device list.
        Each device in the list is a dictionary, like in this example:

        .. code-block :: json

            [
                {
                    "name": "Device",
                    "id": "af9d03a21ddb917492dc1af8a6427f11",
                    "type": "jd"
                }
            ]

        :returns: List of devices
        :rtype: list[dict]
        """

        return self.__devices

    def get_device(self, device_name: str = None, device_id: str = None) -> JDDevice:
        """Get a JDDevice instance for a device

        Will search for ``device_id`` first and then for ``device_name``.

        :param device_name: Name of the device
        :type device_name: str
        :param device_id: ID of the device
        :type device_id: str
        :return: JDDevice instance of the device
        :rtype: JDDevice
        """

        if not self.is_connected():
            raise (Exception("No connection established\n"))

        if device_id is not None:
            for device in self.__devices:
                if device["id"] == device_id:
                    return JDDevice(self, MyJDConnectionHelper, device)

        elif device_name is not None:
            for device in self.__devices:
                if device["name"] == device_name:
                    return JDDevice(self, MyJDConnectionHelper, device)

        raise (Exception("Device not found\n"))

    def request_api(
        self,
        path: str,
        http_method: str = "GET",
        params: Any = None,
        action: str = None,
        api: str = None,
        binary: bool = False,
    ) -> Any:
        """Make a request to the MyJD API.

        The request goes to ``path``, using the ``http_method`` with the
        parameters ``params``.

        All requests should be executed with this method.

        :param path: The path to the endpoint (excluding the base_url)
        :type path: str
        :param http_method: HTTP method for the request.
            Can be:
            - GET
            - POST
        :type http_method: str
        :param params: Parameters for the request
        :type params: dict
        :param action: On which device to execute this.
            The string could look like this: ``/t_<session_token>_<device_id>``
        :type action: str
        :param api: The API URL. (Will be set to ``self.__api_url`` by
            default.)
        :type api: str
        :returns: The response
        :rtype: Any
        """

        if not api:
            api = self.__api_url

        data = None
        if not self.is_connected() and path != "/my/connect":
            raise (Exception("No connection established\n"))

        if http_method == "GET":
            query = [path + "?"]
            if params is not None:
                for param in params:
                    if param[0] != "encryptedLoginSecret":
                        query += ["%s=%s" % (param[0], quote(param[1]))]
                    else:
                        query += ["&%s=%s" % (param[0], param[1])]
            query += ["rid=" + str(self.__request_id)]

            if self.__server_encryption_token is None:
                query += [
                    "signature="
                    + str(
                        self.__create_signature(
                            self.__login_secret, query[0] + "&".join(query[1:])
                        )
                    )
                ]

            else:
                query += [
                    "signature="
                    + str(
                        self.__create_signature(
                            self.__server_encryption_token,
                            query[0] + "&".join(query[1:]),
                        )
                    )
                ]

            query = query[0] + "&".join(query[1:])
            encrypted_response = requests.get(api + query, timeout=3)
        else:
            params_request = []
            if params is not None:
                for param in params:
                    if not isinstance(param, list):
                        params_request += [json.dumps(param)]
                    else:
                        params_request += [param]

            params_request = {
                "apiVer": self.__api_version,
                "url": path,
                "params": params_request,
                "rid": self.__request_id,
            }

            data = json.dumps(params_request)
            # Removing quotes around null elements.
            data = data.replace('"null"', "null")
            data = data.replace("'null'", "null")
            encrypted_data = self.__encrypt(self.__device_encryption_token, data)

            if action is not None:
                request_url = api + action + path
            else:
                request_url = api + path

            try:
                encrypted_response = requests.post(
                    request_url,
                    headers={"Content-Type": "application/aesjson-jd; charset=utf-8"},
                    data=encrypted_data,
                    timeout=3,
                )

            except requests.exceptions.RequestException:
                return None

        if encrypted_response.status_code != 200:
            try:
                error_msg = json.loads(encrypted_response.text)
            except json.JSONDecodeError:
                try:
                    error_msg = json.loads(
                        self.__decrypt(
                            self.__device_encryption_token, encrypted_response.text
                        )
                    )
                except json.JSONDecodeError:
                    raise Exception(
                        "Failed to decode response: {}", encrypted_response.text
                    )

            msg = (
                "\n\tSOURCE: "
                + error_msg["src"]
                + "\n\tTYPE: "
                + error_msg["type"]
                + "\n------\nREQUEST_URL: "
                + api
                + path
            )

            if http_method == "GET":
                msg += query

            msg += "\n"
            if data is not None:
                msg += "DATA:\n" + data

            raise (Exception(msg))

        if binary:

            self.update_request_id()

            # Binary content is not encrypted
            return encrypted_response.content

        if action is None:
            if not self.__server_encryption_token:
                response = self.__decrypt(self.__login_secret, encrypted_response.text)
            else:
                response = self.__decrypt(
                    self.__server_encryption_token, encrypted_response.text
                )

        else:
            response = self.__decrypt(
                self.__device_encryption_token, encrypted_response.text
            )

        jsondata = json.loads(response.decode("utf-8"))
        if jsondata["rid"] != self.__request_id:
            self.update_request_id()
            return None

        self.update_request_id()
        return jsondata
