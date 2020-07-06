from .jd import make_request
from .jd_types import AdvancedConfigAPIEntry, AdvancedConfigQuery, EnumOption
from typing import Any, List

endpoint = 'config'


def action(route: str, params: Any = None) -> Any:
    route = f'{endpoint}{route}'
    return make_request(route, params)


def get(interface_name: str, storage: str, key: str) -> Any:
    """Get value from interface by key.

    :param interface_name: The name of the JDownloader interface
    :type interface_name: str
    :param storage: The storage for the config entry.
        (None, for normal settings, or the extensions name for extension
        settings)
    :type storage: str
    :param key: The key of the config entry
    :type key: str
    :returns: The value of the config entry
    :rtype: Any
    """

    params = [interface_name, storage, key]
    resp = action("/get", params)
    return resp


def get_default(interface_name: str, storage: str, key: str) -> Any:
    """Get default value from interface by key.

    :param interface_name: The name of the JDownloader interface
    :type interface_name: str
    :param storage: The storage for the config entry.
        (None, for normal settings, or the extensions name for extension
        settings)
    :type storage: str
    :param key: The key of the config entry
    :type key: str
    :returns: The default value of the config entry
    :rtype: Any
    """

    params = [interface_name, storage, key]
    resp = action("/getDefault", params)
    return resp


def list(pattern: str = "", returnDescription: bool = True,
        returnValues: bool = True, returnDefaultValues: bool = True,
        returnEnumInfo: bool = True) -> List[AdvancedConfigAPIEntry]:
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

    params = [pattern, returnDescription, returnValues,
              returnDefaultValues, returnEnumInfo]
    resp = action("/list", params)

    config_api_entries = []
    for entry in resp:
        config_api_entry = AdvancedConfigAPIEntry(entry)
        config_api_entries.append(config_api_entry)

    return config_api_entries


def list_enum(enum_type: str) -> List[EnumOption]:
    """List all possible enum values for the type.

    The enum_type is the AdvancedConfigAPIEntry.config_type for an Enum.
    (e.g.: 'org.jdownloader.settings.DelayWriteMode')

    :param enum_type: The enum type
    :type enum_type: str
    :returns: A list of possible options for the enum_type
    :rtype: List[EnumOption]
    """

    params = [enum_type]
    resp = action("/listEnum", params)

    enum_options = []
    for entry in resp:
        enum_option = EnumOption(entry)
        enum_options.append(enum_option)

    return enum_options


def query(advanced_config_query: AdvancedConfigQuery = AdvancedConfigQuery()
        ) -> List[AdvancedConfigAPIEntry]:
    """Query config entries with an :class:`AdvancedConfigQuery`.

    :param advanced_config_query: The query options
    :type advanced_config_query: AdvancedConfigQuery
    :returns: A list of config entries
    :rtype: List[AdvancedConfigAPIEntry]
    """

    params = [advanced_config_query.to_dict()]
    resp = action("/query", params=params)

    config_api_entries = []
    for entry in resp:
        config_api_entry = AdvancedConfigAPIEntry(entry)
        config_api_entries.append(config_api_entry)

    return config_api_entries


def reset(interface_name: str, storage: str, key: str) -> bool:
    """Reset a config entry.

    :param interface_name: The name of the JDownloader interface
    :type interface_name: str
    :param storage: The storage for the config entry.
        (None, for normal settings, or the extensions name for extension
        settings)
    :type storage: str
    :param key: The key of the config entry
    :type key: str
    :returns: Success
    :rtype: bool
    """

    params = [interface_name, storage, key]
    resp = action("/reset", params)
    return resp


def set(interface_name: str, storage: str, key: str, value: str) -> bool:
    """Set a config entry.

    :param interface_name: The name of the JDownloader interface
    :type interface_name: str
    :param storage: The storage for the config entry.
        (None, for normal settings, or the extensions name for extension
        settings)
    :type storage: str
    :param key: The key of the config entry
    :type key: str
    :param value: The new value for the config. Integers, booleans, etc.
        should be converted to strings.
    :type value: str
    :returns: Success
    :rtype: bool
    """

    params = [interface_name, storage, key, value]
    resp = action("/set", params)
    return resp
