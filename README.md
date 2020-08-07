# 3agL3
Sniffing network traffic with Python for real-time or PCAP analysis.

## > Pip Requirements
```
scapy
colored
netaddr
netifaces
```

## Npcap/Tcpdump Installation
- Download Npcap for **Windows**:
    - https://nmap.org/download.html
- Install Tcpdump: **Ubuntu/Debian**:
    - `sudo apt install tcpdump -y`
- Install Tcpdump: **CentOS/RHEL**:
    - `yum install tcpdump -y`

## 3agL3 Modes of Operation: Live, Read, Write
## > Live Mode
    - Args:
    ```python
    live_capture.add_argument("-live", "--live-mode",action="store_true",default=False,help="Perfrom live capture analysis")

	if system() == "Windows":
		live_capture.add_argument("-i", "--interf",nargs="*",help="The interface to listen on (more than one can be specified)")
	else:
		live_capture.add_argument("-i", "--interf", nargs="*",help="The interface to listen on (more than one is allowed)")

	live_capture.add_argument("-c", "--count",metavar="<NUM>",type=int, default=0,help="The number of packets to capture (default = 0 = infinity)")
	live_capture.add_argument("-f", "--filter",metavar="<BPF FITLER>",type=str, default=None,help="Berkeley packet filter to apply to capture")
    ```

## > Read Mode
    - 
    
## > Write Mode
    - 
## > Berkeley Packet Filter Examples
```
# Matching IP
-------------
dst host 192.168.1.0
src host 192.168.1
dst host 172.16
src host 10
host 192.168.1.0
host 192.168.1.0/24
src host 192.168.1/24

# Matching Port/Portranges
--------------------------
src port <PORT>
dst port <PORT>
port <PORT>
src portrange 80-88
tcp portrange 1501-1549

# Matching MAC
--------------
ether host <MAC>
ether src host <MAC>
ether dst host <MAC>

# All supported protocols to filter by
---------------------------------------
arp
ether
fddi
icmp
ip
ip6
link
ppp
radio
rarp
slip
tcp
tr
udp
wlan
```
Check out this [link](https://www.ibm.com/support/knowledgecenter/en/SS42VS_7.3.3/com.ibm.qradar.doc/c_forensics_bpf.html) for more Berkeley Packet Filters.
