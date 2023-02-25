import smbus
from Registers import REGISTER

class BMP280:
    _bus = None
    _bmp280ChipId = 0x58
    def __init__(self, bus_number, device_address):
        self._bus_number = bus_number
        self._device_address = device_address
  
    def init(self):
        if __bus:
            self.close()
        __bus = smbus.SMBus(self._bus_number)
        chipId = __bus.read_byte_data(self._device_address, REGISTER.BMP280_REGISTER_CHIPID)
        if chipId != self._bmp280ChipId:
            raise Exception('Not supported chip')
        __bus.write_byte_data(self._device_address, REGISTER.BMP280_REGISTER_CONTROL, 0xFF)
        __bus.write_byte_data(self._device_address, REGISTER.BMP280_REGISTER_CONFIG, 0x14)

    def close(self):
        if self._bus:
            self._bus.close()
