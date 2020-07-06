from typing import Any
import json
import requests
import traceback

base_url = 'http://localhost:3128/'
debugging = 0


def make_request(endpoint: str, params: Any, binary: bool = False) -> Any:
    """Makes a request to the JDownloader.

    :param endpoint: The url endpoint (exluding base_url) that is called.
    :type endpoint: str
    :param params: Parameters that are to be added
    :type params: list, dict or str
    :param binary: If the request expects a binary answer
    :type binary: bool
    :returns: The result of the request
    :rtype: binary, dict, or string
    """

    rurl = f'{base_url}{endpoint}'

    rparams = []
    if params:
        for param in params:
            rparams.append(json.dumps(param))
    rparams = '?' + '&'.join(rparams)

    if debugging > 1:
        for line in traceback.format_stack():
            print(line.strip())

        print(rurl)
        print(rparams)

    if binary:
        return requests.get(rurl + rparams).content

    rstr = requests.get(rurl + rparams).content.decode()
    robj = json.loads(rstr)

    if 'data' in robj:
        robj = robj['data']

    if debugging > 0:
        print(rurl + rparams)
        print(rstr)
        print()

    return robj


def test_connection() -> bool:
    """Checks if the JDownloader is reachable.

    This makes a dummy-request to the JDownloader and returns, if it was
    successful

    :returns: Connection status
    :rtype: bool
    """

    try:
        requests.get(base_url + 'jd/version')
        return True
    except Exception:
        pass

    return False


def version() -> str:
    """Returns the version of the connected JDownloader.

    :returns: JDownloader version
    :rtype: str
    """

    route = 'jd/version'
    return make_request(route, None)
