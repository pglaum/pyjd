from .jd_types import LogFolder
from typing import Optional, Any, List


class Log:
    def __init__(self, device):
        self.device = device
        self.endpoint = "log"

    def action(self, route: str, params: Optional[Any] = None) -> Any:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params)

    def get_available_logs(self) -> List[LogFolder]:
        """Returns a list of available logs.

        :return: List of log folders
        :rtype: jd_types.LogFolder
        """

        resp = self.action("/getAvailableLogs")

        log_folders = []
        for folder in resp:
            log_folder = LogFolder(**folder)
            log_folders.append(log_folder)

        return log_folders

    def send_log_file(self, log_folders) -> str:
        """Returns a log file.

        :return: The log file
        :rtype: str
        """

        params = [log_folders]
        resp = self.action("/sendLogFile", params)
        return resp
