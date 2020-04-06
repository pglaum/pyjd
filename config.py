from pyjd import make_request
from pyjd.jd_types import AdvancedConfigAPIEntry, EnumOption

endpoint = 'config'


def action(route, params=None):
    route = f'{endpoint}{route}'
    return make_request(route, params)


def get(interface_name, storage, key):
    """Get value from interface by key."""

    params = [interface_name, storage, key]
    resp = action("/get", params)
    return resp


def get_default(interface_name, storage, key):
    """Get default value from interface by key."""

    params = [interface_name, storage, key]
    resp = action("/getDefault", params)
    return resp


def list(pattern=None, returnDescription=True, returnValues=True,
         returnDefaultValues=True, returnEnumInfo=True):
    """List all available config entries.

    :param pattern: A regex pattern to query by. If no pattern is given, all
        config items will be returned
    :type pattern: str
    :param returnDescription: If description should be returned
    :type returnDescription: boolean
    :param returnValues: If values should be returned
    :type returnValues: boolean
    :param returnDefaultValues: If default values should be returned
    :type returnDefaultValues: boolean
    :param returnEnumInfo: If enum info should be returned
    :type returnEnumInfo: boolean
    :return: A list of (matching) config items
    :rtype: List[AdvancedConfigAPIEntry]
    """

    params = None
    if pattern:
        params = [pattern, returnDescription, returnValues,
                  returnDefaultValues, returnEnumInfo]
    resp = action("/list", params)

    config_api_entries = []
    for entry in resp:
        config_api_entry = AdvancedConfigAPIEntry(entry)
        config_api_entries.append(config_api_entry)

    return config_api_entries


def list_enum(enum_type):
    """List all possible enum values."""

    params = [enum_type]
    resp = action("/listEnum", params)
    return resp


def query(advanced_config_query):
    """Query config entries."""

    params = [advanced_config_query.to_dict()]
    resp = action("/query", params=params)

    config_api_entries = []
    for entry in resp:
        config_api_entry = AdvancedConfigAPIEntry(entry)
        config_api_entries.append(config_api_entry)

    return config_api_entries


def reset(interface_name, storage, key):
    """Reset a config entry."""

    params = [interface_name, storage, key]
    resp = action("/reset", params)
    return resp


def set(interface_name, storage, key, value):
    """Set a config entry."""

    params = [interface_name, storage, key, value]
    resp = action("/set", params)
    return resp
