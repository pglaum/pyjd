from .jd import make_request
from .jd_types import Account, AccountQuery, BasicAuth, BasicAuthType

endpoint = 'accountsV2'


def action(route, params=None):
    route = f'{endpoint}{route}'
    return make_request(route, params)


def add_account(premium_hoster, username, password):
    """Add a premium hoster account.

    :param premium_hoster: The name of the premium hoster.
        See ``list_premium_hoster`` for possible names.
    :type premium_hoster: str
    :param username: User name or email address for that account.
    :type username: str
    :param password: Password for that account.
    :type password: str
    :return: empty
    :rtype: str
    """

    params = [premium_hoster, username, password]
    resp = action('/addAccount', params)
    return resp


def add_basic_auth(auth_type, hostmask, username, password):
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
    resp = action('/addBasicAuth', params)
    return resp


def disable_accounts(account_ids):
    """Disable premium hoster accounts.

    :param account_ids: A list of account uuids.
    :type account_ids: List[int]
    :return: empty
    :rtype: str
    """

    params = [account_ids]
    resp = action('/disableAccounts', params)
    return resp


def enable_accounts(account_ids):
    """Enable premium hoster accounts.

    :param account_ids: A list of account uuids.
    :type account_ids: List[int]
    :return: empty
    :rtype: str
    """

    params = [account_ids]
    resp = action('/enableAccounts', params)
    return resp


def get_premium_hoster_url(hoster):
    """Get the url for a premium hoster.

    Note: The url will be a redirect over the jdownloader.org servers.

    :param hoster: The name of a hoster.
    :type hoster: str
    :return: The url for ``hoster``.
    :rtype: str
    """

    params = [hoster]
    resp = action('/getPremiumHosterUrl', params)
    return resp


def list_accounts(account_query=AccountQuery()):
    """List premium hoster accounts.

    :param params: An AccountQuery object.
    :type: AccountQuery
    :return: A list of accounts
    :rtype: List[Account]
    """

    params = [account_query.to_dict()]
    resp = action('/listAccounts', params)

    accounts = []
    for acc in resp:
        account = Account(acc)
        accounts.append(account)

    return accounts


def list_basic_auth():
    """List basic auth accounts.

    :return: A list of basic auth accounts.
    :rtype: list[BasicAuthentication]
    """

    resp = action('/listBasicAuth')

    basic_auths = []
    for auth in resp:
        basic_auth = BasicAuth(auth)
        basic_auths.append(basic_auth)

    return basic_auths


def list_premium_hoster():
    """List known premium hosters.

    :return: A list of all known premium hosters.
    :rtype: List[str]
    """

    resp = action('/listPremiumHoster')
    return resp


def list_premium_hoster_urls():
    """List known premium hosters with urls.

    :return: A map of all known premium hosters to urls.
    :rtype: Map[str, str]
    """

    resp = action('/listPremiumHosterUrls')
    return resp


def refresh_accounts(account_ids):
    """Let JDownloader refresh the account status for ``account_ids``.

    :param account_ids: A list of account ids
    :type account_ids: List[int]
    :return: empty
    :rtype: str
    """

    params = [account_ids]
    resp = action('/refreshAccounts', params)
    return resp


def remove_accounts(account_ids):
    """Remove the accounts for ``account_ids``.

    :param account_ids: A list of account ids
    :type account_ids: List[int]
    :return: empty
    :rtype: str
    """

    params = [account_ids]
    resp = action('/removeAccounts', params)
    return resp


def remove_basic_auths(basic_auth_ids):
    """Remove basic auths for ``basic_auth_ids``.

    :param basic_auth_ids: A list of basic auth ids.
    :type account_ids: List[int]
    :return: Success.
    :rtype: bool
    """

    params = [basic_auth_ids]
    resp = action('/removeBasicAuths', params)
    return resp


def set_username_and_password(account_id, username, password):
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
    resp = action('/setUserNameAndPassword', params)
    return resp


def update_basic_auth(basic_authentication):
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

    params = [basic_authentication.to_dict()]
    resp = action('/updateBasicAuth', params)
    return resp
