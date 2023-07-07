from typing import Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .jd_device import JDDevice


class Update:
    def __init__(self, device: "JDDevice") -> None:
        self.device = device
        self.endpoint = "update"

    def action(self, route: str, params: Optional[Any] = None) -> Any:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params)

    def is_update_available(self) -> str:
        """Returns if an update is available."""

        resp = self.action("/isUpdateAvailable")
        return resp

    def restart_and_update(self) -> str:
        """Restarts and update."""

        resp = self.action("/restartAndUpdate")
        return resp

    def run_update_check(self) -> str:
        """Runs an update check."""

        resp = self.action("/runUpdateCheck")
        return resp
