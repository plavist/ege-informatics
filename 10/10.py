from ipaddress import *

net = ip_network("46.29.170.214/255.255.128.0", strict=False)

count = 0
for ip in net:
    octets = list(map(int, str(ip).split('.')))
    s = sum(octets)

    if octets[0] == s -octets[0] or octets[1] == s -octets[1] or octets[2] == s - octets[2] or octets[3] == s - octets[3]:
        print(ip)


print(net.network_address)
print(net.broadcast_address)

print(net[5])

print(net[-5])