# Program Rekap dan Analisis Nilai Matematika Kelas Berbasis Python

## 1. Deskripsi Proyek

Program Rekap dan Analisis Nilai Matematika Kelas Berbasis Python merupakan aplikasi berbasis teks yang digunakan untuk membaca, mengolah, dan menganalisis nilai siswa dari berkas teks. Program melakukan validasi data, menghitung statistik dasar, menentukan status ketuntasan berdasarkan Kriteria Ketuntasan Minimal (KKM), serta menyimpan hasil analisis ke dalam berkas laporan.

Proyek ini dikembangkan sebagai implementasi materi Algoritma dan Pemrograman, khususnya penggunaan fungsi, struktur data, validasi masukan, pengolahan berkas, pengujian program, debugging, dokumentasi, serta pengelolaan proyek menggunakan Git dan GitHub.

Program ditujukan untuk membantu proses rekapitulasi dan analisis nilai siswa secara sederhana, sistematis, dan mudah diperiksa.

## 2. Tujuan Program

Program ini memiliki beberapa tujuan, yaitu:

1. Membaca data nama dan nilai siswa dari berkas teks.
2. Memvalidasi data agar hanya data yang memenuhi ketentuan yang digunakan dalam analisis.
3. Menghitung jumlah data valid, nilai rata-rata, nilai tertinggi, dan nilai terendah.
4. Menentukan status ketuntasan siswa berdasarkan KKM.
5. Menampilkan hasil analisis nilai melalui terminal.
6. Menyimpan laporan hasil analisis ke dalam berkas teks.
7. Menguji fungsi dan perilaku program melalui beberapa skenario pengujian otomatis.
8. Mendokumentasikan proses pengembangan, pengujian, dan penggunaan program.

## 3. Fitur Utama

Fitur yang tersedia dalam program meliputi:

- Membaca data nilai siswa dari berkas teks berformat `.txt`.
- Memeriksa format data dan validitas nilai siswa.
- Menangani data yang tidak memenuhi ketentuan.
- Menghitung jumlah data valid.
- Menghitung nilai rata-rata, nilai tertinggi, dan nilai terendah.
- Menentukan status ketuntasan berdasarkan KKM 75.
- Menampilkan daftar nilai dan status ketuntasan siswa.
- Menampilkan ringkasan hasil analisis pada terminal.
- Menyimpan laporan hasil analisis ke dalam berkas teks.
- Menangani kondisi ketika berkas masukan tidak ditemukan.
- Menjalankan pengujian otomatis menggunakan modul `unittest`.

## 4. Teknologi dan Persyaratan

Teknologi yang digunakan dalam pengembangan proyek ini adalah:

- **Bahasa pemrograman:** Python.
- **Editor kode:** Visual Studio Code.
- **Format data masukan:** berkas teks `.txt`.
- **Format laporan:** berkas teks `.txt`.
- **Pengujian otomatis:** modul `unittest` dari pustaka standar Python.
- **Pengelolaan versi:** Git.
- **Repositori proyek:** GitHub.

### Persyaratan

Untuk menjalankan program, komputer perlu memiliki Python yang terpasang dan terminal yang dapat digunakan untuk menjalankan perintah Python.

Visual Studio Code digunakan sebagai lingkungan pengembangan. Git digunakan untuk mengelola perubahan kode dan dokumentasi, sedangkan GitHub digunakan untuk menyimpan repositori proyek secara daring.

## 5. Struktur Proyek

Struktur direktori proyek adalah sebagai berikut:

```text
proyek-analisis-nilai-2225250071/
├── data/
│   ├── nilai_contoh.txt
│   ├── uji_tc01.txt
│   ├── uji_tc02.txt
│   ├── uji_tc03.txt
│   └── uji_tc08.txt
├── output/
│   ├── .gitkeep
│   └── laporan_analisis.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   ├── test_case.md
│   └── scripts/
│       ├── uji_analisis.py
│       ├── uji_data_io.py
│       ├── uji_tc01.py
│       ├── uji_tc02.py
│       ├── uji_tc03.py
│       ├── uji_tc04.py
│       ├── uji_tc05.py
│       ├── uji_tc06.py
│       ├── uji_tc07.py
│       ├── uji_tc08.py
│       └── uji_utilitas.py
├── docs/
│   └── screenshot/
│       └── .gitkeep
├── proposal.md
├── README.md
└── .gitignore
```

**Keterangan direktori dan berkas:**

