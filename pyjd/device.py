from .jd_types import DirectConnectionInfos
from typing import Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .jd_device import JDDevice


class Device:
    def __init__(self, device: "JDDevice"):

        self.device = device
        self.endpoint = "device"

    def action(self, route: str, params: Optional[Any] = None) -> Any:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params)

    def get_direct_connection_infos(self) -> Optional[DirectConnectionInfos]:

        resp = self.action("/getDirectConnectionInfos")
        if resp:
            return DirectConnectionInfos(**resp)

        return None

    def get_session_public_key(self) -> str:

        resp = self.action("/getSessionPublicKey")
        return resp

    def ping(self) -> bool:

        resp = self.action("/ping")
        return resp
