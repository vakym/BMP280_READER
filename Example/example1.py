from BMP280 import BMP280

if __name__ == "__main__":
    BMP280.config(1, 0X77)
    BMP280.init()
    BMP280.close()