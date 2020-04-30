import json
import requests
import traceback

base_url = 'http://localhost:3128/'
debugging = 1


def make_request(endpoint, params, binary=False, method='GET'):
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
    robj = robj['data']

    if debugging > 0:
        print(rstr)
        print()

    return robj


def has_connection():
    try:
        requests.get(base_url + 'flash')
        return True
    except Exception:
        pass

    return False
