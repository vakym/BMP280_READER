from enum import IntFlag
class REGISTER(IntFlag):
#BMP280 register address
    BMP280_REGISTER_DIG_T1 = 0x88
    BMP280_REGISTER_DIG_T2 = 0x8A
BMP280_REGISTER_DIG_T3 = 0x8C
BMP280_REGISTER_DIG_P1 = 0x8E
BMP280_REGISTER_DIG_P2 = 0x90
BMP280_REGISTER_DIG_P3 = 0x92
BMP280_REGISTER_DIG_P4 = 0x94
BMP280_REGISTER_DIG_P5 = 0x96
BMP280_REGISTER_DIG_P6 = 0x98
BMP280_REGISTER_DIG_P7 = 0x9A
BMP280_REGISTER_DIG_P8 = 0x9C
BMP280_REGISTER_DIG_P9 = 0x9E 

BMP280_REGISTER_CHIPID = 0xD0
BMP280_REGISTER_VERSION = 0xD1
BMP280_REGISTER_SOFTRESET = 0xE0
BMP280_REGISTER_STATUS = 0xF3
BMP280_REGISTER_CONTROL = 0xF4
BMP280_REGISTER_CONFIG = 0xF5

BMP280_TEMP_XLSB_REG = 0xFC #Temperature XLSB Register
BMP280_TEMP_LSB_REG = 0xFB #Temperature LSB Register
BMP280_TEMP_MSB_REG =    0xFA #Temperature LSB Register
BMP280_PRESS_XLSB_REG =  0xF9 #Pressure XLSB Register
BMP280_PRESS_LSB_REG =   0xF8 #Pressure LSB Register
BMP280_PRESS_MSB_REG =   0xF7 #Pressure MSB Register

#calibration parameters
BMP280_DIG_T1_LSB_REG = 0x88  
BMP280_DIG_T1_MSB_REG = 0x89  
BMP280_DIG_T2_LSB_REG = 0x8A  
BMP280_DIG_T2_MSB_REG = 0x8B  
BMP280_DIG_T3_LSB_REG = 0x8C  
BMP280_DIG_T3_MSB_REG = 0x8D  
BMP280_DIG_P1_LSB_REG = 0x8E  
BMP280_DIG_P1_MSB_REG = 0x8F  
BMP280_DIG_P2_LSB_REG = 0x90  
BMP280_DIG_P2_MSB_REG = 0x91  
BMP280_DIG_P3_LSB_REG = 0x92  
BMP280_DIG_P3_MSB_REG = 0x93  
BMP280_DIG_P4_LSB_REG = 0x94  
BMP280_DIG_P4_MSB_REG = 0x95  
BMP280_DIG_P5_LSB_REG = 0x96  
BMP280_DIG_P5_MSB_REG = 0x97  
BMP280_DIG_P6_LSB_REG = 0x98  
BMP280_DIG_P6_MSB_REG = 0x99  
BMP280_DIG_P7_LSB_REG = 0x9A  
BMP280_DIG_P7_MSB_REG = 0x9B  
BMP280_DIG_P8_LSB_REG = 0x9C  
BMP280_DIG_P8_MSB_REG = 0x9D  
BMP280_DIG_P9_LSB_REG = 0x9E  
BMP280_DIG_P9_MSB_REG = 0x9F