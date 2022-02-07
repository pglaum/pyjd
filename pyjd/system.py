from typing import Any


class System:
    def __init__(self, device):
        self.device = device
        self.endpoint = "system"

    def action(self, route: str, params: Any = None) -> Any:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params)

    def exit_jd(self):
        """Stop the JDownloader."""

        resp = self.action("/exitJD")
        return resp

    def get_storage_infos(self, path=None):
        """Get storage information."""

        params = [path]
        resp = self.action("/getStorageInfos", params)
        return resp

    def get_system_infos(self):
        """Get system information."""

        resp = self.action("/getSystemInfos")
        return resp

    def hibernate_os(self):
        """Hibernate the OS."""

        resp = self.action("/hibernateOS")
        return resp

    def restart_jd(self):
        """Restart the JDownloader."""

        resp = self.action("/restartJD")
        return resp

    def shutdown_os(self, force=False):
        """Shutdown the OS."""

        params = [force]
        resp = self.action("/shutdownOS", params)
        return resp

    def standby_os(self):
        """Put the OS in standby."""

        resp = self.action("/standbyOS")
        return resp
