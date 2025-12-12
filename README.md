<div align="center">

<img src="https://via.placeholder.com/150?text=SimonVault+Logo" alt="Simon Vault Logo" width="120" height="120" />

# Raspberry Pi Pico: Simon Vault

**Sistem Keamanan Biometrik Hibrida & Permainan Memori Digital**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](./LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Raspberry_Pi_Pico-red.svg?style=flat-square)](https://www.raspberrypi.com/products/raspberry-pi-pico/)
[![Language](https://img.shields.io/badge/Language-MicroPython-blue.svg?style=flat-square)](https://micropython.org/)
[![Status](https://img.shields.io/badge/Status-Active-success.svg?style=flat-square)]()

</div>

---

## 📋 Ikhtisar Proyek

**Simon Vault** adalah implementasi sistem tertanam (*embedded system*) yang mensimulasikan mekanisme pengamanan brankas digital yang terintegrasi dengan permainan memori klasik "Simon Says". Proyek ini dirancang untuk mendemonstrasikan manajemen *State Machine*, kontrol I/O kompleks, dan antarmuka pengguna berbasis perangkat keras menggunakan mikrokontroler Raspberry Pi Pico.

Sistem ini beroperasi dalam dua fase logika utama:
1.  **Secure Access Layer (Vault):** Memerlukan autentikasi PIN input fisik untuk membuka akses sistem.
2.  **Gamified Interface (Simon Game):** Setelah autentikasi berhasil, sistem beralih menjadi permainan memori dengan tingkat kesulitan progresif.

---

## ✨ Fitur Utama

### 1. Sistem Keamanan Digital (Vault Mode)
* **Autentikasi PIN:** Menggunakan kombinasi 4-tombol input untuk verifikasi akses.
* **Masking Visual:** Input pengguna disamarkan pada 7-Segment Display untuk keamanan visual.
* **Feedback Real-time:** Status sistem (Locked/Unlocked) ditampilkan melalui LCD I2C 20x4.

### 2. Permainan Memori (Simon Says Mode)
* **Pola Acak Dinamis:** Algoritma menghasilkan urutan pola LED dan nada yang unik setiap sesi permainan.
* **Kesulitan Progresif:** Kecepatan dan panjang urutan meningkat seiring bertambahnya level pengguna.
* **Sistem Poin:** Skor level ditampilkan secara *real-time* pada 7-Segment Display.
* **Audio Feedback:** Nada frekuensi unik untuk setiap tombol dan indikator status (Sukses/Gagal) menggunakan PWM Buzzer.

---

## ⚙️ Arsitektur Teknis

Proyek ini dibangun di atas ekosistem MicroPython dengan spesifikasi berikut:

* **Mikrokontroler:** Raspberry Pi Pico (RP2040)
* **Protokol Komunikasi:** I2C (untuk LCD), GPIO Digital, PWM (Pulse Width Modulation).
* **Library Eksternal:** `pico_i2c_lcd` untuk manajemen display LCD.
* **Modularitas Kode:** Pemisahan logika utama (`main.py`) dan driver periferal (`buzzer_lib.py`, `pico_i2c_lcd.py`) untuk kemudahan pemeliharaan.

---

## 🔌 Diagram Pengkabelan (Wiring)

Konfigurasi pin berikut wajib diikuti untuk memastikan kompatibilitas dengan kode sumber (`main.py` & `buzzer_lib.py`).

| Periferal | Label Pin | Pin Pico (GPIO) | Fungsi |
| :--- | :--- | :--- | :--- |
| **I2C LCD** | SDA | `GP4` | Jalur Data Display |
| | SCL | `GP5` | Jalur Clock Display |
| **Input** | Button 1 | `GP11` | Input Digit 1 |
| | Button 2 | `GP12` | Input Digit 2 |
| | Button 3 | `GP13` | Input Digit 3 |
| | Button 4 | `GP10` | Input Digit 4 |
| **Output LED** | LED Merah | `GP16` | Indikator Visual 1 |
| | LED Hijau | `GP17` | Indikator Visual 2 |
| | LED Biru | `GP18` | Indikator Visual 3 |
| | LED Kuning | `GP19` | Indikator Visual 4 |
| **7-Segment** | Segmen A-G | `GP0, 1, 6-9, 14` | Tampilan Skor/Input |
| **Audio** | Buzzer | `GP20` | Output Suara (PWM) |

> **Catatan:** Semua tombol menggunakan konfigurasi `PULL_UP` internal.

---

## 🚀 Panduan Instalasi & Penggunaan

### Prasyarat
* Raspberry Pi Pico dengan firmware MicroPython terbaru.
* Python IDE (Thonny IDE atau VS Code).

### Langkah Instalasi
1.  **Clone Repositori:**
    ```bash
    git clone [https://github.com/liwiryaym/raspberry-pi-pico-simon-vault.git](https://github.com/liwiryaym/raspberry-pi-pico-simon-vault.git)
    ```
2.  **Unggah File:**
    Unggah file berikut ke direktori *root* Raspberry Pi Pico Anda:
    * `main.py`
    * `buzzer_lib.py`
    * `pico_i2c_lcd.py`

3.  **Jalankan Program:**
    Buka `main.py` di IDE Anda dan jalankan (Run).

### Cara Menggunakan

**1. Membuka Kunci (Unlock)**
Saat sistem menyala, LCD akan menampilkan status terkunci. Masukkan PIN default berikut secara berurutan:
`Tombol 1` ➔ `Tombol 3` ➔ `Tombol 2` ➔ `Tombol 4`
*(Representasi indeks kode: `[0, 2, 1, 3]`)*.

**2. Gameplay**
Setelah terbuka, ikuti pola lampu LED dan suara yang muncul. Tekan tombol yang sesuai dengan urutan tersebut.
* **Benar:** Level naik, pola bertambah panjang.
* **Salah:** Buzzer berbunyi nada error, sistem menampilkan skor akhir.

---

## 📂 Struktur Direktori

```text
raspberry-pi-pico-simon-vault/
├── buzzer_lib.py       # Driver kontrol PWM Buzzer dan nada
├── main.py             # Logika utama (Game Loop & State Machine)
├── pico_i2c_lcd.py     # Driver I2C untuk LCD 1602/2004
├── diagram.json        # Skema sirkuit untuk simulasi Wokwi
├── LICENSE             # Dokumen Lisensi MIT
└── README.md           # Dokumentasi Proyek
````

-----

## 🤝 Kontribusi

Kontribusi untuk pengembangan fitur atau perbaikan *bug* sangat diterima. Silakan ikuti langkah berikut:

1.  Fork repositori ini.
2.  Buat branch fitur baru (`git checkout -b fitur-baru`).
3.  Commit perubahan Anda (`git commit -m 'Menambahkan fitur X'`).
4.  Push ke branch (`git push origin fitur-baru`).
5.  Buat Pull Request.

-----

## ⚖️ Lisensi

Proyek ini dilisensikan di bawah **MIT License**. Hak cipta sepenuhnya milik **CherryYume夢 (2025)**. Anda bebas menggunakan, memodifikasi, dan mendistribusikan ulang kode sumber ini sesuai ketentuan lisensi.

Lihat file [LICENSE](https://www.google.com/search?q=./LICENSE) untuk detail lengkap.
