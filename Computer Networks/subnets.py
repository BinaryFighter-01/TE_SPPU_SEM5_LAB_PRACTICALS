import ipaddress

def subnet_info(ip_addr, num_subnets):
    net = ipaddress.ip_network(ip_addr, strict=False)
    new_prefix = net.prefixlen + (32 - net.prefixlen).bit_length() - (num_subnets - 1).bit_length()
    return list(net.subnets(new_prefix=new_prefix))

if __name__ == "__main__":
    ip = input("IP (e.g. 192.168.1.0/24): ")
    n = int(input("Number of subnets: "))
    
    for i, subnet in enumerate(subnet_info(ip, n), 1):
        print(f"\nSubnet {i}:")
        print(f"Network: {subnet.network_address}")
        print(f"Mask: {subnet.netmask}")
        print(f"Hosts: {subnet.num_addresses - 2}")


