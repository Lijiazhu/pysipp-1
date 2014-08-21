#Carrier / SIP Tester
This is a test tool to iterate over a list of phone numbers (or numbers pulled from a ORM/Table.)
Each number that is called (along with it's proxy) are returned as either passing/failing to complete the call.

Asynchronously a packet capture is made during the test of a call. Post capture, the pcap is analyzed, and
the audio from the call is pulled out and saved to a audio file.

Post phone call, a call to PESQ would be made to compare the audio quality against the known audio on the call (i.e. the
phone number plays back an audio file we have on hand and use the PESQ tool to compare the difference in
audio quality), with the consideraiton that the SLA should have a PESQ score in the realm of telephony scores
(2.3 or higher.)

Post test, the results are saved to a CSV file.  Future enhancements here, should save the results to a database.

##Packages Used
- PESQ (must be compiled on the test computer)
- PyShark (must be modified in order to use with Python 3)
- SIPP (must be compiled on the system. This is used to place the sipp call)

PESQ was used as it's a ready to go audio quality scoring algorithm.
PyShark was utilized to parse RTP channels from the pcap
SIPP was used to place sip calls, as SIP libraries in Python aren't common, I opted for this choice.

