# Raspberry Pi Pico: Simon Vault

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Wokwi](https://img.shields.io/badge/Platform-Wokwi-blue)](https://pornhub.com)
[![Language: MicroPython](https://img.shields.io/badge/Language-MicroPython-orange)](https://micropython.org/)

**Simon Vault** adalah proyek simulasi *embedded system* ganda yang menggabungkan sistem keamanan digital (keypad lock) dengan permainan memori klasik "Simon Says". Proyek ini mendemonstrasikan logika *state machine*, penanganan input/output kompleks, dan penggunaan modul display (LCD & 7-Segment) menggunakan MicroPython.

---

## 📋 Daftar Isi
1. [Gambaran Proyek](#-gambaran-proyek)
2. [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
3. [Konfigurasi Pin (Wiring)](#-konfigurasi-pin-wiring)
4. [Prasyarat & Instalasi](#-prasyarat--instalasi)
5. [Panduan Penggunaan](#-panduan-penggunaan)
6. [Struktur File](#-struktur-file)
7. [Lisensi](#-lisensi)

---

## 🔭 Gambaran Proyek

Sistem ini memiliki dua mode operasi utama:

1.  **Vault Mode (Mode Keamanan):**
    Saat dinyalakan, sistem berada dalam keadaan terkunci. Pengguna harus memasukkan kombinasi 4 digit PIN yang benar melalui tombol fisik untuk membuka akses.

2.  **Game Mode (Simon Says):**
    Setelah autentikasi berhasil, sistem beralih ke mode permainan. Mikroprosesor akan menghasilkan urutan pola lampu LED yang harus diulangi oleh pengguna. Kesulitan (level) akan meningkat setiap kali pengguna berhasil meniru pola dengan benar.

**Fitur Utama:**
* Autentikasi PIN 4-digit.
* Tampilan status *real-time* pada LCD 20x4 (I2C).
* Indikator skor dan input tersembunyi menggunakan 7-Segment Display.
* Algoritma permainan memori dengan peningkatan level tanpa batas.
* Animasi visual untuk status *Success*, *Error*, dan *Game Over*.

---

## 🛠 Teknologi yang Digunakan

<p align="left">
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Raspberrry_pi_logo.png" width="40" alt="Raspberry Pi" style="margin-right: 15px;"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="40" alt="MicroPython" style="margin-right: 15px;"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/cb/Wokwi.png" width="40" alt="Wokwi"/>
</p>

* **Hardware:** Raspberry Pi Pico W
* **Bahasa Pemrograman:** MicroPython
* **Platform Simulasi:** Wokwi
* **Library:** `pico_i2c_lcd` (Driver untuk LCD I2C)

---

## 🔌 Konfigurasi Pin (Wiring)

Berikut adalah pemetaan pin GPIO yang digunakan dalam kode `main.py`. Pastikan rangkaian Anda sesuai dengan tabel ini:

| Komponen | Pin Device | Raspberry Pi Pico (GP) | Keterangan |
| :--- | :--- | :--- | :--- |
| **I2C LCD** | SDA | `GP4` | Display Instruksi |
| | SCL | `GP5` | |
| **Tombol (Input)** | Btn 1 | `GP11` | Pull-up Internal |
| | Btn 2 | `GP12` | Pull-up Internal |
| | Btn 3 | `GP13` | Pull-up Internal |
| | Btn 4 | `GP10` | Pull-up Internal |
| **LED (Output)** | Merah | `GP16` | Indikator Game |
| | Hijau | `GP17` | |
| | Biru | `GP18` | |
| | Kuning | `GP19` | |
| **7-Segment** | A, B | `GP0`, `GP1` | Skor & Input Mask |
| | C, D, E | `GP6`, `GP7`, `GP8` | |
| | F, G | `GP9`, `GP14` | |

---

## 📥 Prasyarat & Instalasi

### Opsi 1: Simulasi Online (Disarankan)
Anda dapat langsung menjalankan proyek ini tanpa instalasi software apapun melalui browser:
👉 **[Buka Simulasi di Wokwi](https://wokwi.com/projects/449697556937651201)**

### Opsi 2: Menjalankan di Hardware Fisik

1.  **Siapkan Lingkungan Kerja:**
    * Install [Thonny IDE](https://thonny.org/).
    * Flash firmware MicroPython terbaru ke Raspberry Pi Pico Anda.

2.  **Clone Repository:**
    ```bash
    git clone https://github.com/liwiryaym/raspberry-pi-pico-simon-vault.git
    ```

3.  **Upload File ke Pico:**
    Buka Thonny IDE, lalu upload file berikut ke root direktori Pico:
    * `pico_i2c_lcd.py` (Library wajib)
    * `main.py` (Program utama)

4.  **Jalankan:**
    Buka `main.py` dan klik tombol **Run**.

---

## 📖 Panduan Penggunaan

### Tahap 1: Membuka Brankas (Unlock)
Saat program dimulai, layar menampilkan `-INPUT PASSWORD-`. Masukkan kode default berikut (sesuai urutan wiring tombol):

> **Kombinasi:** Tombol 1 ➔ Tombol 3 ➔ Tombol 2 ➔ Tombol 4

* *Catatan Teknis:* Password didefinisikan dalam variabel `PASSWORD = [0, 2, 1, 3]` pada `main.py`, yang mereferensikan indeks pada list `btns`.

### Tahap 2: Bermain Simon Says
Jika password benar, LCD akan menampilkan "AKSES TERBUKA" dan permainan dimulai.
1.  **Perhatikan (Watch):** LED akan menyala dengan urutan tertentu.
2.  **Ulangi (Repeat):** Tekan tombol yang sesuai dengan warna LED tersebut.
3.  **Skor:** Level Anda saat ini ditampilkan pada layar 7-Segment.
4.  **Game Over:** Jika salah menekan, permainan berakhir dan skor ditampilkan.

---

## 📂 Struktur File

```text
.
├── diagram.json        # Skema rangkaian untuk simulator Wokwi
├── main.py             # Logika utama (Boot, Vault System, Game Loop)
├── pico_i2c_lcd.py     # Library driver untuk I2C LCD
└── README.md           # Dokumentasi proyek
````

-----

## 📄 Lisensi

Proyek ini didistribusikan di bawah lisensi **MIT**. Anda bebas menggunakan, memodifikasi, dan mendistribusikan ulang kode ini.
Lihat file [LICENSE](https://www.google.com/search?q=./LICENSE) untuk detail lengkap.

```text
Copyright (c) 2025 LiwiryaYM夢
```
