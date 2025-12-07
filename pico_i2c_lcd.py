import machine
import time

class I2cLcd:
    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        self.i2c = i2c
        self.i2c_addr = i2c_addr
        self.backlight_val = 0x08 # Backlight ON by default
        self.num_lines = num_lines
        self.num_columns = num_columns
        
        # --- INISIALISASI KHUSUS (HARD RESET) ---
        # Ini penting agar LCD tidak muncul karakter aneh saat restart
        time.sleep_ms(20)
        self.write_nibble(0x03) # Wake up 1
        time.sleep_ms(5)
        self.write_nibble(0x03) # Wake up 2
        time.sleep_ms(5)
        self.write_nibble(0x03) # Wake up 3
        time.sleep_ms(5)
        self.write_nibble(0x02) # Set 4-bit mode
        time.sleep_ms(5)
        
        # Konfigurasi Layar
        self.send_command(0x28) # Function set: 4-bit, 2-line
        self.send_command(0x08) # Display OFF
        self.send_command(0x01) # Clear
        time.sleep_ms(2)
        self.send_command(0x06) # Entry Mode
        self.send_command(0x0C) # Display ON, Cursor OFF

    def write_nibble(self, data):
        # Mengirim 4-bit data tanpa latching yang rumit (khusus init)
        val = (data << 4) | self.backlight_val
        self.i2c.writeto(self.i2c_addr, bytearray([val | 0x04]))
        self.i2c.writeto(self.i2c_addr, bytearray([val]))

    def send_byte(self, data, mode):
        # Mode: 0=Command, 1=Data
        high = mode | (data & 0xF0) | self.backlight_val
        low = mode | ((data << 4) & 0xF0) | self.backlight_val
        
        # Kirim High Nibble
        self.i2c.writeto(self.i2c_addr, bytearray([high | 0x04]))
        self.i2c.writeto(self.i2c_addr, bytearray([high]))
        
        # Kirim Low Nibble
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
        # Mapping alamat memori untuk LCD 20x4
        offsets = [0x00, 0x40, 0x14, 0x54]
        if row > 3: row = 3
        addr = col + offsets[row]
        self.send_command(0x80 | addr)

    def putstr(self, string):
        for char in string:
            self.send_data(ord(char))
