import subprocess
class Dialer(object):
    def __init__(self, dnis, proxy):
        self.dnis = dnis
        self.proxy = proxy

    def place_call(self, dnis, proxy):
        command = ["sipp", "-s" ,dnis, proxy, "-sn" ,"uac" ,"-l", "1" ,"-m" ,"1" ,"-r", "1"]

        try:
            sipp_call = subprocess.check_call(command)
            if sipp_call == 0:
                result = True
        except:
            result = False
        return result
