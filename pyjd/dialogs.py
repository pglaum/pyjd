from .jd_types import DialogInfo, DialogTypeInfo
from typing import Optional, Any, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .jd_device import JDDevice


class Dialogs:
    def __init__(self, device: "JDDevice") -> None:
        self.device = device
        self.endpoint = "dialogs"

    def action(self, route: str, params: Optional[Any] = None) -> bool:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params)

    def answer(self, id: int, data: dict) -> Any:
        """Answer the dialog.

        The data is a dictionary with the following keys:
            - dontshowagain OR dontshowagainselected: bool
            - closereason: 'OK' | 'CANCEL' | 'CLEAR' | 'TIMEOUT' | 'INTERRUPT'

        (see src/org/jdownloader/api/dialog/DialogApiImpl.java)

        :param id: Dialog id
        :type id: int
        :param data: Dialog answer data
        :type data: dict
        :returns: Response
        :rtype: Any
        """

        params = [id, data]
        resp = self.action("/answer", params)
        if resp == "":
            return True
        return False

    def get(self, id: int, icon: bool = True, properties: bool = True) -> DialogInfo:
        """Get the requested dialog info.

        :param id: Dialog id
        :type id: int
        :param icon: Whether to include the dialog icon, defaults to True
        :type icon: bool, optional
        :param properties: Whether to include the dialog properties, defaults to True
        :type properties: bool, optional
        :returns: Dialog info
        :rtype: DialogInfo
        """

        params = [id, icon, properties]
        resp = self.action("/get", params)
        return DialogInfo(**resp)

    def get_type_info(self, type: str) -> DialogTypeInfo:
        """Get the dialog type info.

        :param type: Dialog type
        :type type: str
        :returns: Dialog type info
        :rtype: DialogTypeInfo
        """

        params = [type]
        resp = self.action("/getTypeInfo", params)
        return DialogTypeInfo(**resp)

    def list(self) -> List[int]:
        """List all open dialog ids.

        :returns: List of dialog ids
        :rtype: List[int]
        """

        resp = self.action("/list")
        if not resp:
            return []
        return resp
