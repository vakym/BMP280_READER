import smbus
from Registers import REGISTER

BUS_NUMBER = 0
DEVICE_ADDRESS = 0
BMP280_CHIP_ID = 0x58
configure = False
bus = None
def config(bus_number, device_address):
    BUS_NUMBER = bus_number
    DEVICE_ADDRESS = device_address
    configure = True
    

def init():
    if not configure:
        raise Exception('Not configured')
    if bus:
        close()
    bus = smbus.SMBus(BUS_NUMBER)
    chipId = bus.read_byte_data(DEVICE_ADDRESS, REGISTER.BMP280_REGISTER_CHIPID)
    if chipId != BMP280_CHIP_ID:
        raise Exception('Not supported chip')
    bus.write_byte_data(DEVICE_ADDRESS, REGISTER.BMP280_REGISTER_CONTROL, 0xFF)
    bus.write_byte_data(DEVICE_ADDRESS, REGISTER.BMP280_REGISTER_CONFIG, 0x14)

def close():
    bus.close()
