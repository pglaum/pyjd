from .jd import make_request
from .jd_types import AdvancedConfigAPIEntry, EnumOption

endpoint = 'system'


def action(route, params=None):
    route = f'{endpoint}{route}'
    return make_request(route, params)


def exit_jd():
    """Stop the JDownloader."""

    resp = action("/exitJD")
    return resp


def get_storage_infos(path=None):
    """Get storage information."""

    params = [path]
    resp = action("/getStorageInfos", params)
    return resp


def get_system_infos():
    """Get system information."""

    resp = action("/getSystemInfos")
    return resp


def hibernate_os():
    """Hibernate the OS."""

    resp = action("/hibernateOS")
    return resp


def restart_jd():
    """Restart the JDownloader."""

    resp = action("/restartJD")
    return resp


def shutdown_os(force=False):
    """Shutdown the OS."""

    params = [force]
    resp = action("/shutdownOS", params)
    return resp


def standby_os():
    """Put the OS in standby."""

    resp = action("/standbyOS")
    return resp
