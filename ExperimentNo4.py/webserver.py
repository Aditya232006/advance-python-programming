server_ip = (192, 168, 1, 1)
allowed_ips = ["192.168.1.2", "192.168.1.3"]

def update_ips(ip):
    allowed_ips.append(ip)

update_ips(input("Enter new allowed IP: "))

print("Server IP:", server_ip)
print("Allowed IPs:", allowed_ips)