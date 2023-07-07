from .jd_types import AdvancedConfigQuery, AdvancedConfigAPIEntry, Plugin, PluginsQuery
from typing import Optional, Any


class Plugins:
    def __init__(self, device):
        self.device = device
        self.endpoint = "plugins"

    def action(self, route: str, params: Optional[Any] = None) -> Any:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params)

    def get(self, interface_name, display_name, key):
        """Get a plugin."""

        params = [interface_name, display_name, key]
        resp = self.action("/get", params)

        return resp

    def get_all_plugin_regex(self):
        """Get all plugin regular expressions."""

        resp = self.action("/getAllPluginRegex")

        return resp

    def get_plugin_regex(self, url):
        """Get plugin regular expressions for a url."""

        params = [url]
        resp = self.action("/getPluginRegex", params)

        return resp

    def list(self, plugins_query=PluginsQuery.default()):
        """List plugins with query."""

        params = [plugins_query.dict()]
        resp = self.action("/list", params)

        plugins = []
        for p in resp:
            plugin = Plugin(**p)
            plugins.append(plugin)

        return plugins

    def query(self, config_query=AdvancedConfigQuery.default()):
        """Query plugin configurations."""

        params = [config_query.dict()]
        resp = self.action("/query", params)

        entries = []
        for c in resp:
            entry = AdvancedConfigAPIEntry(**c)
            entries.append(entry)

        return entries

    def reset(self, interface_name, display_name, key):
        """Reset plugin config."""

        params = [interface_name, display_name, key]
        resp = self.action("/reset", params)

        return resp

    def set(self, interface_name, display_name, key, new_value):
        """Set a plugin config value."""

        params = [interface_name, display_name, key, new_value]
        resp = self.action("/set", params)

        return resp
