import pyshark

def capturepcap():
    cap = pyshark.LiveCapture(interface='en0')
    cap.sniff(timeout=10)
    cap
    file = open("caller.pcap","w+")
    file.write(str(cap[0]))
    file.close()

capturepcap()

# cap = pyshark.LiveCapture(interface='en0')
# cap.sniff(timeout=10)
# cap
# print(cap[0])