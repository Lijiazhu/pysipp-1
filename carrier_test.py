from dialer import Dialer
import pyshark, time, threading, queue

class CarrierTest(Dialer):

    def test_carrier_call(self):
        # q1 = queue.Queue()
        t1 = threading.Thread(target=self.caller_audio).start()
        tc= threading.Thread(target=super().place_call(self.dnis,self.proxy)).start()

        return tc

    def capturepcap(self):
        cap = pyshark.LiveCapture().sniff(timeout=10)
        file_name = self.dnis+"_"+self.proxy+"_caller.pcap"
        file = open(file_name,"w")
        file.write(str(cap))
        file.close()

    def caller_audio(self):
        rtp_list = []
        # cap = pyshark.FileCapture('caller.pcap', display_filter='rtp')
        cap = pyshark.LiveCapture(interface='en0')
        file_name = self.dnis+"_"+self.proxy+"_audio.raw"
        raw_audio = open(file_name,'wb+')
        for i in cap:
            try:
                rtp = i[3]
                if rtp.payload:
                     print(rtp.payload)
                     rtp_list.append(rtp.payload.split(":"))
            except:
                pass

        for rtp_packet in rtp_list:
            packet = " ".join(rtp_packet)
            print(packet)
            audio = bytearray.fromhex(packet)
            raw_audio.write(audio)

