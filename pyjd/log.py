from .jd import make_request
from .jd_types import LogFolder

endpoint = 'log'


def action(route, params=None):
    route = f'{endpoint}{route}'
    return make_request(route, params)


def get_available_logs():
    """Returns a list of available logs.

    :return: List of log folders
    :rtype: jd_types.LogFolder
    """

    resp = action("/getAvailableLogs")

    log_folders = []
    for folder in resp:
        log_folder = LogFolder(folder)
        log_folders.append(log_folder)

    return log_folders


def send_log_file(log_folders):
    """Returns a log file.

    :return: The log file
    :rtype: str
    """

    params = [log_folders]
    resp = action("/sendLogFile", params)
    return resp
