from .jd_types import MenuStructure
from typing import Any


class UI:
    def __init__(self, device):
        self.device = device
        self.endpoint = "ui"

    def action(self, route: str, params: Any = None) -> Any:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params)

    def get_menu(self, context):
        """Get the custom menu structure for the desired context."""

        params = [context.value]
        resp = self.action("/getMenu", params)
        menu_item = MenuStructure(resp)
        return menu_item

    def invoke_action(self, context, action_id, link_ids, package_ids):
        """Invoke a menu action on our selection and get the results."""

        params = [context, action_id, link_ids, package_ids]
        resp = self.action("/invokeAction", params)
        return resp
