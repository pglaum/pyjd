import json
import requests

base_url = 'http://localhost:3128/'
debugging = True


def make_request(endpoint, params, method='GET'):
    rurl = f'{base_url}{endpoint}'

    rparams = []
    if params:
        for param in params:
            if not isinstance(param, list):
                rparams.append(json.dumps(param))
            else:
                rparams.append(param)
    rparams = '?' + '&'.join(rparams)

    if debugging:
        print(rurl)
        print(rparams)
        print()

    rstr = requests.get(rurl + rparams).content.decode()
    robj = json.loads(rstr)
    robj = robj['data']

    return robj
