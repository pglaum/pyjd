from typing import Any


class Update:

    def __init__(self, device):
        self.device = device
        self.endpoint = 'update'

    def action(self, route: str, params: Any = None) -> Any:
        route = f'/{self.endpoint}{route}'
        return self.device.connection_helper.action(route, params)

    def is_update_available(self):
        """Returns if an update is available."""

        resp = self.action("/isUpdateAvailable")
        return resp

    def restart_and_update(self):
        """Restarts and update."""

        resp = self.action("/restartAndUpdate")
        return resp

    def run_update_check(self):
        """Runs an update check."""

        resp = self.action("/runUpdateCheck")
        return resp
