def ip_to_le(ip_address):
    # Convert IP address to little-endian format
    parts = list(map(int, ip_address.split('.')))
    ip_le = ((parts[3] << 24) | (parts[2] << 16) | (parts[1] << 8) | parts[0])
    return hex(ip_le)

def port_to_le(port):
    # Convert port to little-endian format
    port_le = ((port & 0xFF) << 8) | ((port & 0xFF00) >> 8)
    return hex(port_le)

# Input IP address
ip_address_str = input("Enter the IP address (e.g., 127.0.0.1): ")

# Input port number
port_number = int(input("Enter the port number: "))

print()
# Get little-endian representation
result = ip_to_le(ip_address_str)

print(f"IP Address (little-endian): {result}")

# Get little-endian representation
result2 = port_to_le(port_number)

print(f"Port (little-endian): {result2}")