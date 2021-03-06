import I2C_LCD_driver
import socket
import fcntl
import struct
import time

lcdi2c = I2C_LCD_driver.lcd()

#Initial info
lcdi2c.lcd_display_string("Esteirense", 1,1)
lcdi2c.lcd_display_string("LCD I2C e RPi", 2,1)
time.sleep(2)

#Clear display
lcdi2c.lcd_clear()

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, 
        struct.pack('256s', ifname[:15])
    )[20:24])

#Show IP (3g modem)
lcdi2c.lcd_display_string("IP", 1)
lcdi2c.lcd_display_string(get_ip_address('ppp0'), 1,3)
 
while True:
#Show date
    lcdi2c.lcd_display_string("Data: %s" %time.strftime("%d/%m/%y"), 2,1)

time.sleep(5)
lcdi2c.lcd_clear()
