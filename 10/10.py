from ipaddress import *

net = ip_network("192.168.159.86/255.255.252.0", strict=False)
print(net.network_address)