- `data/` menyimpan data contoh serta berkas masukan untuk beberapa skenario pengujian.
- `output/` digunakan untuk menyimpan laporan hasil analisis program.
- `src/` berisi kode sumber program.
- `src/main.py` mengatur alur utama pelaksanaan program.
- `src/data_io.py` menangani pembacaan data dan penyimpanan laporan.
- `src/analisis.py` menangani validasi serta analisis nilai.
- `src/utilitas.py` menyediakan fungsi pendukung penyusunan laporan.
- `tests/` menyimpan dokumentasi skenario pengujian dan skrip pengujian.
- `tests/test_case.md` mendokumentasikan skenario pengujian, hasil yang diharapkan, hasil aktual, dan status pengujian.
- `tests/scripts/` menyimpan skrip untuk menguji fungsi dan skenario program.
- `docs/screenshot/` disiapkan untuk menyimpan dokumentasi visual proyek.
- `proposal.md` berisi proposal proyek.
- `.gitignore` menentukan berkas atau direktori yang tidak perlu dimasukkan ke repositori Git.
- `README.md` berisi informasi mengenai proyek, cara penggunaan, struktur direktori, dan hasil pengujian.

Catatan: struktur tersebut menggambarkan susunan berkas proyek yang telah didokumentasikan. Pastikan kembali kesesuaiannya dengan isi direktori proyek sebelum pengumpulan.

## 6. Format Data Masukan

Data utama program disimpan dalam berkas `data/nilai_contoh.txt`.

Setiap baris berisi nama siswa dan nilai yang dipisahkan dengan tanda koma.

Contoh data masukan:

```text
Alya,80
Bima,70
Citra,90
Dimas,75
Eka,60
Fajar,85
Gita,95
Hana,65
```

### Ketentuan Data

Data yang digunakan dalam analisis harus memenuhi ketentuan berikut:

1. Nama siswa tidak boleh kosong.
2. Nilai harus dapat dibaca sebagai angka.
3. Nilai yang digunakan dalam analisis harus berada pada rentang 0 sampai 100.
4. Baris kosong atau data dengan format yang tidak sesuai ditangani berdasarkan mekanisme validasi program.
5. Nilai 0 dan 100 termasuk nilai yang valid.
6. KKM yang digunakan dalam proyek ini adalah 75.

Data yang tidak memenuhi ketentuan tidak digunakan sebagai data valid dalam analisis.

## 7. Cara Menjalankan Program

### 7.1 Membuka Direktori Proyek

Buka folder `proyek-analisis-nilai-2225250071` melalui Visual Studio Code.

Kemudian buka terminal PowerShell dan pastikan direktori aktif berada pada folder utama proyek, yaitu folder yang memuat direktori `src`, `data`, dan `output`.

### 7.2 Menjalankan Program Utama

Jalankan perintah berikut pada komputer pengembang yang menggunakan lokasi instalasi Python tersebut:

```powershell
& "C:\Users\USER\.local\bin\python3.14.exe" -m src.main
```

Jika Python sudah terdaftar pada `PATH` komputer, program juga dapat dijalankan menggunakan:

```powershell
python -m src.main
```

Apabila perintah `python` tidak dikenali oleh terminal, gunakan lokasi instalasi Python yang sesuai dengan komputer masing-masing.

### 7.3 Menjalankan Pengujian Otomatis

Pengujian otomatis dapat dijalankan menggunakan perintah berikut pada PowerShell:

```powershell
& "C:\Users\USER\.local\bin\python3.14.exe" -m unittest discover -s tests\scripts -p "uji_tc*.py" -v
```

Jika Python sudah terdaftar pada `PATH`, perintahnya dapat disesuaikan menjadi:

```powershell
python -m unittest discover -s tests\scripts -p "uji_tc*.py" -v
```

Perintah tersebut menjalankan pengujian otomatis untuk berkas yang sesuai dengan pola `uji_tc*.py` di dalam direktori `tests/scripts`.

### 7.4 Hasil Pelaksanaan Program

Setelah program utama dijalankan, program membaca data dari `data/nilai_contoh.txt`, melakukan analisis, menampilkan hasil pada terminal, dan menyimpan laporan ke:

```text
output/laporan_analisis.txt
```

Lokasi Python pada contoh perintah pertama merupakan lokasi khusus komputer pengembang. Pengguna lain perlu menyesuaikan perintah tersebut dengan instalasi Python yang tersedia.

## 8. Hasil Analisis Program

Berdasarkan delapan data siswa pada berkas contoh, program menghasilkan ringkasan sebagai berikut:

