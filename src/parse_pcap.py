from collections import Counter
from colored import fg, attr
from json import dump
from pprint import pprint

class PCAPParser:
    def filt_src_ip(self, capture, src_ip):
        """ Filter source IP addresses from capture """
        filtered = []
        for cap in capture:
            if cap[1].src == src_ip:
                filtered.append(cap)
        return filtered

    def filt_dst_ip(self, capture, dst_ip):
        """ Filter destination IP addresses from capture """
        filtered = []
        for cap in capture:
            if cap[1].dst == dst_ip:
                filtered.append(cap)
        return filtered

    def filt_src_port(self, capture, src_port):
        """
        """
        filtered = []
        for cap in capture:
            if cap[2].sport == int(src_port):
                filtered.append(cap)
        return filtered

    def filt_dst_port(self, capture, dst_port):
        """
        """
        filtered = []
        for cap in capture:
            if cap[2].dport == int(dst_port):
                filtered.append(cap)
        return filtered

    def filt_src_mac(self, capture, src_mac):
        """ """
        filtered = []
        for cap in capture:
            if cap[0].dst == src_mac:
                filtered.append(cap)
        return filtered

    def filt_dst_mac(self, capture, dst_mac):
        """ """
        filtered = []
        for cap in capture:
            if cap[0].src == dst_mac:
                filtered.append(cap)
        return filtered

    def filt_tcp(self):
        """ """
        
    def filt_udp(self):
        """ """

    def summary(self, capture):
        """ Prints a summary of the data contained in a capture.
        This summary includes:
            - unique IP and the number of times they appear
            - unique port number and the number of time they appear
            - unique mac addresses and the number of times they appear

        Args:
            capture (scapy.plist.PacketList): scapy packet capture list
        """
        print("[%sATTENTION%s] THIS MAY TAKE A COUPLE OF SECONDS" % (fg(202), attr(0)))

        # FILTERING IP ADDRESSES
        ip_list = [cap[1].src for cap in capture] + [cap[1].dst for cap in capture]

        ip_dict = Counter(ip_list)
        print("-"*50)
        for ip, count in ip_dict.most_common():
            print("%sIP%s: \'%s\', COUNT: %s" % (fg(124), attr(0), ip, count))
        print("-"*50)

        # FILTERING PORT NUMBERS
        port_list = [cap[2].sport for cap in capture] + [cap[2].dport for cap in capture]
        
        port_dict = Counter(port_list)
        for port, count in port_dict.most_common():
            print("%sPort%s: %s, COUNT: %s" % (fg(113), attr(0), port, count))
        print("-"*50)

        # FILTERING MAC ADDRESSES
        mac_list = [cap[0].src for cap in capture] + [cap[0].dst for cap in capture]

        mac_dict = Counter(mac_list)
        for mac, count in mac_dict.most_common():
            print("%sMAC%s: %s, COUNT: %s" % (fg(153), attr(0), mac, count))

        # FILTERING PACKETS LENGTHS
        i = 0
        pkt_len_sum = 0
        for cap in capture:
            i += 1
            pkt_len_sum += cap[0].len
        average_pkt_len = pkt_len_sum / i
        print("-"*50)
        print("%sAVERAGE PACKET LENGTH%s: %s bytes" % (fg(109), attr(0), average_pkt_len))

        # FILTERING TTL
        i = 0
        pkt_ttl_sum = 0
        for cap in capture:
            try:
                i += 1
                pkt_ttl_sum += cap[0].ttl
            except AttributeError:
                continue
        average_pkt_ttl = pkt_ttl_sum / i
        print("%sAVERAGE TTL%s: %s " % (fg(109), attr(0), average_pkt_ttl))

    def len_less_equal(self):
        """ """

    def len_greater_equal(self):
        """ """

    def len_equal(self):
        """ """

    def ttl_equal(self):
        """ """

    def json_summary(self, capture):
        """ Generate JSON file containing summary of packet capture.
        The JSON file will contain:
            - ip: count
            - port: count
            - mac: count
        
        Args:
            capture (scapy.plist.PacketList): scapy packet capture list
        """
        capture_summary = {}

        ip_list = [cap[1].src for cap in capture] + [cap[1].dst for cap in capture]
        ip_dict = Counter(ip_list)
        capture_summary["ip_dict"] = ip_dict

        port_list = [cap[2].sport for cap in capture] + [cap[2].dport for cap in capture]
        port_dict = Counter(port_list)
        capture_summary["port_dict"] = port_dict

        mac_list = [cap[0].src for cap in capture] + [cap[0].dst for cap in capture]
        mac_dict = Counter(mac_list)
        capture_summary["mac_dict"] = mac_dict
        
        try:
            with open("capture_summary.json", "w") as cap_sum_file:
                dump(capture_summary, cap_sum_file, indent=4)
        except:
            print(
				"[%sERROR%s] THERE WAS AN ERROR CREATING SUMMARY JSON FILE... PLEASE TRY AGAIN"
				% (fg(9), attr(0))
			)
