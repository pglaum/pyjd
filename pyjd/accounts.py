from .jd_types import Account, AccountQuery, BasicAuth, BasicAuthType
from typing import Optional, Any, Dict, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .jd_device import JDDevice


class Accounts:
    def __init__(self, device: "JDDevice"):

        self.device = device
        self.endpoint = "accountsV2"

    def action(self, route: str, params: Optional[Any] = None) -> Any:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params)

    def add_account(self, premium_hoster: str, username: str, password: str) -> None:
        """Add a premium hoster account.

        .. warning:: The password is used in plain text, so beware...

        :param premium_hoster: The name of the premium hoster.
            See ``list_premium_hoster`` for possible names.
        :type premium_hoster: str
        :param username: User name or email address for that account.
        :type username: str
        :param password: Password for that account.
        :type password: str
        :return: empty
        :rtype: None
        """

        params = [premium_hoster, username, password]
        self.action("/addAccount", params)

    def add_basic_auth(
        self, auth_type: BasicAuthType, hostmask: str, username: str, password: str
    ) -> int:
        """Add a basic auth account.

        These accounts are plain HTTP or FTP connections, with passwords.

        :param auth_type: The auth type has to be on of the following:

            - "HTTP"
            - "FTP"
        :type auth_type: BasicAuthType
        :param hostmask: Mask of the account host.
        :type hostmask: str
        :param username: User name for the account.
        :type username: str
        :param password: Password for the account.
        :type password: str
        :return: The ID of the newly created basic auth account.
        :rtype: int
        """

        params = [auth_type.value, hostmask, username, password]
        resp = self.action("/addBasicAuth", params)
        return resp

    def disable_accounts(self, account_ids: List[int]) -> None:
        """Disable premium hoster accounts.

        :param account_ids: A list of account uuids.
        :type account_ids: List[int]
        :return: empty
        :rtype: None
        """

        params = [account_ids]
        self.action("/disableAccounts", params)

    def enable_accounts(self, account_ids: List[int]) -> None:
        """Enable premium hoster accounts.

        :param account_ids: A list of account uuids.
        :type account_ids: List[int]
        """

        params = [account_ids]
        self.action("/enableAccounts", params)

    def get_premium_hoster_url(self, hoster: str) -> str:
        """Get the url for a premium hoster.

        Note: The url will be a redirect over the jdownloader.org servers.

        :param hoster: The name of a hoster.
        :type hoster: str
        :return: The url for ``hoster``.
        :rtype: str
        """

        params = [hoster]
        resp = self.action("/getPremiumHosterUrl", params)
        return resp

    def list_accounts(
        self, account_query: AccountQuery = AccountQuery.default()
    ) -> List[Account]:
        """List premium hoster accounts.

        :param params: An AccountQuery object.
        :type: AccountQuery
        :return: A list of accounts
        :rtype: List[Account]
        """

        params = [account_query.dict()]
        resp = self.action("/listAccounts", params)

        accounts = []
        for acc in resp:
            account = Account(**acc)
            accounts.append(account)

        return accounts

    def list_basic_auth(self) -> List[BasicAuth]:
        """List basic auth accounts.

        :return: A list of basic auth accounts.
        :rtype: list[BasicAuthentication]
        """

        resp = self.action("/listBasicAuth")

        basic_auths = []
        for auth in resp:
            basic_auth = BasicAuth(**auth)
            basic_auths.append(basic_auth)

        return basic_auths

    def list_premium_hoster(self) -> List[str]:
        """List known premium hosters.

        :return: A list of all known premium hosters.
        :rtype: List[str]
        """

        resp = self.action("/listPremiumHoster")
        return resp

    def list_premium_hoster_urls(self) -> Dict[str, str]:
        """List known premium hosters with urls.

        :return: A map of all known premium hosters to urls.
        :rtype: Dict[str, str]
        """

        resp = self.action("/listPremiumHosterUrls")
        return resp

    def refresh_accounts(self, account_ids: List[int]) -> None:
        """Let JDownloader refresh the account status for ``account_ids``.

        :param account_ids: A list of account ids
        :type account_ids: List[int]
        :return: empty
        :rtype: None
        """

        params = [account_ids]
        self.action("/refreshAccounts", params)

    def remove_accounts(self, account_ids: List[int]) -> None:
        """Remove the accounts for ``account_ids``.

        :param account_ids: A list of account ids
        :type account_ids: List[int]
        :return: empty
        :rtype: None
        """

        params = [account_ids]
        self.action("/removeAccounts", params)

    def remove_basic_auths(self, basic_auth_ids: List[int]) -> bool:
        """Remove basic auths for ``basic_auth_ids``.

        :param basic_auth_ids: A list of basic auth ids.
        :type account_ids: List[int]
        :return: Success.
        :rtype: bool
        """

        params = [basic_auth_ids]
        resp = self.action("/removeBasicAuths", params)
        return resp

    def set_username_and_password(
        self, account_id: int, username: str, password: str
    ) -> bool:
        """Set a new username and password for a premium hoster account.

        :param account_id: The ID of the account.
        :type account_id: int
        :param username: The new username.
        :type username: str
        :param password: The new password.
        :type password: str
        :return: Success
        :rtype: bool
        """

        params = [account_id, username, password]
        resp = self.action("/setUserNameAndPassword", params)
        return resp

    def update_basic_auth(self, basic_authentication: BasicAuth) -> bool:
        """Update the credentials for a basic auth.

        .. note ::

            It is recommended to use the result of a ``list_basic_auth`` query
            for the input parameters. This way all necessary fields are filled
            and you can just update select parameters.

        :param basic_authentication: The new account parameters.
        :type basic_authentication: dict, BasicAuthentication
        :return: Success
        :rtype: bool
        """

        params = [basic_authentication.dict()]
        resp = self.action("/updateBasicAuth", params)
        return resp
