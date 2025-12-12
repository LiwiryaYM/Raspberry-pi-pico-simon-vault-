# Buzzer Implementasi
**Credit by: Liwirya**

Dokumentasi ini menjelaskan cara kerja dan implementasi fitur **Audio Feedback (Buzzer)** yang telah ditambahkan ke dalam sistem keamanan brankas (Safe Lock) yang terintegrasi dengan permainan memori (Simon Game).

---

## 🛠️ 1. Hardware: Modul Audio (Buzzer)

Fitur suara menggunakan komponen **Piezo Buzzer**. Buzzer ini memberikan respon suara (feedback) kepada pengguna agar interaksi terasa lebih nyata.

### Skema Kabel (Wiring)
Pastikan pemasangan kabel sesuai tabel di bawah ini agar buzzer tidak rusak:

| Kaki Komponen | Pin Raspberry Pi Pico | Keterangan |
| :--- | :--- | :--- |
| **Pin 1 (Hitam / Negatif)** | **GND** (Pin 3, 8, atau 13) | Ground (Arus Balik) |
| **Pin 2 (Merah / Positif)** | **GP20** (Pin 26) | Sinyal Data (PWM) |

> **Catatan Penting:** Pada simulasi Wokwi, pastikan atribut volume buzzer diatur ke `0.1` atau `1.0` agar suara terdengar.

---

## 💻 2. Implementasi Kode (Python)

Sistem audio menggunakan teknik **PWM (Pulse Width Modulation)** untuk menghasilkan frekuensi nada yang berbeda.

### A. Konfigurasi Awal
Tambahkan library `PWM` dan inisialisasi pin di bagian atas kode `main.py`:

```python
from machine import Pin, PWM
import time

# Inisialisasi Buzzer pada GP20
buzzer = PWM(Pin(20))
buzzer.duty_u16(0) # Pastikan buzzer mati (silence) saat awal menyala

B. Rumus Nada (Frequency Dictionary)
Kita menggunakan frekuensi standar tangga nada (C4 Major Scale) agar suara terdengar harmonis:
| Tombol / Warna | Nada Musik | Frekuensi (Getaran/Detik) |
|---|---|---|
| Tombol 1 (Merah) | Do (C4) | 262 Hz |
| Tombol 2 (Hijau) | Re (D4) | 294 Hz |
| Tombol 3 (Biru) | Mi (E4) | 330 Hz |
| Tombol 4 (Kuning) | Fa (F4) | 349 Hz |
Dalam kode Python, ini ditulis sebagai List:
TONES = [262, 294, 330, 349]

C. Fungsi Pemutar Suara
Fungsi ini dibuat untuk mempermudah pemanggilan suara di logika utama:
def play_tone(freq, duration):
    """
    freq     : Angka getaran per detik (Hz)
    duration : Lama bunyi dalam detik (seconds)
    """
    buzzer.freq(freq)          # Set kecepatan getar
    buzzer.duty_u16(32768)     # Set Volume (50% Power)
    time.sleep(duration)       # Tahan bunyi
    buzzer.duty_u16(0)         # Matikan suara
    time.sleep(0.05)           # Beri jeda sedikit

⚙️ 3. Integrasi Logika (Logic Flow)
Audio diintegrasikan ke dalam logika permainan yang dibuat oleh Liwirya dengan skenario berikut:
 * Input Feedback: Setiap kali tombol ditekan, buzzer berbunyi pendek (0.1 detik) sesuai nada tombol tersebut. Ini memberi kepastian pada pengguna bahwa tombol berhasil ditekan.
 * Simon Game (Memori):
   Saat komputer menampilkan pola lampu, buzzer juga membunyikan nada yang sesuai dengan warna lampu. Ini membantu pemain mengingat pola menggunakan Visual (Lampu) dan Audio (Suara).
 * Status Akses:
   * Access Granted (Sukses): Memainkan melodi naik (Nada C -> E -> G) untuk memberikan kesan positif.
   * Access Denied (Gagal): Memainkan nada rendah dan panjang untuk memberikan kesan peringatan/error.
> Credits:
> Core Logic, Game Design, & Wiring Diagram © 2024 Liwirya.
> Dokumentasi ini dibuat untuk tujuan edukasi dan presentasi tugas sekolah.
