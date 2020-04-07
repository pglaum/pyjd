from pyjd import make_request
from pyjd.jd_types import MenuStructure

endpoint = 'ui'


def action(route, params=None):
    route = f'{endpoint}{route}'
    return make_request(route, params)


def get_menu(context):
    """Get the custom menu structure for the desired context."""

    params = [context.value]
    resp = action("/getMenu", params)
    menu_item = MenuStructure(resp)
    return menu_item


def invoke_action(context, action_id, link_ids, package_ids):
    """Invoke a menu action on our selection and get the results."""

    params = [context, action_id, link_ids, package_ids]
    resp = action("/invokeAction", params)
    return resp
