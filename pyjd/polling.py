from .jd import make_request
from .jd_types import APIQuery

endpoint = 'polling'


def action(route, params=None):
    route = f'{endpoint}{route}'
    return make_request(route, params)


def poll(query_params=APIQuery()):
    """Poll for APIQuery.
    """

    params = [query_params.to_dict()]
    resp = action("/poll", params)
    return resp
