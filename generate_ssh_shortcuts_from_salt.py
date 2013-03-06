#!/usr/bin/python3.3

__author__ = 'ahammond'

from ipaddress import ip_address
from io import StringIO
from subprocess import check_output
from yaml import safe_load

# must be run as root on salt-master

salt_command = ["/usr/bin/salt", "*", "network.ip_addrs", "--out", "yaml"]

response = check_output(salt_command, universal_newlines=True)
response_stream = StringIO(response)
response_data = safe_load(response_stream)

for machine in sorted(response_data.keys()):
    filtered_addresses = [a for a in response_data[machine] if not ip_address(a).is_private]

    if filtered_addresses:
        print("Host", machine, "\n    HostName", filtered_addresses[0], "\n")
