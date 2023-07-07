from .jd_types import Context, MenuStructure
from typing import Optional, Any, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .jd_device import JDDevice


class UI:
    def __init__(self, device: "JDDevice") -> None:
        self.device = device
        self.endpoint = "ui"

    def action(self, route: str, params: Optional[Any] = None) -> Any:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params)

    def get_menu(self, context: Context) -> MenuStructure:
        """Get the custom menu structure for the desired context."""

        params = [context.value]
        resp = self.action("/getMenu", params)
        menu_item = MenuStructure(**resp)
        return menu_item

    def invoke_action(
        self,
        context: Context,
        action_id: int,
        link_ids: List[int],
        package_ids: List[int],
    ) -> str:
        """Invoke a menu action on our selection and get the results."""

        params = [context, action_id, link_ids, package_ids]
        resp = self.action("/invokeAction", params)
        return resp
