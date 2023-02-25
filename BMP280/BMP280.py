import smbus

BUS_NUMBER = 0
DEVICE_ADDRESS = 0
configure = False
bus = None
def config(bus_number, device_address):
    BUS_NUMBER = bus_number
    DEVICE_ADDRESS = device_address
    configure = True
    

def init():
    if not configure:
        raise Exception('Not configured')
    bus = smbus.SMBus(BUS_NUMBER)

def close():
    bus.close()
