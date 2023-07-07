from .jd_types import APIQuery
from typing import Optional, Any


class Polling:
    def __init__(self, device):
        self.device = device
        self.endpoint = "polling"

    def action(self, route: str, params: Optional[Any] = None) -> Any:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params)

    def poll(self, query_params=APIQuery.default()):
        """Poll for APIQuery."""

        params = [query_params.dict()]
        resp = self.action("/poll", params)
        return resp
