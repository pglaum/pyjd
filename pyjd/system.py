from typing import Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .jd_device import JDDevice


class System:
    def __init__(self, device: "JDDevice") -> None:
        self.device = device
        self.endpoint = "system"

    def action(self, route: str, params: Optional[Any] = None) -> Any:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params)

    def exit_jd(self) -> str:
        """Stop the JDownloader."""

        resp = self.action("/exitJD")
        return resp

    def get_storage_infos(self, path: Optional[str] = None) -> dict:
        """Get storage information."""

        params = [path]
        resp = self.action("/getStorageInfos", params)
        return resp

    def get_system_infos(self) -> dict:
        """Get system information."""

        resp = self.action("/getSystemInfos")
        return resp

    def hibernate_os(self) -> str:
        """Hibernate the OS."""

        resp = self.action("/hibernateOS")
        return resp

    def restart_jd(self) -> str:
        """Restart the JDownloader."""

        resp = self.action("/restartJD")
        return resp

    def shutdown_os(self, force: bool = False) -> str:
        """Shutdown the OS."""

        params = [force]
        resp = self.action("/shutdownOS", params)
        return resp

    def standby_os(self) -> str:
        """Put the OS in standby."""

        resp = self.action("/standbyOS")
        return resp
