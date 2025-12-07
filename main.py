import machine
import time
import random
from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd

# ================= KONFIGURASI =================
# Password: Indeks tombol [0, 2, 1, 3] 
# (Sesuai urutan kabelmu: Btn1, Btn3, Btn2, Btn4)
PASSWORD = [0, 2, 1, 3]

# LCD (SDA=GP4, SCL=GP5)
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
try:
    lcd = I2cLcd(i2c, 0x27, 4, 20)
except:
    print("LCD Error: Cek kabel SDA/SCL")

# LEDs [Merah, Hijau, Biru, Kuning]
leds = [Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT), Pin(19, Pin.OUT)]

# Buttons (GP11, GP12, GP13, GP10)
# Urutan di list ini PENTING karena menentukan indeks 0,1,2,3
btns = [Pin(11, Pin.IN, Pin.PULL_UP), Pin(12, Pin.IN, Pin.PULL_UP), 
        Pin(13, Pin.IN, Pin.PULL_UP), Pin(10, Pin.IN, Pin.PULL_UP)]

# 7-Segment [A,B,C,D,E,F,G] -> [GP0, GP1, GP6, GP7, GP8, GP9, GP14]
seg_pins = [Pin(0,Pin.OUT), Pin(1,Pin.OUT), Pin(6,Pin.OUT), Pin(7,Pin.OUT), 
            Pin(8,Pin.OUT), Pin(9,Pin.OUT), Pin(14,Pin.OUT)]

# Pola Angka (Common Cathode: 1=Nyala)
# Jika masih terbalik (malah mati saat harusnya nyala), ganti 1 jadi 0
digits = {
    0:[1,1,1,1,1,1,0], 1:[0,1,1,0,0,0,0], 2:[1,1,0,1,1,0,1], 3:[1,1,1,1,0,0,1],
    4:[0,1,1,0,0,1,1], 5:[1,0,1,1,0,1,1], 6:[1,0,1,1,1,1,1], 7:[1,1,1,0,0,0,0],
    8:[1,1,1,1,1,1,1], 9:[1,1,1,1,0,1,1],
    'E':[1,0,0,1,1,1,1], '-':[0,0,0,0,0,0,1], ' ':[0,0,0,0,0,0,0]
}

# ================= FUNGSI BANTUAN =================
def show_seg(char):
    pola = digits.get(char, digits[' '])
    for i in range(7):
        seg_pins[i].value(pola[i])

def flash_led(idx, speed=0.3):
    leds[idx].value(1)
    time.sleep(speed)
    leds[idx].value(0)
    time.sleep(0.1)

def read_btn():
    while True:
        for i, btn in enumerate(btns):
            if btn.value() == 0: # Ditekan
                flash_led(i, 0.1) # Feedback visual
                while btn.value() == 0: time.sleep(0.01) # Debounce
                return i
        time.sleep(0.01)

def simon_game():
    lcd.clear()
    lcd.move_to(5,0); lcd.putstr("SIMON GAME")
    lcd.move_to(6,1); lcd.putstr("START!")
    time.sleep(1)
    
    level = 1
    seq = []
    
    while True:
        # Tampilkan Level di 7-Seg
        show_seg(level % 10)
        
        # Tambah Soal
        seq.append(random.randint(0, 3))
        
        # Tampilkan Pola
        lcd.move_to(0,2); lcd.putstr(f"Level {level}: Watch... ")
        time.sleep(0.5)
        for s in seq:
            flash_led(s, 0.4)
            time.sleep(0.2)
            
        lcd.move_to(0,2); lcd.putstr(f"Level {level}: Repeat!  ")
        
        # Cek Jawaban User
        for ans in seq:
            user_in = read_btn()
            if user_in != ans:
                # GAMEOVER
                lcd.clear()
                lcd.move_to(5,1); lcd.putstr("GAME OVER")
                lcd.move_to(4,2); lcd.putstr(f"Score: {level}")
                show_seg('E')
                
                # Kedip Error
                for _ in range(3):
                    for l in leds: l.value(1)
                    time.sleep(0.2)
                    for l in leds: l.value(0)
                    time.sleep(0.2)
                return # Keluar game
        
        # Level Up
        lcd.move_to(0,2); lcd.putstr("CORRECT! Next...   ")
        level += 1
        time.sleep(0.5)

# ================= PROGRAM UTAMA =================
def main():
    lcd.clear()
    # Animasi Cek 7-Segment (Angka 8)
    show_seg(8) 
    time.sleep(0.5)
    show_seg('-')
    
    input_code = []
    
    while True:
        # Tampilan Awal
        if len(input_code) == 0:
            lcd.clear()
            lcd.move_to(2,1); lcd.putstr("-INPUT PASSWORD-")
            lcd.move_to(8,2); lcd.putstr("[    ]")
            show_seg('-')
            
        # Baca Tombol
        p = read_btn()
        input_code.append(p)
        
        # Tampilkan Bintang
        lcd.move_to(9 + len(input_code) - 1, 2)
        lcd.putstr("*")
        show_seg(' ') # Matikan 7-seg saat ngetik
        
        # Cek Password
        if len(input_code) == 4:
            time.sleep(0.3)
            if input_code == PASSWORD:
                # SUKSES
                lcd.clear()
                lcd.move_to(4,1); lcd.putstr("-SAFE OPEN-")
                show_seg('O') # O untuk Open (pola 0)
                # Animasi Sukses
                for _ in range(2):
                    for l in leds: l.value(1)
                    time.sleep(0.2)
                    for l in leds: l.value(0)
                    time.sleep(0.2)
                
                time.sleep(1)
                simon_game() # Masuk Game
                input_code = [] # Reset kalau game over
            else:
                # GAGAL
                lcd.clear()
                lcd.move_to(6,1); lcd.putstr("-ERROR-")
                show_seg('E')
                # Animasi Gagal
                for _ in range(3):
                    for l in leds: l.value(1)
                    time.sleep(0.1)
                    for l in leds: l.value(0)
                    time.sleep(0.1)
                
                input_code = []
                lcd.clear()

if __name__ == "__main__":
    main()
