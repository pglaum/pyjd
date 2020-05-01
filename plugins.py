from pyjd import make_request
from pyjd.jd_types import AdvancedConfigQuery, AdvancedConfigAPIEntry, Plugin, \
    PluginsQuery

endpoint = 'plugins'


def action(route, params=None):
    route = f'{endpoint}{route}'
    return make_request(route, params)


def get(interface_name, display_name, key):
    """Get a plugin."""

    params = [interface_name, display_name, key]
    resp = action('/get', params)

    return resp


def get_all_plugin_regex():
    """Get all plugin regular expressions."""

    resp = action('/getAllPluginRegex')

    return resp


def get_plugin_regex(url):
    """Get plugin regular expressions for a url."""

    params = [url]
    resp = action('/getAllPluginRegex', params)

    return resp


def list(plugins_query=PluginsQuery()):
    """List plugins with query."""

    params = [plugins_query.to_dict()]
    resp = action('/list', params)

    plugins = []
    for p in resp:
        plugin = Plugin(p)
        plugins.append(plugin)

    return plugins


def query(config_query=AdvancedConfigQuery()):
    """Query plugin configurations."""

    params = [config_query.to_dict()]
    resp = action('/query', params)

    entries = []
    for c in resp:
        entry = AdvancedConfigAPIEntry(c)
        entries.append(entry)

    return entries


def reset(interface_name, display_name, key):
    """Reset plugin config."""

    params = [interface_name, display_name, key]
    resp = action('/reset', params)

    return resp


def set(interface_name, display_name, key, new_value):
    """Set a plugin config value."""

    params = [interface_name, display_name, key, new_value]
    resp = action('/set', params)

    return resp
