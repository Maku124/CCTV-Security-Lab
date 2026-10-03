#!/usr/bin/env python3

import socket
import sys

COMMON_PORTS = {
    80: "HTTP",
    443: "HTTPS",
    554: "RTSP",
    8080: "HTTP-ALT",
    8443: "HTTPS-ALT",
}


def check_port(ip, port, timeout=1):
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def scan_camera_ports(ip):
    print(f"\nScanning authorized target: {ip}")
    print("-" * 45)

    for port, service in COMMON_PORTS.items():
        if check_port(ip, port):
            print(f"[OPEN]   {port}/tcp  {service}")
        else:
            print(f"[CLOSED] {port}/tcp  {service}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 cctv_scanner.py <IP>")
        print("Example: python3 cctv_scanner.py 127.0.0.1")
        sys.exit(1)

    target = sys.argv[1]

    try:
        socket.inet_aton(target)
    except OSError:
        print("Invalid IPv4 address.")
        sys.exit(1)

    scan_camera_ports(target)


if __name__ == "__main__":
    main()