| Komponen | Hasil |
|---|---:|
| Jumlah data valid | 8 |
| Jumlah seluruh nilai | 620 |
| Nilai rata-rata | 77,50 |
| Nilai tertinggi | 95 |
| Nilai terendah | 60 |
| KKM | 75 |
| Jumlah siswa tuntas | 5 |
| Jumlah siswa belum tuntas | 3 |

Nilai rata-rata dihitung dengan membagi jumlah seluruh nilai dengan jumlah data valid.

\[
\bar{x}=\frac{620}{8}=77{,}50
\]

Siswa dinyatakan tuntas apabila memperoleh nilai minimal 75. Siswa yang memperoleh nilai di bawah 75 dinyatakan belum tuntas.

Hasil analisis lengkap mencakup daftar nilai setiap siswa dan status ketuntasannya. Laporan tersebut tersimpan dalam berkas `output/laporan_analisis.txt`.

## 9. Pembagian Modul Program

Program disusun dalam beberapa modul untuk memisahkan tanggung jawab setiap bagian.

### 9.1 `src/main.py`

Mengatur alur utama program, mulai dari pemanggilan fungsi pembacaan data, pelaksanaan analisis, penyusunan hasil, hingga penyimpanan laporan.

### 9.2 `src/data_io.py`

Menangani proses pembacaan data siswa dari berkas teks dan penyimpanan hasil analisis ke dalam berkas laporan. Modul ini juga berkaitan dengan penanganan kondisi ketika berkas tidak ditemukan.

### 9.3 `src/analisis.py`

Menangani proses analisis data nilai, termasuk perhitungan statistik dasar dan penentuan status ketuntasan siswa berdasarkan KKM.

### 9.4 `src/utilitas.py`

Menyediakan fungsi pendukung yang digunakan dalam penyusunan atau penyajian laporan analisis.

### 9.5 Direktori `tests/`

Menyimpan dokumentasi skenario pengujian dan skrip untuk memeriksa perilaku program pada berbagai kondisi masukan.

Pemisahan modul tersebut bertujuan membuat kode lebih terstruktur, mudah diperiksa, dan lebih mudah dikembangkan.

## 10. Pengujian Program

Pengujian dilakukan untuk memeriksa apakah program menghasilkan perilaku yang sesuai dengan ketentuan pada berbagai kondisi masukan.

Delapan skenario pengujian otomatis telah dijalankan menggunakan modul `unittest`. Hasil terakhir menunjukkan bahwa seluruh delapan pengujian berhasil.

### 10.1 Ringkasan Kasus Uji

| No. | Skenario | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | Data nilai normal | Statistik dan status ketuntasan sesuai dengan data yang valid | 3 data valid, rata-rata 80, nilai tertinggi 90, nilai terendah 70, 2 siswa tuntas, dan 1 belum tuntas | LULUS |
| 2 | Nilai minimum 0 | Nilai 0 dapat diproses sebagai nilai valid | Nilai minimum 0 berhasil diproses; rata-rata 60, nilai tertinggi 100, dan 2 siswa tuntas | LULUS |
| 3 | Nilai maksimum 100 | Nilai 100 dapat diproses sebagai nilai valid | Nilai tertinggi 100 berhasil diproses; rata-rata 83,33 dan 2 siswa tuntas | LULUS |
| 4 | Nilai di luar rentang | Nilai di luar rentang valid ditangani sesuai ketentuan | Nilai 105 dan -1 ditolak, sedangkan nilai 100 dan 0 tetap valid | LULUS |
| 5 | Berkas tidak ditemukan | Program menangani kondisi berkas masukan tidak tersedia tanpa kesalahan yang tidak tertangani | Pesan berkas tidak ditemukan ditampilkan dan fungsi pembacaan mengembalikan daftar kosong | LULUS |
| 6 | Semua siswa tuntas | Semua siswa dengan nilai minimal 75 dinyatakan tuntas | Rata-rata 90, nilai tertinggi 100, nilai terendah 80, 3 siswa tuntas, dan 0 belum tuntas | LULUS |
| 7 | Nilai di sekitar KKM | Status ketuntasan ditentukan berdasarkan batas KKM 75 | Nilai 80 dan 75 dinyatakan tuntas, sedangkan nilai 60 belum tuntas | LULUS |
| 8 | Tidak ada data valid | Program menangani kondisi ketika tidak terdapat data valid | Baris dengan nama kosong dan nilai di luar rentang ditolak; program menampilkan pesan bahwa tidak ada data valid | LULUS |

