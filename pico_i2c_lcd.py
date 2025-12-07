import machine
import time

class I2cLcd:
    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        self.i2c = i2c
        self.i2c_addr = i2c_addr
        self.backlight_val = 0x08
        self.num_lines = num_lines
        self.num_columns = num_columns
        
        time.sleep_ms(20)
        self.write_nibble(0x03) 
        time.sleep_ms(5)
        self.write_nibble(0x03) 
        time.sleep_ms(5)
        self.write_nibble(0x03)
        time.sleep_ms(5)
        self.write_nibble(0x02)
        time.sleep_ms(5)
        
        self.send_command(0x28) 
        self.send_command(0x08)
        self.send_command(0x01) 
        time.sleep_ms(2)
        self.send_command(0x06)
        self.send_command(0x0C) 

    def write_nibble(self, data):
        val = (data << 4) | self.backlight_val
        self.i2c.writeto(self.i2c_addr, bytearray([val | 0x04]))
        self.i2c.writeto(self.i2c_addr, bytearray([val]))

    def send_byte(self, data, mode):
        high = mode | (data & 0xF0) | self.backlight_val
        low = mode | ((data << 4) & 0xF0) | self.backlight_val
        
        self.i2c.writeto(self.i2c_addr, bytearray([high | 0x04]))
        self.i2c.writeto(self.i2c_addr, bytearray([high]))
        
        self.i2c.writeto(self.i2c_addr, bytearray([low | 0x04]))
        self.i2c.writeto(self.i2c_addr, bytearray([low]))

    def send_command(self, cmd):
        self.send_byte(cmd, 0)

    def send_data(self, data):
        self.send_byte(data, 1)

    def clear(self):
        self.send_command(0x01)
        time.sleep_ms(2)

    def move_to(self, col, row):
        offsets = [0x00, 0x40, 0x14, 0x54]
        if row > 3: row = 3
        addr = col + offsets[row]
        self.send_command(0x80 | addr)

    def putstr(self, string):
        for char in string:
            self.send_data(ord(char))
