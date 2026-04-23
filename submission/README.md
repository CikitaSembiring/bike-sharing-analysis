# Proyek Analisis Data: Bike Sharing Dataset

Proyek ini adalah bagian dari kurikulum Dicoding untuk menganalisis dataset Bike Sharing. Tujuan utama dari proyek ini adalah untuk mengeksplorasi tren penyewaan sepeda, pengaruh kondisi cuaca, serta perbedaan perilaku antara tipe pengguna (Casual vs Registered).

## Nama: Cikita Natasya Br Sembiring

---

## 1. Tahapan Analisis Data
Berikut adalah ringkasan dari setiap tahapan analisis yang telah dilakukan dalam proyek ini:

* **Gathering Data:** Mengumpulkan dataset `day.csv` dan `hour.csv` yang berisi data harian dan per jam penyewaan sepeda.
* **Assessing Data:** Mengidentifikasi tipe data yang tidak sesuai (kolom `dteday`), mendeteksi nilai duplikat, dan memeriksa statistik deskriptif untuk mencari anomali.
* **Cleaning Data:** Mengubah tipe data `dteday` menjadi datetime, melakukan mapping pada kolom `season`, `weathersit`, dan `yr` agar data lebih mudah diinterpretasikan (misal: 1 menjadi 'Spring', 0 menjadi 2011).
* **Exploratory Data Analysis (EDA):** Mengeksplorasi hubungan antar variabel untuk menjawab pertanyaan bisnis mengenai tren bulanan, dampak cuaca terhadap pengguna casual, dan jam sibuk pada hari kerja.
* **Explanatory Analysis:** Membuat visualisasi data menggunakan Matplotlib dan Seaborn untuk memperjelas temuan, serta melakukan analisis lanjutan (RFM Analysis) untuk melihat pertumbuhan bisnis.

## 2. Struktur Direktori
```text
submission
├───dashboard
│   ├───dashboard.py
│   └───main_data.csv
├───data
│   ├───day.csv
│   └───hour.csv
├───notebook.ipynb
├───README.md
└───requirements.txt

## 3. Instalasi Environment
Untuk menjalankan proyek ini secara lokal, silakan ikuti langkah-langkah instalasi berikut:

* **Pastikan Python Terinstal** Pastikan sistem Anda sudah memiliki Python versi 3.9 atau yang terbaru.
* **Instalasi Pustaka (Library)** Buka terminal atau command prompt, arahkan ke folder proyek, lalu jalankan perintah berikut untuk menginstal semua library yang dibutuhkan:
```bash
pip install -r requirements.txt

## 4. Cara Menjalankan Dashboard
Setelah instalasi selesai, Anda dapat menjalankan dashboard Streamlit dengan langkah-langkah berikut:

1. Masuk ke Direktori Dashboard
Arahkan terminal Anda ke dalam folder dashboard:

cd dashboard

2. Menjalankan Aplikasi Streamlit
Ketik perintah di bawah ini untuk memulai server Streamlit:
streamlit run dashboard.py

3. Akses Dashboard
Dashboard akan otomatis terbuka di browser Anda. Jika tidak, silakan buka browser dan akses alamat