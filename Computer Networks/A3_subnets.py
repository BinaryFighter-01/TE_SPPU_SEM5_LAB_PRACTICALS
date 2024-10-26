import ipaddress

def calculate_subnets(ip_address, num_subnets):
    # Convert IP address to network object
    network = ipaddress.ip_network(ip_address, strict=False)
    # Calculate new prefix length
    new_prefix_length = network.prefixlen + (32 - network.prefixlen).bit_length() - (num_subnets - 1).bit_length()
    # Create subnets
    subnets = list(network.subnets(new_prefix=new_prefix_length))
    return subnets

def main():
    print("Subnetting Demonstration Program")
    print("--------------------------------")
    # Get input from user
    ip_address = input("Enter an IP address (e.g., 192.168.1.0/24): ")
    num_subnets = int(input("Enter the number of subnets to create: "))
    # Calculate subnets
    subnets = calculate_subnets(ip_address, num_subnets)
    # Display results
    print(f"\nSubnet Information for {ip_address} divided into {num_subnets} subnets:")
    print("------------------------------------------------------------")
    for i, subnet in enumerate(subnets, 1):
        print(f"Subnet {i}:")
        print(f"  Network Address: {subnet.network_address}")
        print(f"  Broadcast Address: {subnet.broadcast_address}")
        print(f"  Subnet Mask: {subnet.netmask}")
        print(f"  Prefix Length: /{subnet.prefixlen}")
        print(f"  Number of Usable Hosts: {subnet.num_addresses - 2}")
        print()

if __name__ == "__main__":
    main()
