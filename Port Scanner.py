import socket
from datetime import datetime

# User input
target = input("Enter IP address to scan: ")
start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))

print(f"\nScanning target: {target}")
print(f"Scan started at: {datetime.now()}")
print("-" * 50)

# Scan loop
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = sock.connect_ex((target, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"
        print(f"[+] Port {port} is open - {service}")
    sock.close()

print("-" * 50)
print(f"Scan completed at: {datetime.now()}")
