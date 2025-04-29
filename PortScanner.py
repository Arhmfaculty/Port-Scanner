import socket
import ipaddress
from datetime import datetime


def portScanner(ip, start_port, end_port):
    open_ports = []
    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")
    start_time = datetime.now()

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
        except KeyboardInterrupt:
            print("Scan interrupted by user.")
            return
        except socket.error:
            print(f"Couldn't connect to server at {ip}.")
            return

    end_time = datetime.now()
    duration = end_time - start_time

    if open_ports:
        print(f"\nOpen ports on {ip}: {open_ports}")
    else:
        print("\nNo open ports found.")

    print(f"Scan completed in {duration}")

def main():
    user_input = input("Enter IP address or domain to scan: ").strip()

    try:
        ip = socket.gethostbyname(user_input)  # Resolves domain name to IP
    except socket.gaierror:
        print("Invalid domain or IP address.")
        return

    try:
        start_port = int(input("Enter start port: ").strip())
        end_port = int(input("Enter end port: ").strip())
        if not (0 <= start_port <= 65535 and 0 <= end_port <= 65535 and start_port <= end_port):
            print("Invalid port range. Must be between 0-65535 and start <= end.")
            return
    except ValueError:
        print("Port numbers must be integers.")
        return

    portScanner(ip, start_port, end_port)

if __name__ == "__main__":
    main()
