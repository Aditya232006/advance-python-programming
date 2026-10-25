import ipaddress

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

ip = input("Enter IP address: ")
print(validate_ip(ip))