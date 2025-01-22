import threading
import queue
from scapy.all import IP, TCP, sniff
from collections import defaultdict

class PacketSniffer():
    def __init__(self):
       # A thread-safe queue to store captured packets. 
       self.packet_queue=queue.Queue() 
       # A thread event that acts as a signal to stop the capture(sniffing process)
       self.stop_capture=threading.Event()
    
    # Method is called whenever a packet is captured by sniff()
    def packet_callback(self,packet):
        if IP in packet and TCP in packet:
            self.packet_queue.put(packet)
    
    # Packet Capture Here
    def start_capture(self, interface="eth0"):
        def capture_thread():
            sniff(iface=interface, # Specifies the network interface to sniff packets on (default is "eth0").
                  prn=self.packet_callback, # Passes each captured packet to the packet_callback mtd
                  store=0, # Avoids storing packets in memory
                  stop_filter=lambda _:self.stop_capture.is_set()) # A filter function to stop sniffing when stop_capture.is_set() becomes True       

        self.capture_thread = threading.Thread(target=capture_thread) #Stores the thread instance
        self.capture_thread.start()
        
    def stop(self):
        self.stop_capture.set() # Sets the stop_capture event, signaling the stop_filter in sniff() to terminate.
        self.capture_thread.join() # Waits for the sniffing thread to finish execution, ensuring clean termination.
        
        
        