### 10.2 Dokumentasi Pengujian

Rincian data masukan, tujuan pengujian, hasil yang diharapkan, hasil aktual, dan kesimpulan setiap skenario dicatat dalam berkas:

`tests/test_case.md`

Skrip pengujian otomatis tersedia di direktori `tests/scripts/`, termasuk pengujian untuk skenario TC-01 sampai TC-08.

Pengujian dilakukan pada data normal, nilai minimum dan maksimum, nilai di luar rentang, berkas yang tidak ditemukan, kondisi semua siswa tuntas, nilai di sekitar KKM, serta kondisi tanpa data valid.

### 10.3 Hasil Pengujian Terakhir

Berdasarkan pelaksanaan perintah pengujian otomatis, hasilnya adalah:

```text
Ran 8 tests
OK
```

Hasil tersebut menunjukkan bahwa delapan skenario pengujian otomatis yang dijalankan berhasil. Hasil ini berlaku untuk skenario yang diuji dan tidak dengan sendirinya menjamin bahwa semua kemungkinan kesalahan telah ditemukan.

## 11. Penanganan Kesalahan dan Masalah yang Diketahui

Program dilengkapi mekanisme validasi untuk menangani data yang tidak sesuai dengan ketentuan. Program juga menangani kondisi ketika berkas masukan tidak ditemukan.

Berdasarkan delapan skenario pengujian otomatis yang telah dijalankan, seluruh skenario tersebut berhasil. Belum ada masalah utama yang teridentifikasi dari skenario pengujian tersebut.

Namun, perilaku program di luar kondisi yang telah diuji belum dapat dipastikan sepenuhnya. Oleh karena itu, pengujian tambahan dapat dilakukan apabila program dikembangkan untuk menangani format data atau kebutuhan baru.

## 12. Pengembangan Selanjutnya

Program masih dapat dikembangkan melalui penambahan fitur, antara lain:

1. Menambahkan antarmuka pengguna yang lebih interaktif.
2. Menyediakan fitur pencarian nama siswa.
3. Menambahkan pengurutan data berdasarkan nilai.
4. Menyediakan pilihan KKM sesuai kebutuhan pengguna.
5. Menambahkan pilihan format keluaran laporan.
6. Memperluas skenario pengujian untuk memeriksa kondisi masukan lainnya.

Fitur-fitur tersebut merupakan rencana pengembangan dan bukan bagian dari fitur yang dinyatakan telah selesai pada versi proyek ini.

## 13. Pengembang dan Kontribusi

**Nama pengembang:** Mutiara Sari

**NIM:** 2225250071

**Kontribusi:**

Pengembang bertanggung jawab atas pengembangan program rekap dan analisis nilai matematika, penyusunan struktur kode, implementasi pembacaan dan pengolahan data, penyusunan laporan, pengujian program, debugging, serta penyusunan dokumentasi proyek.

Bagian ini mencantumkan pengembang dan kontribusi proyek. Jika terdapat anggota lain yang ikut mengerjakan proyek, identitas dan kontribusi mereka perlu ditambahkan sesuai pekerjaan yang benar-benar dilakukan.

## 14. Dokumentasi dan Referensi

Proyek ini dikembangkan sebagai implementasi materi perkuliahan Algoritma dan Pemrograman, khususnya fungsi, struktur data, pengolahan berkas, pengujian program, debugging, dokumentasi, serta penggunaan Git dan GitHub.

Dokumentasi proyek terdiri atas:

- `proposal.md`, sebagai dokumen proposal proyek.
- `README.md`, sebagai panduan penggunaan dan dokumentasi proyek.
- `tests/test_case.md`, sebagai dokumentasi skenario dan hasil pengujian.
- Skrip pada `tests/scripts/`, sebagai implementasi pengujian otomatis.
- Riwayat commit Git, sebagai catatan perubahan selama pengembangan.

Bantuan AI digunakan sebagai pendukung proses pengembangan, pemeriksaan kode, penyusunan skenario pengujian, dan perapian dokumentasi. Kode program, hasil pengujian, dan dokumentasi tetap diperiksa oleh pengembang agar sesuai dengan implementasi proyek.

Referensi teknis utama yang digunakan dalam proyek ini adalah materi perkuliahan Algoritma dan Pemrograman. Referensi tambahan dapat dicantumkan sesuai dokumentasi atau sumber yang benar-benar digunakan selama pengembangan.