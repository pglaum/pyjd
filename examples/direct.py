"""
Direct connection example
=========================

This script gives a short overview of how to connect to a JDownloader on the
localhost.
"""

from pyjd.direct_connector import DirectConnector

conn = DirectConnector()
jdownloader = conn.get_device()

system_infos = jdownloader.system.get_system_infos()
print(system_infos)
