import json
import requests
import traceback

base_url = 'http://localhost:3128/'
debugging = True


def make_request(endpoint, params, binary=False, method='GET'):
    rurl = f'{base_url}{endpoint}'

    rparams = []
    if params:
        for param in params:
            rparams.append(json.dumps(param))
    rparams = '?' + '&'.join(rparams)

    if debugging:
        for line in traceback.format_stack():
            print(line.strip())

        print(rurl)
        print(rparams)

    if binary:
        return requests.get(rurl + rparams).content

    rstr = requests.get(rurl + rparams).content.decode()
    robj = json.loads(rstr)
    robj = robj['data']

    if debugging:
        print(rstr)
        print()

    return robj
