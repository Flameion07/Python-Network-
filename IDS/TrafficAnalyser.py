class TrafficAnalyser():
    def __init__(self):
        # Tracks statistics for each connection
        # A tuple (source_ip, dest_ip, source_port, dest_port)
        self.connections = defaultdict(list) 
        # Tracks statistics for each connection
        self.flow_stats = defaultdic(lambda: {
            'packet_count': 0, # Total number of packets in the flow
            'byte_count': 0, # Total bytes transferred in the flow.
            'start_time': None, # Timestamp of the first packet in the flow.
            'last-time': None # Timestamp of the most recent packet in the flow.
        })
        
    # Analyzes a single packet and updates the statistics of its corresponding flow.    
    def analyze_packet(self,packet):
        if IP in packet and TCP in packet:
            # ip_src, ip_dst: Source and destination IPs.
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            # port_src, port_dst: Source and destination ports.
            port_src = packet[TCP].sport
            port_dst = packet[TCP].dport
            # A unique identifier for a flow based on the 4-tuple
            flow_key = (ip_src,ip_dst,port_src,port_dst)
            
            #Update flow statistics
            stats = self.flow_stats[flow_key]
            stats['packet_count'] +=1 # Increment packet_count
            stats['byte_count'] += len(packet) # Add the packet's length to byte_count 
            current_time = packet.time
            
            # Set or update start_time and last_time based on the packet's timestamp
            if not stats['start_time']:
                stats['start_time'] = current_time
            stats['last_time'] = current_time
            
            return self.extract_features(packet,stats)
    
    def extract_features(self,packet,stats):
        return{
            'packet_size': len(packet), # Length of the current packet in bytes.
            'flow_duration': stats['last_time'] - stats['start_time'], # Time difference between the first and last packet of the flow.
            'packet_rate': stats['packet_count'] / (stats['last_time'] - stats['start_time']), # Number of packets per second in the flow.
            'byte-range': stats['byte-count'] / (stats['last_time'] - stats['start_time']), # Number of bytes per second in the flow.
            'tcp_flags': packet[TCP].flags, # TCP flags from the current packet (e.g., SYN, ACK, etc.).
            'window_size': packet[TCP].window # TCP window size of the packet.
        }