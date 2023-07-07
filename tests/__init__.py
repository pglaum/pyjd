import sys, os

from pyjd.direct_connector import DirectConnector

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def get_jdownloader():
    conn = DirectConnector("http://jdownloader:3128")
    jdownloader = conn.get_device()

    return jdownloader
