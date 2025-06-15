# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institute adalah lembaga pendidikan tinggi yang menghadapi tantangan dalam mempertahankan mahasiswa hingga lulus. Analisis ini bertujuan untuk mengidentifikasi faktor-faktor yang memengaruhi keberhasilan akademik mahasiswa dan memberikan rekomendasi untuk meningkatkan tingkat retensi dan kelulusan mahasiswa.

### Permasalahan Bisnis
Berdasarkan analisis data, ditemukan bahwa **32.12% mahasiswa dropout** dari Jaya Jaya Institute. Tingginya tingkat dropout ini paling banyak terjadi pada program studi ..., ..., dan .... Tujuan utama dari proyek ini adalah memahami penyebab dropout dan mengembangkan strategi prediktif dan preventif berbasis data.

### Cakupan Proyek
Proyek ini mencakup:

1. Analisis menyeluruh data demografis, akademik, dan keuangan mahasiswa untuk mengidentifikasi faktor-faktor utama yang mempengaruhi dropout mahasiswa
2. Pengembangan model prediktif untuk mengidentifikasi mahasiswa berisiko dropout
3. Pengembangan aplikasi Streamlit untuk Direktorat Kemahasiswaan melakukan prediksi dropout.
4. Implementasi dashboard untuk monitoring performa mahasiswa
5. Penyusunan rekomendasi berbasis data untuk meningkatkan retensi mahasiswa

### Persiapan

* **Sumber data:** Dataset ini berisi informasi mengenai 4424 mahasiswa dengan 37 variabel yang mencakup berbagai aspek latar belakang mahasiswa, performa akademik, dan status pendidikan. Dataset (students performance)[https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv] berasal dari Dicoding.

* **Penjelasan fitur:** Lihat (dokumentasi fitur)[https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance].

* Setup environment:
```
# Membuat environment baru dan mengaktifkannya
conda create --name main-ds python=3.9
conda activate main-ds

# Instalasi dependencies
pip install -r requirements.txt
```

## Business Dashboard
Dashboard interaktif dibuat menggunakan Supabase sebagai backend dan berisi visualisasi data performa mahasiswa. Dashboard ini memungkinkan stakeholder untuk:

1. Memantau tingkat dropout per program studi
2. Menganalisis hubungan antara faktor demografis, ekonomi dan keberhasilan akademik
3. Mengidentifikasi tren pembayaran biaya kuliah dan dampaknya terhadap status mahasiswa
4. Melihat performa semester pertama sebagai indikator keberhasilan di masa mendatang

Akses dashboard: https://student-performance-dashboard.example.com

## Menjalankan Sistem Machine Learning
Sistem prediksi dropout mahasiswa yang telah dibuat menggunakan model Random Forest Classifier dengan akurasi 85,98% dan diimplementasikan dalam bentuk sistem website interaktif dengan Streamlit. Sistem ini memungkinkan pengguna untuk memasukkan data mahasiswa dan mendapatkan prediksi risiko dropout secara langsung.

### Persiapan Lingkungan

#### Metode Cepat (Recommended)
Kami telah menyediakan script untuk setup environment secara otomatis:
```bash
# Jalankan script setup
python setup_environment.py

# Ikuti instruksi yang muncul untuk mengaktifkan environment
```

#### Setup Manual
Jika Anda mengalami masalah dengan setup otomatis, Anda dapat mengikuti langkah-langkah manual:

1. **Menggunakan Conda (Disarankan)**
   ```bash
   # Buat environment baru dengan Python 3.8
   conda create -n student-predictor python=3.8 -y
   conda activate student-predictor
   
   # Install package inti dengan versi spesifik untuk menghindari konflik
   conda install numpy=1.20.3 pandas=1.3.4 scikit-learn=1.0.2 -y
   conda install -c conda-forge streamlit=1.11.0 -y
   conda install matplotlib=3.5.1 seaborn=0.11.2 -y
   conda install -c conda-forge joblib=1.1.0 plotly=5.8.0 -y
   ```

2. **Menggunakan Pip**
   ```bash
   # Buat virtual environment
   python -m venv venv
   
   # Aktifkan environment
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   
   # Install dependensi
   pip install -r requirements.txt
   ```

### Penyelesaian Masalah Umum

