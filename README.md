# 🎓 Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institute

## 🧠 Business Understanding
Jaya Jaya Institute adalah lembaga pendidikan tinggi yang menghadapi tantangan dalam mempertahankan mahasiswa hingga lulus. Analisis ini bertujuan untuk mengidentifikasi faktor-faktor yang memengaruhi keberhasilan akademik mahasiswa dan memberikan rekomendasi untuk meningkatkan tingkat retensi dan kelulusan mahasiswa.

### ❓ Permasalahan Bisnis
Berdasarkan analisis data, ditemukan bahwa **32.12% mahasiswa dropout** dari Jaya Jaya Institute. Tingginya tingkat dropout ini paling banyak terjadi pada program studi *Biofuel Production Technologies*, *Equinculture*, dan *Informatics Engineering*. Tujuan utama dari proyek ini adalah mengidentifikasi faktor risiko dropout mahasiswa untuk intervensi dini dan menyediakan informasi visual bagi pihak manajemen akademik untuk pengambilan keputusan berbasis data.

### 🧪 Cakupan Proyek
Proyek ini mencakup:
1. Analisis menyeluruh data demografis, akademik, dan keuangan mahasiswa untuk mengidentifikasi faktor-faktor utama yang mempengaruhi dropout mahasiswa.
2. Pengembangan model prediktif untuk mengidentifikasi mahasiswa berisiko dropout
3. Pengembangan aplikasi Streamlit untuk Direktorat Kemahasiswaan melakukan prediksi dropout.
4. Implementasi dashboard untuk monitoring performa mahasiswa
5. Penyusunan rekomendasi berbasis data untuk meningkatkan retensi mahasiswa

### 📦 Persiapan

* 📁 **Sumber data:** Dataset ini berisi informasi mengenai 4424 mahasiswa dengan 37 variabel yang mencakup berbagai aspek latar belakang mahasiswa, performa akademik, dan status pendidikan. Dataset [students performance](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv) berasal dari Dicoding.

* 📚 **Penjelasan fitur:** Lihat [dokumentasi fitur](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance).

* ⚙️ **Setup environment:**
```
# Membuat environment baru dan mengaktifkannya
conda create --name main-ds python=3.9
conda activate main-ds

# Instalasi dependencies
pip install -r requirements.txt
```

## 📊 Business Dashboard
Dashboard interaktif dibuat menggunakan Metabase dan berisi visualisasi data performa mahasiswa. Dashboard ini memungkinkan stakeholder untuk:
1. Memantau tingkat dropout per program studi
2. Menganalisis hubungan antara faktor demografis, ekonomi dan keberhasilan akademik
3. Mengidentifikasi tren pembayaran biaya kuliah dan dampaknya terhadap status mahasiswa
4. Melihat performa semester pertama sebagai indikator keberhasilan di masa mendatang
   
