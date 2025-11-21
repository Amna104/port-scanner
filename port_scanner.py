import socket
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    # Validate/resolve hostname/IP
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        if all(c.isdigit() or c == '.' for c in target):
            return "Error: Invalid IP address"
        else:
            return "Error: Invalid hostname"

    # Scan ports
    start, end = port_range

    for port in range(start, end + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        if sock.connect_ex((ip, port)) == 0:
            open_ports.append(port)

        sock.close()

    # Verbose mode
    if verbose:
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname = target

        lines = []
        lines.append(f"Open ports for {hostname} ({ip})")
        lines.append("PORT     SERVICE")

        for p in open_ports:
            service = ports_and_services.get(p, "unknown")
            lines.append(f"{p:<9}{service}")

        return "\n".join(lines)

    return open_ports
