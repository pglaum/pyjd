from .jd_types import APIQuery
from typing import Any


class Polling:
    def __init__(self, device):
        self.device = device
        self.endpoint = "polling"

    def action(self, route: str, params: Any = None) -> Any:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params)

    def poll(self, query_params=APIQuery()):
        """Poll for APIQuery."""

        params = [query_params.to_dict()]
        resp = self.action("/poll", params)
        return resp