![Dashboard 1](https://github.com/filzarahma/student-dropout/blob/main/filzrahma-dashboard/School%20Dashboard_page-0001.jpg)

![Dashboard 2](https://github.com/filzarahma/student-dropout/blob/main/filzrahma-dashboard/School%20Dashboard_page-0002.jpg)

* **Statistik Dropout:**
  * 1.421 dari 4.424 mahasiswa mengalami dropout (**32.12%**).

* **Distribusi Dropout:**
  * Berdasarkan course, usia saat masuk, status pembayaran biaya kuliah, serta nilai, jumlah evaluasi, dan jumlah mata kuliah yang disetujui pada semester 1 dan 2.
  * Distribusi visual ditampilkan melalui stacked bar, pie chart, dan line chart.

* **Key Insight:**
  * Program studi dengan dropout rate tertinggi: **Biofuel Production Technologies**, **Equiniculture**, dan **Informatics Engineering**.
  * Dropout meningkat secara signifikan pada kelompok usia **>50 tahun**, tertinggi pada **61–70 tahun (67%)**.
  * Mahasiswa yang **tidak memperbarui status biaya kuliah** (tuition no update) memiliki dropout rate sangat tinggi (**86.5%**).
  * Mahasiswa dropout memiliki rata-rata:
    - Nilai semester 1 dan 2 lebih rendah (**7.26 & 5.90**) dibanding graduate (**12.64 & 12.70**).
    - Jumlah mata kuliah yang disetujui lebih sedikit (**2.55 & 1.94**) dibanding graduate (**6.23 & 6.18**).
    - Jumlah evaluasi semester lebih sedikit dibanding status lainnya.
         
### 🚀 Cara Menjalankan Dashboard Metabase

1. **Install Docker**

   * Unduh dan install Docker Desktop dari [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/).

2. **Siapkan Direktori dan Unduh File Database**

   * Buat folder khusus, misal `metabase-data`, lalu pindahkan file `metabase.db.mv.db` ke folder tersebut.

3. **Buka Command Prompt/Terminal**

   * Arahkan ke folder tempat file database berada (`metabase-data`).
   * Contoh perintah:

     ```bash
     cd path/to/metabase-data
     ```

4. **Jalankan Metabase dengan Docker**

   * Gunakan perintah berikut (otomatis kompatibel untuk Linux/Mac.
     Untuk Windows PowerShell, pastikan format path benar, atau gunakan `//c/metabase-data`):

     ```bash
     docker run -d -p 3000:3000 --name attrition \
       -v "$(pwd)/metabase.db.mv.db:/metabase.db/metabase.db.mv.db" \
       -e "MB_DB_FILE=/metabase.db/metabase.db.mv.db" \
       metabase/metabase
     ```

     > **Catatan:**
     >
     > * Jika di Windows CMD, ganti `$(pwd)` dengan path lengkap, misal:
     >   `-v "C:\metabase-data\metabase.db.mv.db:/metabase.db/metabase.db.mv.db"`
     > * Untuk PowerShell, bisa pakai:
     >   `-v "${PWD}\metabase.db.mv.db:/metabase.db/metabase.db.mv.db"`

5. **Akses Dashboard**

   * Buka browser ke [http://localhost:3000](http://localhost:3000)
   * **Login:**

     * Email: `filzarahmamuflihah@gmail.com`
     * Password: `9Hwbc_DoRV5FlH`
   * Pilih menu **Our Analytics** > **Dashboards** > **School Dashboard** untuk melihat visualisasi.

## 🤖 Menjalankan Sistem Machine Learning
Sistem prediksi dropout mahasiswa yang telah dibuat menggunakan model Random Forest Classifier dengan akurasi 85,98% dan diimplementasikan dalam bentuk sistem website interaktif dengan Streamlit. Sistem ini memungkinkan pengguna untuk memasukkan data mahasiswa dan mendapatkan prediksi risiko dropout secara langsung. Berdasarkan temuan model, berikut adalah 10 faktor tertinggi yang mempengaruhi keputusan dropout mahasiswa.
![image](https://github.com/user-attachments/assets/cf6ec111-76d5-4299-a44c-1987e2a78e5f)


### 🧪 Langkah-langkah Menjalankan Aplikasi
1. **Clone Repository**
   ```bash
   git clone https://github.com/filzarahma/student-dropout.git
   cd student-performance
   ```

2. **Jalankan Aplikasi Streamlit**
   ```bash
   streamlit run app.py
   ```
   
   Aplikasi akan berjalan secara lokal dan akan otomatis terbuka di browser pada alamat `http://localhost:8501`.

Aplikasi juga dapat diakses secara global di [https://student-prediction-admission.streamlit.app/](https://student-prediction-admission.streamlit.app/)

### 🧠 Cara Menggunakan Sistem Machine Learning
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

## 🧾 Conclusion
Dari analisis data mahasiswa dan pengembangan model prediktif, kami mengidentifikasi beberapa faktor kunci yang mempengaruhi risiko dropout:

1. Performa akademik di semester kedua merupakan prediktor terkuat, diikuti oleh performa di semester pertama
2. Status pembayaran biaya kuliah memiliki pengaruh signifikan (87% mahasiswa yang menunggak akan dropout)
3. Program studi tertentu memiliki tingkat dropout yang jauh lebih tinggi (Biofuel Production Technologies: 66.67%)
4. Usia pendaftaran berkorelasi dengan tingkat kelulusan (mahasiswa yang lebih tua berisiko lebih tinggi)
5. Status pernikahan berpengaruh terhadap kemungkinan dropout (terutama mahasiswa dengan status Legally Separated)

### ✅ Rekomendasi Action Items
Berdasarkan temuan analisis, berikut rekomendasi untuk menurunkan tingkat dropout mahasiswa:
- Implementasikan sistem peringatan dini yang memprioritaskan performa semester kedua sebagai indikator kritis
- Kembangkan program bantuan keuangan dan konseling khusus bagi mahasiswa dengan tunggakan biaya kuliah
- Tingkatkan dukungan akademik untuk program studi dengan tingkat dropout tertinggi
- Desain program dukungan khusus untuk mahasiswa yang mendaftar di usia lebih tua
- Evaluasi struktur kurikulum semester kedua yang tampaknya menjadi titik kritis dalam perjalanan akademik mahasiswa
