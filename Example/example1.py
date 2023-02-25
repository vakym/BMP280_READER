from BMP280.BMP280 import BMP280

if __name__ == "__main__":
    sensor = BMP280(1, 0x77)
    sensor.init()
    sensor.close()