from .jd import make_request
from .jd_types import LinkCheckResult

endpoint = 'toolbar'


def action(route, params=None):
    route = f'{endpoint}{route}'
    return make_request(route, params)


def add_links_from_dom():
    """Unknown."""

    resp = action("/addLinksFromDOM")
    return resp


def check_links_from_dom():
    """Unknown."""

    resp = action("/checkLinksFromDOM")
    return resp


def get_status():
    """Get JDownloader status.

    Example result:

        {
            "running" : false,
            "reconnect" : false,
            "premium" : true,
            "download_complete" : 0,
            "stopafter" : false,
            "limit" : false,
            "limitspeed" : 0,
            "state" : "STOPPED_STATE",
            "download_current" : 0,
            "clipboard" : true,
            "speed" : 0,
            "pause" : false
        }

    """

    resp = action("/getStatus")
    return resp


def is_available():
    """Unknown."""

    resp = action("/isAvailable")
    return resp


def poll_checked_links_from_dom(check_id):
    """Unknown."""

    params = [check_id]
    resp = action("/pollCheckedLinksFromDOM", params)
    link_check_result = LinkCheckResult(resp)
    return link_check_result


def special_url_handling(url):
    """Unknown."""

    params = [url]
    resp = action("/specialURLHandling", params)
    return resp


def start_downloads():
    """Start downloads."""

    resp = action("/startDownloads")
    return resp


def stop_downloads():
    """Stops the downloads."""

    resp = action("/stopDownloads")
    return resp


def toggle_automatic_reconnect():
    """Unknown."""

    resp = action("/toggleAutomaticReconnect")
    return resp


def toggle_clipboard_monitoring():
    """Unknown."""

    resp = action("/toggleClipboardMonitoring")
    return resp


def toggle_download_speed_limit():
    """Unknown."""

    resp = action("/toggleDownloadSpeedLimit")
    return resp


def toggle_pause_downloads():
    """Unknown."""

    resp = action("/togglePauseDownloads")
    return resp


def toggle_premium():
    """Unknown."""

    resp = action("/togglePremium")
    return resp


def toggle_stop_after_current_download():
    """Unknown."""

    resp = action("/toggleStopAfterCurrentDownload")
    return resp


def trigger_update():
    """Unknown."""

    resp = action("/triggerUpdate")
    return resp
