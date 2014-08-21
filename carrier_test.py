from dialer import Dialer
class CarrierTest(Dialer):
    def test_carrier_call(self):
        tc= super().place_call(self.dnis,self.proxy)
        return tc

