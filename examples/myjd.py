"""
MyJD connection example
=======================

This script gives a short overview of how to connect to a JDownloader vie the
MyJD API.

You'll have to use your email and password for the login.
"""

from pyjd.myjd_connector import MyJDConnector

conn = MyJDConnector()
conn.connect('your@email.com', 'your password')

devices = conn.list_devices()
print('Your JDownloaders:')
for d in devices:
    print('-', d['name'])

jdownloader = conn.get_device(device_id=devices[0]['id'])

system_infos = jdownloader.system.get_system_infos()
print(system_infos)