Jika Anda mengalami error seperti `ImportError: DLL load failed while importing _multiarray_umath`, coba:

1. Uninstall dan install ulang NumPy dengan versi yang kompatibel:
   ```bash
   pip uninstall numpy -y
   pip install numpy==1.20.3
   ```

2. Pastikan Microsoft Visual C++ Redistributable terinstal di sistem Anda (untuk Windows)

3. Jika menggunakan conda, coba install ulang dengan conda:
   ```bash
   conda remove numpy -y
   conda install numpy=1.20.3 -y
   ```

Untuk panduan lengkap penyelesaian masalah, lihat `README_SETUP.md`.

### Langkah-langkah Menjalankan Aplikasi
1. **Clone Repository**
   ```bash
   git clone https://github.com/username/student-performance-prediction.git
   cd student-performance
   ```

2. **Jalankan Aplikasi Streamlit**
   ```bash
   streamlit run app.py
   ```
   
   Aplikasi akan berjalan secara lokal dan akan otomatis terbuka di browser pada alamat `http://localhost:8501`.

Aplikasi juga dapat diakses secara global di ...

### Cara Menggunakan Sistem Machine Learning
1. **Masukkan Informasi Mahasiswa**
   - Isi formulir dengan data demografis mahasiswa (usia, jenis kelamin, status pernikahan, dll.)
   - Masukkan informasi akademik seperti nilai kualifikasi sebelumnya dan program studi
   - Tambahkan data keuangan (status beasiswa, status pembayaran biaya kuliah)
   - Masukkan performa akademik semester pertama dan kedua

2. **Dapatkan Prediksi**
   - Klik tombol "Predict Dropout Risk" untuk mendapatkan hasil prediksi
   - Dashboard akan menampilkan probabilitas dropout mahasiswa
   - Kategori risiko akan ditampilkan (Rendah/Sedang/Tinggi)
   - Faktor-faktor utama yang mempengaruhi prediksi juga akan ditunjukkan
   - Rekomendasi tindakan sesuai dengan tingkat risiko akan diberikan

3. **Interpretasi Hasil**
   - Risiko Rendah (<30%): Mahasiswa menunjukkan progres akademik yang baik
   - Risiko Sedang (30-70%): Perlu tindakan pencegahan, seperti konseling akademik
   - Risiko Tinggi (>70%): Membutuhkan intervensi segera, termasuk dukungan akademik dan finansial

Dashboard ini memungkinkan staf akademik untuk mengidentifikasi mahasiswa yang berisiko dropout sejak dini, sehingga tindakan pencegahan yang tepat dapat diambil untuk meningkatkan retensi mahasiswa.

## Conclusion
Dari analisis data mahasiswa dan pengembangan model prediktif, kami mengidentifikasi beberapa faktor kunci yang mempengaruhi risiko dropout:

1. Performa akademik di semester kedua merupakan prediktor terkuat, diikuti oleh performa di semester pertama
2. Status pembayaran biaya kuliah memiliki pengaruh signifikan (87% mahasiswa yang menunggak akan dropout)
3. Program studi tertentu memiliki tingkat dropout yang jauh lebih tinggi (Biofuel Production Technologies: 66.67%)
4. Usia pendaftaran berkorelasi dengan tingkat kelulusan (mahasiswa yang lebih tua berisiko lebih tinggi)
5. Status pernikahan berpengaruh terhadap kemungkinan dropout (terutama mahasiswa dengan status Legally Separated)

### Rekomendasi Action Items
Berdasarkan temuan analisis, berikut rekomendasi untuk menurunkan tingkat dropout mahasiswa:
- Implementasikan sistem peringatan dini yang memprioritaskan performa semester kedua sebagai indikator kritis
- Kembangkan program bantuan keuangan dan konseling khusus bagi mahasiswa dengan tunggakan biaya kuliah
- Tingkatkan dukungan akademik untuk program studi dengan tingkat dropout tertinggi
- Desain program dukungan khusus untuk mahasiswa yang mendaftar di usia lebih tua
- Sediakan konseling dan dukungan tambahan untuk mahasiswa dengan situasi pernikahan yang berpotensi mempengaruhi studi
- Evaluasi struktur kurikulum semester kedua yang tampaknya menjadi titik kritis dalam perjalanan akademik mahasiswa
