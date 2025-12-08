# 🔒 Raspberry Pi Pico Simon Vault

![Project Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Language](https://img.shields.io/badge/Language-MicroPython-blue)
![Platform](https://img.shields.io/badge/Platform-Wokwi-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Raspberry Pi Pico Simon Vault** adalah proyek simulasi interaktif yang menggabungkan sistem keamanan berbasis kata sandi dengan permainan memori klasik "Simon Says". Proyek ini dibangun menggunakan **MicroPython** dan disimulasikan sepenuhnya di platform **Wokwi**.

🔗 **Coba Simulasi Langsung:** [Klik di sini untuk membuka Project di Wokwi](https://wokwi.com/projects/449697556937651201)

---

## 🌟 Fitur Utama

Project ini memiliki dua mode operasi utama:

1.  **🛡️ Security Vault Mode (Mode Brankas)**
    * Sistem terkunci saat pertama kali dinyalakan.
    * Membutuhkan input 4-digit PIN melalui tombol fisik.
    * Indikator status menggunakan LCD 20x4 dan 7-Segment Display.
    * Umpan balik visual LED saat tombol ditekan.

2.  **🎮 Simon Says Game Mode**
    * Terbuka otomatis setelah password benar.
    * Permainan memori visual: Ikuti urutan nyala LED yang dihasilkan sistem.
    * Tingkat kesulitan (Level) meningkat tanpa batas setiap kali Anda berhasil.
    * Sistem skor ditampilkan secara *real-time* pada 7-Segment.
    * Animasi *Game Over* jika salah menekan urutan.

---

## 🛠️ Teknologi & Komponen

Proyek ini menggunakan komponen berikut yang dikendalikan oleh **Raspberry Pi Pico W**:

| Komponen | Pin (GP) | Deskripsi |
| :--- | :--- | :--- |
| **Microcontroller** | - | Raspberry Pi Pico (MicroPython) |
| **I2C LCD 20x4** | SDA: `GP4`, SCL: `GP5` | Menampilkan instruksi dan status game |
| **7-Segment Display** | `GP0, 1, 6-9, 14` | Menampilkan input password (bintang) & Level game |
| **LEDs (4 Warna)** | `GP16 - GP19` | Output visual untuk game Simon Says |
| **Pushbuttons (x4)** | `GP10 - GP13` | Input untuk password dan kontrol game |

---

## 📂 Susunan Project

Struktur file dalam repositori ini adalah sebagai berikut:

```text
📦 raspberry-pi-pico-simon-vault
 ┣ 📜 main.py           # Logika utama program (Vault & Game Loop)
 ┣ 📜 pico_i2c_lcd.py   # Driver library untuk mengontrol LCD via I2C
 ┣ 📜 diagram.json      # Konfigurasi wiring untuk simulasi Wokwi
 ┣ 📜 wokwi-project.txt # Metadata project Wokwi
 ┣ 📜 LICENSE           # Lisensi MIT
 ┗ 📜 README.md         # Dokumentasi project
````

-----

## 🚀 Prasyarat & Instalasi

Jika Anda ingin menjalankan proyek ini secara lokal (di hardware asli) atau mengeditnya:

1.  **Hardware (Jika fisik):**

      * Raspberry Pi Pico.
      * Kabel Jumper & Breadboard.
      * Modul LCD 1602/2004 dengan I2C Backpack.
      * 4x LED & Resistor (220Ω).
      * 4x Pushbutton.
      * 1x 7-Segment Display (Common Cathode).

2.  **Software:**

      * Install [Thonny IDE](https://thonny.org/) atau VS Code (dengan ekstensi Pico-W-Go).
      * Flash firmware MicroPython terbaru ke dalam Pico.

3.  **Langkah Instalasi:**

      * Clone repositori ini:
        ```bash
        git clone [https://github.com/liwiryaym/raspberry-pi-pico-simon-vault-.git](https://github.com/liwiryaym/raspberry-pi-pico-simon-vault-.git)
        ```
      * Upload `pico_i2c_lcd.py` ke root direktori Pico.
      * Buka `main.py` dan jalankan (Run).

-----

## 🕹️ Cara Penggunaan

### 1\. Membuka Brankas (Vault)

Saat simulasi dimulai, layar akan menampilkan `-INPUT PASSWORD-`.

  * Default Password (berdasarkan urutan kabel di `main.py`):
      * Tombol 1 (GP11)
      * Tombol 3 (GP13)
      * Tombol 2 (GP12)
      * Tombol 4 (GP10)
  * **Urutan Kode:** `0 - 2 - 1 - 3` (Lihat variabel `PASSWORD` di kode).
  * Jika Benar: Layar LCD menampilkan "SAFE OPEN" dan 7-Segment menampilkan 'O'.
  * Jika Salah: Layar LCD menampilkan "ERROR" dan 7-Segment menampilkan 'E'.

### 2\. Bermain Simon Says

Setelah brankas terbuka, game dimulai:

  * **Watch:** Perhatikan urutan LED yang menyala.
  * **Repeat:** Tekan tombol yang sesuai dengan warna LED tersebut.
  * Jika benar, level naik dan urutan menjadi lebih panjang.
  * Lihat skor Anda pada layar 7-Segment.

-----

## 🤝 Kontribusi

Kontribusi selalu diterima\! Jika Anda ingin meningkatkan fitur (misalnya menambahkan suara buzzer atau penyimpanan skor tertinggi):

1.  Fork repositori ini.
2.  Buat branch fitur baru (`git checkout -b fitur-keren`).
3.  Commit perubahan Anda (`git commit -m 'Menambahkan fitur buzzer'`).
4.  Push ke branch (`git push origin fitur-keren`).
5.  Buat Pull Request.

-----

*Dibuat Oleh Liwirya sambil ☕.*
