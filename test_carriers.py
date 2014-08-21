from carrier_test import CarrierTest

results = []
phone_numbers = ["9995551212","999","18187205417"]
for p in phone_numbers:
    proxies = ["216.52.221.169","localhost"]
    for prox in proxies:
        ct = CarrierTest(p, prox)
        print(ct.test_carrier_call())

# ct = CarrierTest("9995551212","216.52.221.140")
# print(ct.test_carrier_call())
# ct = CarrierTest("9","localhost")
# print(ct.test_carrier_call())