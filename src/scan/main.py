"""Basic TCP port scanner script."""

from __future__ import annotations

import argparse
import socket


def scan_ports(host: str, start: int, end: int, timeout: float = 0.5) -> list[int]:
    """Return a list of open TCP ports on ``host`` between ``start`` and ``end``."""
    open_ports: list[int] = []
    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            if sock.connect_ex((host, port)) == 0:
                open_ports.append(port)
    return open_ports


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan a host for open TCP ports")
    parser.add_argument("host", help="Host name or IP address to scan")
    parser.add_argument("--start", type=int, default=1, help="Starting port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="Ending port (default: 1024)")
    args = parser.parse_args()

    print(f"Scanning {args.host} from port {args.start} to {args.end}...")
    open_ports = scan_ports(args.host, args.start, args.end)
    if open_ports:
        print("Open ports found:")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found in the specified range.")


if __name__ == "__main__":
    main()
