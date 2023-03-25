import nmap

def scan():
# Replace your_network_range with your actual network range (e.g., '192.168.1.0/24')
    network_range = input("Enter your network range (Eg: 192.168.1.0/24): ")

# Initialize the nmap.PortScanner object
    nm = nmap.PortScanner()

# Perform a ping scan on the specified network range
    nm.scan(hosts=network_range, arguments='-sn')

# Loop through the scan results and print the IP addresses and hostnames (if available) of the connected devices
    for host in nm.all_hosts():
        print(f'Host: {host} ({nm[host].hostname()})')
