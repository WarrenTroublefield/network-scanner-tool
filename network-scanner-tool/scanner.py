import socket
import sys

def scan_ports(host):
    print(f"Scanning {host}...")
    open_ports = []
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f" - {port}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <target IP>")
        sys.exit(1)
    scan_ports(sys.argv[1])
