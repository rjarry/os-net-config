# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import netaddr


class NetworkObjectException(Exception):
    pass


class Route(object):
    """Base class for network routes."""

    def __init__(self, netmask_cidr, gateway):
        self.netmask_cidr = netmask_cidr
        self.gateway = gateway


class Address(object):
    """Base class for network addresses."""

    def __init__(self, ip_netmask, routes=[]):
        self.ip_netmask = ip_netmask
        ip_nw = netaddr.IPNetwork(self.ip_netmask)
        self.ip = str(ip_nw.ip)
        self.netmask = str(ip_nw.netmask)
        self.version = ip_nw.version
        self.routes = routes


class Interface(object):
    """Base class for network interfaces."""

    def __init__(self, name, use_dhcp=False, use_dhcpv6=False, addresses=[],
                 mtu=1500):
        self.name = name
        self.mtu = mtu
        self.use_dhcp = use_dhcp
        self.addresses = addresses
        self.bridge = None
        self.type = None

    def v4_addresses(self):
        v4_addresses = []
        for addr in self.addresses:
            if addr.version == 4:
                v4_addresses.append(addr)

        return v4_addresses

    def v6_addresses(self):
        v6_addresses = []
        for addr in self.addresses:
            if addr.version == 6:
                v6_addresses.append(addr)

        return v6_addresses
