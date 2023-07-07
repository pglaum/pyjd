from .jd_types import LinkCheckResult
from typing import Optional, Any


class Toolbar:
    def __init__(self, device):
        self.device = device
        self.endpoint = "toolbar"

    def action(self, route: str, params: Optional[Any] = None) -> Any:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params)

    def add_links_from_dom(self):
        """Unknown."""

        resp = self.action("/addLinksFromDOM")
        return resp

    def check_links_from_dom(self):
        """Unknown."""

        resp = self.action("/checkLinksFromDOM")
        return resp

    def get_status(self):
        """Get JDownloader status.

        Example result:

        .. code-block :: json

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

        resp = self.action("/getStatus")
        return resp

    def is_available(self):
        """Unknown."""

        resp = self.action("/isAvailable")
        return resp

    def poll_checked_links_from_dom(self, check_id):
        """Unknown."""

        params = [check_id]
        resp = self.action("/pollCheckedLinksFromDOM", params)
        link_check_result = LinkCheckResult(**resp)
        return link_check_result

    def special_url_handling(self, url):
        """Unknown."""

        params = [url]
        resp = self.action("/specialURLHandling", params)
        return resp

    def start_downloads(self):
        """Start downloads."""

        resp = self.action("/startDownloads")
        return resp

    def stop_downloads(self):
        """Stops the downloads."""

        resp = self.action("/stopDownloads")
        return resp

    def toggle_automatic_reconnect(self):
        """Unknown."""

        resp = self.action("/toggleAutomaticReconnect")
        return resp

    def toggle_clipboard_monitoring(self):
        """Unknown."""

        resp = self.action("/toggleClipboardMonitoring")
        return resp

    def toggle_download_speed_limit(self):
        """Unknown."""

        resp = self.action("/toggleDownloadSpeedLimit")
        return resp

    def toggle_pause_downloads(self):
        """Unknown."""

        resp = self.action("/togglePauseDownloads")
        return resp

    def toggle_premium(self):
        """Unknown."""

        resp = self.action("/togglePremium")
        return resp

    def toggle_stop_after_current_download(self):
        """Unknown."""

        resp = self.action("/toggleStopAfterCurrentDownload")
        return resp

    def trigger_update(self):
        """Unknown."""

        resp = self.action("/triggerUpdate")
        return resp
