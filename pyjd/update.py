from .jd import make_request

endpoint = 'update'


def action(route, params=None):
    route = f'{endpoint}{route}'
    return make_request(route, params)


def is_update_available():
    """Returns if an update is available."""

    resp = action("/isUpdateAvailable")
    return resp


def restart_and_update():
    """Restarts and update."""

    resp = action("/restartAndUpdate")
    return resp


def run_update_check():
    """Runs an update check."""

    resp = action("/runUpdateCheck")
    return resp
