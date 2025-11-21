from port_scanner import get_open_ports

print(get_open_ports("scanme.nmap.org", [20, 80], True))
