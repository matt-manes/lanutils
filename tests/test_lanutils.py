import pytest

from lanutils import lanutils


def test__lanutils__get_myip():
    # Not gonna work if you aren't connected to your network
    assert len(lanutils.get_myip()) > 0
    assert any(ip[2] in ["Ethernet", "Wi-Fi"] for ip in lanutils.get_myip())
    assert len(lanutils.get_myip(None)) > 0


def test__lanutils__ip_is_alive():
    assert lanutils.ip_is_alive(lanutils.get_myip()[0][0])


def test__lanutils__enumerate_devices():
    assert len(lanutils.enumerate_devices()) > 0


# Start a http server in shell with command
# "py -m http.server 8000 -b {whatever is returned by lanutils.get_myip()[0][0]}"
# before running the following tests.
def test__lanutils__port_is_open():
    myip = lanutils.get_myip()[0][0]
    port = 8000
    assert lanutils.port_is_open(myip, port)


def test__lanutils__scan_ports():
    myip = lanutils.get_myip()[0][0]
    assert 8000 in lanutils.scan_ports(myip, (7999, 8001))


def test__lanutils__get_available_port():
    myip = lanutils.get_myip()[0][0]
    assert lanutils.get_available_port(myip, (8000, 8100)) > 8000
