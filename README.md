# 🔒 Raspberry Pi Pico Simon Vault

<p align="center">
  <img src="https://dummyimage.com/800x300/2c3e50/ffffff&text=Wokwi+Simulation+Screenshot+Placeholder" alt="Project Banner" width="100%" />
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square" alt="Status">
    <img src="https://img.shields.io/badge/Language-MicroPython-blue?style=flat-square&logo=python" alt="Language">
    <img src="https://img.shields.io/badge/Platform-Wokwi-orange?style=flat-square" alt="Platform">
    <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License">
</p>

<p align="center">
  <strong>Sistem Keamanan & Game Memori Interaktif Berbasis IoT</strong>
</p>
<p align="center">
  <a href="https://wokwi.com/projects/449697556937651201">
    <img src="https://avatars.githubusercontent.com/u/65966273?s=40&v=4" width="30" height="30" align="center" />
    <b>Coba Simulasi Langsung di Wokwi</b>
  </a>
</p>

---

## 📖 Tentang Proyek

**Raspberry Pi Pico Simon Vault** adalah proyek simulasi interaktif yang menggabungkan konsep sistem keamanan digital dengan permainan memori elektronik klasik "Simon Says".

Proyek ini didesain sebagai demonstrasi penggunaan mikrokontroler untuk menangani multiple input (tombol), multiple output visual (LED & berbagai jenis layar), serta logika pemrograman state-machine menggunakan **MicroPython**.

---

## 🌟 Fitur Utama

Project ini memiliki dua mode operasi utama yang saling terhubung:

### 1. 🛡️ Security Vault Mode (Mode Brankas)
Mode default saat perangkat dinyalakan. Sistem terkunci dan meminta otentikasi.
* **Input PIN:** Membutuhkan kombinasi 4-tombol yang tepat untuk membuka.
* **Indikator Status:** Menggunakan LCD 20x4 untuk instruksi teks dan 7-Segment Display untuk menampilkan digit tersembunyi (*).
* **Feedback Visual:** LED berkedip sebagai respon saat tombol ditekan.

### 2. 🎮 Simon Says Game Mode
Mode permainan yang aktif otomatis setelah brankas berhasil dibuka.
* **Tantangan Memori:** Sistem menghasilkan urutan nyala LED acak.
* **Level Progresif:** Tingkat kesulitan (panjang urutan) meningkat setiap kali pemain berhasil meniru pola.
* **Real-time Scoring:** Skor (Level saat ini) ditampilkan langsung pada 7-Segment Display.
* **Visual Effects:** Animasi khusus untuk "Correct Answer" dan "Game Over".

---

## 🛠️ Teknologi & Komponen

Proyek ini dibangun menggunakan ekosistem teknologi berikut:

| Teknologi / Komponen | Ikon | Deskripsi & Pinout (GP) |
| :--- | :---: | :--- |
| **Raspberry Pi Pico W** | <img src="https://www.raspberrypi.com/app/uploads/2022/02/COLOUR-Raspberry-Pi-Symbol-Registered.png" width="35"/> | Mikrokontroler utama sebagai otak sistem. |
| **MicroPython** | <img src="https://micropython.org/static/img/M-dark-128.png" width="35"/> | Bahasa pemrograman yang digunakan untuk logika kontrol. |
| **Wokwi Simulator** | <img src="https://avatars.githubusercontent.com/u/65966273?s=40&v=4" width="35"/> | Platform simulasi perangkat keras secara online. |
| **I2C LCD 20x4** | 📟 | Menampilkan status dan instruksi game. <br> `SDA: GP4`, `SCL: GP5` |
| **7-Segment Display** | 🔢 | Menampilkan input password & skor level. <br> `GP0, 1, 6, 7, 8, 9, 14` |
| **LEDs (Merah, Hijau, Biru, Kuning)** | 💡 | Output visual utama untuk game Simon Says. <br> `GP16, GP17, GP18, GP19` |
| **Pushbuttons (x4)** | 🔘 | Input user untuk password dan kontrol game. <br> `GP10, GP11, GP12, GP13` |

---

## 📂 Susunan Project

Struktur file dalam repositori ini diatur untuk kemudahan penggunaan di Wokwi maupun hardware fisik:

```text
📦 raspberry-pi-pico-simon-vault
 ┣ 📜 main.py           # 🧠 Logika utama program (Vault & Game Loop)
 ┣ 📜 pico_i2c_lcd.py   # 🔌 Driver library untuk mengontrol LCD via I2C
 ┣ 📜 diagram.json      # 🗺️ Konfigurasi wiring visual untuk simulasi Wokwi
 ┣ 📜 wokwi-project.txt # ⚙️ Metadata project Wokwi
 ┣ 📜 LICENSE           # ⚖️ Lisensi MIT
 ┗ 📜 README.md         # 📘 Dokumentasi project ini
````

-----

## 🚀 Panduan Instalasi & Penggunaan

### Prasyarat

  * **Simulator:** Akun [Wokwi](https://wokwi.com) (Gratis).
  * **Hardware Fisik (Opsional):** Raspberry Pi Pico, Kabel data, Thonny IDE, dan komponen elektronik sesuai tabel di atas.

### Cara Menjalankan (Simulasi)

1.  Buka tautan proyek Wokwi di bagian atas halaman ini.
2.  Klik tombol **Play** (▶️) berwarna hijau di simulator Wokwi.
3.  Sistem akan mulai booting.

### Cara Bermain

#### Tahap 1: Membuka Brankas

Layar akan menampilkan `-INPUT PASSWORD-`. Masukkan kode default berikut menggunakan tombol yang tersedia:

> **Password:** Tombol 1 → Tombol 3 → Tombol 2 → Tombol 4
> (Urutan Pin: GP11 → GP13 → GP12 → GP10)

  * ✅ **Sukses:** Layar LCD menampilkan "SAFE OPEN", 7-Segment menampilkan 'O', dan game dimulai.
  * ❌ **Gagal:** Layar LCD menampilkan "ERROR", 7-Segment menampilkan 'E', silakan coba lagi.

#### Tahap 2: Simon Says

Setelah terbuka, ikuti instruksi di LCD:

1.  **Watch:** Perhatikan urutan LED yang menyala.
2.  **Repeat:** Tekan tombol berwarna yang sesuai dengan urutan tadi.
3.  Bertahanlah selama mungkin untuk mencapai level tertinggi\!

-----

## 🤝 Kontribusi

Kontribusi adalah apa yang membuat komunitas open source menjadi tempat yang luar biasa untuk belajar, menginspirasi, dan berkreasi. Setiap kontribusi yang Anda buat **sangat dihargai**.

1.  Fork Project ini.
2.  Buat Branch Fitur baru (`git checkout -b feature/FiturKeren`).
3.  Commit Perubahan Anda (`git commit -m 'Menambahkan FiturKeren'`).
4.  Push ke Branch (`git push origin feature/FiturKeren`).
5.  Buka Pull Request.

-----

## 📄 Lisensi

Didistribusikan di bawah Lisensi MIT. Lihat `LICENSE` untuk informasi lebih lanjut.

```text
MIT License

Copyright (c) 2025 CherryYume夢

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

-----

\<p align="center"\>
Dibuat dengan ❤️ menggunakan \<a href="https://micropython.org/"\>MicroPython\</a\> dan \<a href="https://wokwi.com/"\>Wokwi\</a\>.
\</p\>
